"""Regressions for the 1.1.1 dual-resolution contract; synthetic geometry only."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
import numpy as np
from test_workflow import strip, subdivision, write, ROOT
sys.path.insert(0, str(ROOT / 'scripts'))
from mesh_io import StopUV, read_obj, sha256
from parameterize import coarse_levels, topology, unwrap, prolong
from lowpoly import heavy_input, face_states, choose_level, boundary_error, write_derived, verify_derived
from rect_strip_uv import parser


def fixture(rounded=False, depth=2):
    v, q = strip(48 if rounded else 16, 12 if rounded else 4)
    for _ in range(depth):
        v, q = subdivision(v, q)
    if rounded:
        x, y = v[:, 0].copy(), v[:, 1].copy()
        v[:, 0] += .45 * (np.exp(-((12 - x) / .8) ** 2) - np.exp(-(x / .8) ** 2)) * np.sin(np.pi * y)
        v[:, 2] = .015 * np.sin(x * .4)
    levels = coarse_levels(q)
    ids = np.unique(levels[-1])
    uv, _, _ = unwrap(v[ids], np.searchsorted(ids, levels[-1]).astype(np.int32))
    uv = prolong(levels, ids, uv, len(v))
    return v, q, levels, uv, topology(q, len(v))['boundary']


class LowpolyTests(unittest.TestCase):
    def test_default_auto_and_compatibility_alias(self):
        args = parser().parse_args(['run', '--input', 'a.obj', '--work', 'work'])
        self.assertEqual(args.lowpoly, 'auto')
        args = parser().parse_args(['run', '--input', 'a.obj', '--work', 'work', '--also-lowpoly-auto'])
        self.assertEqual(args.lowpoly, 'auto')

    def test_heavy_uses_real_edges_or_faces(self):
        cfg = {'lowpoly_face_threshold': 100, 'lowpoly_edge_threshold': 180}
        info = {'vertices': 95, 'faces': 90, 'components': [{}]}
        self.assertEqual(heavy_input(info, cfg), (True, 184))
        info.update(vertices=10, faces=10)
        self.assertEqual(heavy_input(info, cfg), (False, 19))
        info.update(vertices=1, faces=100)
        self.assertTrue(heavy_input(info, cfg)[0])

    def test_levels_reduce_not_restore_high_resolution(self):
        v, q, levels, uv, bd = fixture()
        level, records = choose_level(v, uv, levels, bd, np.zeros(len(q), np.int32), 1., 64)
        self.assertGreater(level, 0)
        self.assertEqual(len(levels[level]), 64)
        self.assertLess(len(levels[level]), len(q))
        self.assertTrue(all(x['accepted'] for x in records))

    def test_reversed_level_order_is_rejected(self):
        v, q, levels, uv, bd = fixture()
        with self.assertRaises(StopUV) as exc:
            choose_level(v, uv, list(reversed(levels)), bd, np.zeros(len(q), np.int32), 1., 64)
        self.assertEqual(exc.exception.code, 'HIERARCHY_INVALID')

    def test_rounded_ends_keep_original_quad_flow(self):
        v, q, levels, uv, bd = fixture(rounded=True)
        original = v.copy()
        level, records = choose_level(v, uv, levels, bd, np.zeros(len(q), np.int32), 1., 576)
        self.assertGreater(level, 0)
        self.assertTrue(np.array_equal(v, original))
        cq = levels[level]
        ids = np.unique(cq)
        top = topology(np.searchsorted(ids, cq).astype(np.int32), len(ids))
        reduced_boundary = ids[top['boundary']]
        error = boundary_error(v, bd, reduced_boundary)
        self.assertLessEqual(error['max_world'], .01)
        self.assertTrue(error['source_boundary_order_preserved'])
        # Cap still bulges past the start rail; no square-grid replacement.
        self.assertLess(v[reduced_boundary, 0].min(), -.4)
        self.assertTrue(all(x['accepted'] for x in records))

    def test_sampled_surface_damage_blocks_reduction(self):
        v, q, levels, uv, bd = fixture()
        v[-1, 2] += 2
        level, records = choose_level(v, uv, levels, bd, np.zeros(len(q), np.int32), 1., 64)
        self.assertEqual(level, 0)
        self.assertEqual(records[0]['code'], 'SURFACE_ERROR')

    def test_boundary_damage_blocks_reduction(self):
        v, q, levels, uv, bd = fixture()
        removed = next(int(i) for i in bd if i not in set(np.unique(levels[1])))
        v[removed, 2] += 1
        level, records = choose_level(v, uv, levels, bd, np.zeros(len(q), np.int32), 1., 64)
        self.assertEqual(level, 0)
        self.assertEqual(records[0]['code'], 'BOUNDARY_ERROR')

    def test_no_merging_across_material_or_group_change(self):
        v, q, levels, uv, bd = fixture()
        labels = np.zeros(len(q), np.int32)
        labels[0] = 1
        level, records = choose_level(v, uv, levels, bd, labels, 1., 64)
        self.assertEqual(level, 0)
        self.assertEqual(records[0]['code'], 'METADATA_BOUNDARY')

    def test_no_hierarchy_does_not_invent_lowpoly(self):
        v, q = strip(16, 4)
        uv, _, top = unwrap(v, q)
        level, records = choose_level(v, uv, [q], top['boundary'], np.zeros(len(q), np.int32), 1., 10)
        self.assertEqual((level, records), (0, []))

    def test_derived_export_reloads_positions_uv_and_metadata(self):
        v, q, levels, uv, bd = fixture()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            source, dest = tmp / 'source.obj', tmp / 'low.obj'
            write(source, v, q, normals=True, old_uv=True)
            vv, qq, _, info, _, _ = read_obj(source)
            labels, table = face_states(info)
            ids = np.unique(levels[-1]); lowq = np.searchsorted(ids, levels[-1]).astype(np.int32)
            lowlabels = labels.reshape(-1, 16)[:, 0]
            write_derived(dest, vv[ids], lowq, uv[ids], lowlabels, table, info['mtllibs'])
            report = verify_derived(dest, vv[ids], lowq, uv[ids],
                                    [{'face_start': 0, 'face_stop': len(lowq)}], lowlabels, table)
            self.assertTrue(all(report['checks'].values()))

    def test_uv_flip_is_rejected_for_lowpoly_too(self):
        v, q = strip(16, 4)
        uv, _, _ = unwrap(v, q); uv[:, 1] *= -1
        labels = np.zeros(len(q), np.int32); table = [('', '', '', '')]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'flipped.obj'
            write_derived(path, v, q, uv, labels, table, [])
            with self.assertRaises(StopUV):
                verify_derived(path, v, q, uv, [{'face_start': 0, 'face_stop': len(q)}], labels, table)

    def call(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'scripts/rect_strip_uv.py'), *map(str, args)],
                              capture_output=True, text=True, timeout=180)

    def test_cli_heavy_delivers_both_real_resolutions_and_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); src = tmp / 'dense.obj'; work = tmp / 'job'
            v, q, *_ = fixture(); write(src, v, q, normals=True, old_uv=True)
            digest = sha256(src)
            result = self.call('run', '--input', src, '--work', work, '--also-01',
                               '--lowpoly-face-threshold', 1, '--lowpoly-target-faces', 64)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            high = work / 'delivery/dense_UV_tile.obj'; low = work / 'delivery/dense_lowpoly_UV_tile.obj'
            sv, sq, *_ = read_obj(src); hv, hq, *_ = read_obj(high); lv, lq, *_ = read_obj(low)
            self.assertTrue(np.array_equal(sv, hv)); self.assertTrue(np.array_equal(sq, hq))
            self.assertEqual(len(lq), 64); self.assertLess(len(lq), len(sq))
            self.assertEqual(sha256(src), digest)
            report = json.loads((work / 'delivery/QA_report_lowpoly.json').read_text())
            self.assertEqual(len(report['files']), 2)
            with zipfile.ZipFile(work / 'rect_strip_uv_delivery.zip') as z:
                self.assertIn(high.name, z.namelist()); self.assertIn(low.name, z.namelist())
                self.assertIn('LOWPOLY_ends.png', z.namelist()); self.assertIsNone(z.testzip())

    def test_cli_light_input_returns_only_original_uv(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); src = tmp / 'small.obj'; work = tmp / 'job'
            v, q = strip(16, 4); write(src, v, q)
            r = self.call('run', '--input', src, '--work', work)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            report = json.loads((work / 'delivery/QA_report_lowpoly.json').read_text())
            self.assertEqual(report['status'], 'NOT_REQUIRED')
            self.assertFalse(list((work / 'delivery').glob('*lowpoly*.obj')))

    def test_cli_heavy_without_safe_reduction_reports_partial(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); src = tmp / 'edited.obj'; work = tmp / 'job'
            v, q = strip(16, 4); write(src, v, q)
            r = self.call('run', '--input', src, '--work', work, '--lowpoly-face-threshold', 1)
            self.assertEqual(r.returncode, 4, r.stdout + r.stderr)
            self.assertTrue((work / 'delivery/edited_UV_tile.obj').exists())
            self.assertFalse(list((work / 'delivery').glob('*lowpoly*.obj')))
            state = json.loads((work / 'state.json').read_text())
            self.assertEqual(state['status'], 'HIGH_POLY_VERIFIED_LOW_POLY_BLOCKED')
            self.assertTrue((work / 'rect_strip_uv_delivery.zip').exists())

    def test_explicit_off_respects_uv_only_override(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); src = tmp / 'a.obj'; work = tmp / 'job'
            v, q, *_ = fixture(); write(src, v, q)
            r = self.call('run', '--input', src, '--work', work, '--lowpoly-face-threshold', 1, '--lowpoly', 'off')
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            report = json.loads((work / 'delivery/QA_report_lowpoly.json').read_text())
            self.assertEqual(report['status'], 'DISABLED_BY_USER')

    def test_lowpoly_checkpoint_tampering_blocks_resume(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); src = tmp / 'a.obj'; work = tmp / 'job'
            v, q, *_ = fixture(); write(src, v, q)
            r = self.call('run', '--input', src, '--work', work, '--lowpoly-face-threshold', 1,
                          '--lowpoly-target-faces', 64, '--stop-after', 'lowpoly')
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            path = work / 'delivery/a_lowpoly_UV_tile.obj'
            with path.open('a') as f:
                f.write('# tamper\n')
            r = self.call('resume', '--work', work)
            self.assertEqual(r.returncode, 2)
            self.assertIn('CHECKPOINT_CHANGED', r.stdout + r.stderr)

    def test_invalid_budget_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp); src = tmp / 'a.obj'; v, q = strip(16, 4); write(src, v, q)
            r = self.call('run', '--input', src, '--work', tmp / 'job', '--lowpoly-target-faces', -1)
            self.assertEqual(r.returncode, 2)
            self.assertIn('INVALID_OPTION', r.stdout + r.stderr)


if __name__ == '__main__':
    unittest.main()
