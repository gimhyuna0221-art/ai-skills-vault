#!/usr/bin/env python3
"""UV-only original + automatically checked low-poly companion for dense strips.

The proven UV-only implementation is kept byte-for-byte in uv_core.py.
This entry point adds guarded delivery orchestration, not a replacement UV solver.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_name, '2')
import argparse
import json
import platform
import socket
import sys
import time
import zipfile
from pathlib import Path
try:
    import numpy as np
    import uv_core as core
    import lowpoly
    from mesh_io import StopUV, sha256, json_write
except ImportError as exc:
    print(f'MISSING_DEPENDENCY: {exc}; install requirements.txt', file=sys.stderr)
    raise SystemExit(3)

VERSION = '1.1.1'
# Inherited UV-only QA reports identify the distribution actually running them.
core.VERSION = VERSION
STAGES = ['inspect', 'unwrap', 'export', 'verify', 'preview', 'lowpoly', 'package']
code_hash = core.code_hash


class Job(core.Job):
    def execute(self, stop_after=None):
        if sha256(self.source) != self.state['source_sha256']:
            raise StopUV('SOURCE_CHANGED', 'Input changed. Use a new work directory.')
        if code_hash() != self.state['code_sha256']:
            raise StopUV('CODE_CHANGED', 'Scripts changed. Use a new work directory.')
        for stage in STAGES:
            if stage in self.state['done']:
                for name, digest in self.state['done'][stage]['artifacts'].items():
                    p = self.work / name
                    if not p.is_file() or sha256(p) != digest:
                        raise StopUV('CHECKPOINT_CHANGED', f'Missing or modified checkpoint: {name}')
                self.event('stage_reused', stage=stage)
            else:
                self.state.update(status='RUNNING', current_stage=stage)
                self.save()
                self.event('stage_started', stage=stage)
                start = time.monotonic()
                paths = getattr(self, 'stage_' + stage)()
                self.state['done'][stage] = {
                    'seconds': round(time.monotonic() - start, 3),
                    'artifacts': {str(p.relative_to(self.work)): sha256(p) for p in paths}}
                self.state['current_stage'] = None
                self.save()
                self.event('stage_saved', stage=stage, seconds=self.state['done'][stage]['seconds'])
            if stage == stop_after:
                self.state['status'] = 'CHECKPOINT_SAVED'
                self.save()
                return
        report = json.loads((self.out / 'QA_report_lowpoly.json').read_text(encoding='utf-8'))
        self.state['lowpoly_status'] = report['status']
        self.state['status'] = ('HIGH_POLY_VERIFIED_LOW_POLY_BLOCKED' if report['status'] == 'BLOCKED'
                                else 'NUMERIC_PASS_VISUAL_REVIEW_REQUIRED')
        self.save()
        self.event('delivery_ready', directory=str(self.out), zip=str(self.work / 'rect_strip_uv_delivery.zip'),
                   status=self.state['status'], lowpoly=report['status'], visual_review='required')

    def stage_lowpoly(self):
        return lowpoly.run(self)

    def stage_package(self):
        lp = json.loads((self.out / 'QA_report_lowpoly.json').read_text(encoding='utf-8'))
        high = f'{self.source.stem}_UV_tile.obj'
        low = f'{self.source.stem}_lowpoly_UV_tile.obj'
        summary = {'skill_version': VERSION, 'source_sha256': self.state['source_sha256'],
                   'code_sha256': code_hash(), 'highpoly': high,
                   'highpoly_role': 'UV-only, original vertices/connectivity/normals/metadata preserved',
                   'lowpoly_status': lp['status'],
                   'lowpoly': low if lp['status'].startswith('AVAILABLE') else None,
                   'visual_review': 'REQUIRED',
                   'status': 'HIGH_POLY_VERIFIED_LOW_POLY_BLOCKED' if lp['status'] == 'BLOCKED' else 'NUMERIC_PASS_VISUAL_REVIEW_REQUIRED'}
        receipt = self.out / 'DELIVERY.json'
        json_write(receipt, summary)
        readme = self.out / 'README.txt'
        readme.write_text(
            f'Rect Strip UV {VERSION}\n\nHIGH-POLY (UV-only original): {high}\n'
            f'LOW-POLY status: {lp["status"]}\n'
            + (f'LOW-POLY companion: {low}\n' if summary['lowpoly'] else '')
            + '\nHigh-poly geometry is never replaced by a simplified mesh.\n'
            'For dense inputs, both resolutions are delivered when a safe reduction exists.\n'
            'If reduction is BLOCKED, high-poly is still delivered; no fake low-poly duplicate is produced.\n'
            'Low-poly uses existing quad hierarchy levels, source-coordinate samples and inherited UVs.\n'
            'Rounded ends are not replaced with a rectangular grid. Check LOWPOLY_ends.png.\n'
            'The face budget is soft; sampled shape-error and metadata gates take priority.\n'
            'Low-poly normals are recomputed by the importing host; high-poly normals are preserved.\n'
            'Tile coordinates outside 0-1 mean repeat UVs, not multiple UDIM images.\n'
            'Optional *_01.obj files are uniformly scaled UV alternatives, not additional geometry.\n'
            'MTL/textures are not bundled or invented. Source geometry is never uploaded by this tool.\n'
            'Inspect all checker/layout/end previews. NUMERIC_PASS is not visual approval.\n'
            'See QA_report.json, QA_report_lowpoly.json and DELIVERY.json.\n', encoding='utf-8')
        allowed = [readme, receipt]
        for stage in STAGES:
            if stage == 'package':
                continue
            for name in self.state['done'][stage]['artifacts']:
                if Path(name).parent == Path('delivery'):
                    allowed.append(self.work / name)
        destination = self.work / 'rect_strip_uv_delivery.zip'
        temp = destination.with_suffix('.zip.part')
        with zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED, compresslevel=5, allowZip64=True) as z:
            for path in allowed:
                z.write(path, arcname=path.name)
        with zipfile.ZipFile(temp) as z:
            if z.testzip() is not None:
                raise StopUV('ZIP_INVALID', 'ZIP CRC validation failed.')
        os.replace(temp, destination)
        return [readme, receipt, destination]


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    for command in ('run', 'inspect'):
        s = sub.add_parser(command)
        s.add_argument('--input', type=Path, required=True)
        s.add_argument('--work', type=Path, required=True)
        s.add_argument('--also-01', action='store_true')
        s.add_argument('--max-faces', type=int, default=3_000_000)
        s.add_argument('--max-base-vertices', type=int, default=150_000)
        s.add_argument('--tile-width', type=float, default=None)
        s.add_argument('--endpoints', type=Path)
        s.add_argument('--lowpoly', choices=('auto', 'off'), default='auto',
                       help='auto: add a checked low-poly companion for dense input; off: explicit UV-only override')
        s.add_argument('--also-lowpoly-auto', action='store_const', const='auto', dest='lowpoly',
                       help='Compatibility alias; automatic low-poly is already the default.')
        s.add_argument('--lowpoly-face-threshold', type=int, default=250_000)
        s.add_argument('--lowpoly-edge-threshold', type=int, default=500_000)
        s.add_argument('--lowpoly-target-faces', type=int, default=40_000)
        s.add_argument('--lowpoly-boundary-error', type=float, default=.01,
                       help='Max original-boundary sample deviation divided by belt width.')
        s.add_argument('--lowpoly-surface-error', type=float, default=.03,
                       help='Max original-vertex interpolation error divided by belt width.')
        s.add_argument('--stop-after', choices=STAGES)
    for command in ('resume', 'status'):
        s = sub.add_parser(command)
        s.add_argument('--work', type=Path, required=True)
        if command == 'resume':
            s.add_argument('--stop-after', choices=STAGES)
    sub.add_parser('doctor')
    return p


def main():
    args = parser().parse_args()
    if args.command == 'doctor':
        import scipy, shapely, PIL, numba
        print(json.dumps({'status': 'READY', 'skill': VERSION, 'python': platform.python_version(),
                          'numpy': np.__version__, 'scipy': scipy.__version__, 'shapely': shapely.__version__,
                          'Pillow': PIL.__version__, 'numba': numba.__version__}, indent=2))
        return 0
    work = args.work.resolve()
    state_path = work / 'state.json'
    if args.command == 'status':
        print(state_path.read_text(encoding='utf-8') if state_path.exists() else '{"status":"NOT_STARTED"}')
        return 0
    work.mkdir(parents=True, exist_ok=True)
    if args.command in ('run', 'inspect'):
        source = args.input.resolve()
        if not source.is_file():
            raise StopUV('INPUT_MISSING', str(source))
        if source.suffix.lower() != '.obj':
            raise StopUV('OBJ_REQUIRED', 'Use the actual OBJ, not a screenshot or .max file.')
        if work in source.parents or work == source:
            raise StopUV('UNSAFE_WORK_PATH', 'Keep the input outside the work directory.')
        cfg = {key: getattr(args, key) for key in (
            'also_01', 'max_faces', 'max_base_vertices', 'tile_width', 'lowpoly',
            'lowpoly_face_threshold', 'lowpoly_edge_threshold', 'lowpoly_target_faces',
            'lowpoly_boundary_error', 'lowpoly_surface_error')}
        cfg['endpoints'] = json.loads(args.endpoints.read_text(encoding='utf-8')) if args.endpoints else None
        for key, value in cfg.items():
            if key in ('max_faces', 'max_base_vertices', 'tile_width', 'lowpoly_face_threshold',
                       'lowpoly_edge_threshold', 'lowpoly_target_faces', 'lowpoly_boundary_error', 'lowpoly_surface_error'):
                if value is not None and (not np.isfinite(value) or value <= 0):
                    raise StopUV('INVALID_OPTION', f'{key} must be finite and positive.')
        if state_path.exists():
            state = json.loads(state_path.read_text(encoding='utf-8'))
            if state['input'] != str(source) or state['config'] != cfg:
                raise StopUV('CONFIG_CHANGED', 'Resume the old job or use a new work directory.')
        else:
            state = {'version': VERSION, 'input': str(source), 'source_sha256': sha256(source),
                     'code_sha256': code_hash(), 'config': cfg, 'done': {}, 'status': 'NEW', 'current_stage': None}
            json_write(state_path, state)
    else:
        if not state_path.exists():
            raise StopUV('NO_CHECKPOINT', 'Start with run.')
        state = json.loads(state_path.read_text(encoding='utf-8'))
        if state.get('version') != VERSION:
            raise StopUV('CODE_CHANGED', 'Old-version checkpoints require a new work directory.')
    lock = work / 'run.lock'
    if lock.exists():
        content = json.loads(lock.read_text(encoding='utf-8'))
        stale = False
        if content.get('host') == socket.gethostname() and os.name == 'posix':
            try:
                os.kill(int(content['pid']), 0)
            except ProcessLookupError:
                stale = True
            except PermissionError:
                pass
        if stale:
            lock.unlink()
        else:
            raise StopUV('JOB_LOCKED', f'Check this process before starting another: {content}')
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    with os.fdopen(fd, 'w') as f:
        json.dump({'pid': os.getpid(), 'host': socket.gethostname()}, f)
    job = Job(work, state)
    try:
        job.execute('inspect' if args.command == 'inspect' else args.stop_after)
        return 4 if state['status'] == 'HIGH_POLY_VERIFIED_LOW_POLY_BLOCKED' else 0
    except Exception as exc:
        code = getattr(exc, 'code', 'INTERNAL_ERROR')
        state.update(status='STOPPED', error={'code': code, 'message': str(exc)})
        job.save()
        job.event('stopped', code=code, detail=str(exc))
        return 2
    finally:
        lock.unlink(missing_ok=True)


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except StopUV as exc:
        print(json.dumps({'status': 'STOPPED', 'code': exc.code, 'message': str(exc)}), file=sys.stderr)
        raise SystemExit(2)
