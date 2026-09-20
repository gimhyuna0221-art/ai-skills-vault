"""Shape-checked low-poly companion. Never modifies the UV-only high-poly file.

Only recognizes the ordered four-child hierarchy already proven by parameterize.
No UV quantization, decimation, welding, smoothing, or square replacement caps.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import numpy as np
from mesh_io import StopUV, json_write, read_obj, sha256
from parameterize import topology, validate_island


def heavy_input(info, cfg):
    # Each inspected component is an oriented topological disk: V-E+F=1.
    edges = info['vertices'] + info['faces'] - len(info['components'])
    return (info['faces'] >= cfg['lowpoly_face_threshold'] or
            edges >= cfg['lowpoly_edge_threshold']), int(edges)


def face_states(info):
    """Carry object/group/smoothing/material states; never merge across changes."""
    records = info.get('metadata_records', [])
    current = dict.fromkeys(('o', 'g', 's', 'usemtl'), '')
    labels = np.empty(info['faces'], np.int32)
    table = []
    known = {}
    offset = 0
    for boundary in sorted(set([0, info['faces']] + [int(x[0]) for x in records])):
        if boundary > offset:
            state = tuple(current[k] for k in ('o', 'g', 's', 'usemtl'))
            if state not in known:
                known[state] = len(table)
                table.append(state)
            labels[offset:boundary] = known[state]
        for face, line in records:
            if face == boundary:
                key = line.split(None, 1)[0] if line.strip() else ''
                if key in current:
                    current[key] = line
        offset = boundary
    return labels, table


def boundary_error(v, original, reduced):
    """Every original boundary vertex to its corresponding surviving chord."""
    original = np.asarray(original)
    lookup = {int(vid): i for i, vid in enumerate(original)}
    if any(int(vid) not in lookup for vid in reduced):
        raise StopUV('BOUNDARY_CHANGED', 'Reduced boundary is not a source-boundary subset.')
    positions = np.array([lookup[int(i)] for i in reduced])
    steps = (np.roll(positions, -1) - positions) % len(original)
    if np.any(steps == 0) or int(steps.sum()) != len(original):
        raise StopUV('BOUNDARY_CHANGED', 'Source boundary order was not preserved.')
    distances = np.empty(len(original))
    for start, count, a, b in zip(positions, steps, reduced, np.roll(reduced, -1)):
        ix = (int(start) + np.arange(int(count))) % len(original)
        A, B = v[a], v[b]
        d = B - A
        denominator = float(d @ d)
        if denominator == 0:
            raise StopUV('ZERO_LENGTH_EDGE', 'Candidate has a zero-length boundary chord.')
        P = v[original[ix]]
        t = np.clip((P - A) @ d / denominator, 0, 1)
        distances[ix] = np.linalg.norm(P - (A + t[:, None] * d), axis=1)
    return {'samples': len(distances), 'max_world': float(distances.max()),
            'p95_world': float(np.percentile(distances, 95)),
            'source_boundary_order_preserved': True}


def surface_error(v, levels, level):
    """Sample error against the original vertices, not continuous Hausdorff error."""
    q = levels[level]
    ids = np.unique(q)
    prediction = np.full_like(v, np.nan, dtype=float)
    prediction[ids] = v[ids]
    for fine in reversed(levels[:level]):
        children = fine.reshape(-1, 4, 4)
        parent = children[:, np.arange(4), np.arange(4)]
        p = prediction[parent]
        if not np.isfinite(p).all():
            raise StopUV('HIERARCHY_INVALID', 'Candidate interpolation has missing parents.')
        mids = [children[:, 0, 1], children[:, 1, 2], children[:, 2, 3], children[:, 3, 0]]
        for k, mid in enumerate(mids):
            prediction[mid] = (p[:, k] + p[:, (k + 1) % 4]) * .5
        prediction[children[:, 0, 2]] = p.mean(axis=1)
    used = np.unique(levels[0])
    distances = np.linalg.norm(prediction[used] - v[used], axis=1)
    if not np.isfinite(distances).all():
        raise StopUV('HIERARCHY_INVALID', 'Non-finite interpolation error.')
    return {'samples': len(distances), 'max_world': float(distances.max()),
            'p95_world': float(np.percentile(distances, 95)),
            'method': 'Original-vertex samples versus hierarchical bilinear interpolation; not continuous Hausdorff.'}


def choose_level(v, uv, levels, boundary, labels, width, budget,
                 boundary_tolerance=.01, surface_tolerance=.03):
    """Level 0 is full resolution; increasing indices MUST reduce face count."""
    if not np.isfinite(width) or width <= 0:
        raise StopUV('INVALID_WIDTH', 'A positive scene-unit reference width is required.')
    for i in range(1, len(levels)):
        if len(levels[i - 1]) != 4 * len(levels[i]):
            raise StopUV('HIERARCHY_INVALID', 'Coarser levels must have exactly one quarter as many quads.')
    selected = 0
    attempts = []
    for level in range(1, len(levels)):
        q = levels[level]
        record = {'level': level, 'quads': len(q)}
        try:
            child_labels = labels.reshape(-1, 4 ** level)
            if not np.all(child_labels == child_labels[:, :1]):
                raise StopUV('METADATA_BOUNDARY', 'A candidate merges across object/group/material/smoothing states.')
            ids = np.unique(q)
            top = topology(np.searchsorted(ids, q).astype(np.int32), len(ids))
            bd = ids[top['boundary']]
            b = boundary_error(v, boundary, bd)
            s = surface_error(v, levels, level)
            b['max_fraction_of_width'] = b['max_world'] / width
            s['max_fraction_of_width'] = s['max_world'] / width
            record.update(boundary=b, surface=s)
            if b['max_fraction_of_width'] > boundary_tolerance:
                raise StopUV('BOUNDARY_ERROR', 'Rounded-end/rail chord error exceeds the preservation limit.')
            if s['max_fraction_of_width'] > surface_tolerance:
                raise StopUV('SURFACE_ERROR', 'Surface sample error exceeds the preservation limit.')
            p = v[q]
            a = np.cross(p[:, 1] - p[:, 0], p[:, 2] - p[:, 0])
            bnormal = np.cross(p[:, 2] - p[:, 0], p[:, 3] - p[:, 0])
            if np.any(np.einsum('ij,ij->i', a, bnormal) <= 0):
                raise StopUV('FOLDED_QUAD', 'Candidate contains a degenerate or internally reversed quad.')
            record['uv'] = validate_island(uv, q, bd)
            record['accepted'] = True
            selected = level
        except StopUV as exc:
            record.update(accepted=False, code=exc.code, reason=str(exc))
        attempts.append(record)
        # Geometry takes priority over budget. Stop at the first rejected level.
        if not record['accepted'] or len(q) <= budget:
            break
    return selected, attempts


def write_derived(dest, v, q, uv, labels, table, mtllibs):
    """No fabricated material/identity. Host recomputes low-poly normals."""
    if len(v) != len(uv) or len(labels) != len(q):
        raise StopUV('LOWPOLY_EXPORT', 'Inconsistent low-poly table lengths.')
    tmp = dest.with_suffix('.obj.part')
    with tmp.open('w', encoding='utf-8', newline='\n') as f:
        f.write('# rect-strip-uv: derived low-poly companion; original high-poly is separate.\n')
        for name in mtllibs:
            f.write('mtllib ' + name + '\n')
        for p in v:
            f.write('v ' + ' '.join(format(float(x), '.17g') for x in p) + '\n')
        for p in uv:
            f.write('vt ' + ' '.join(format(float(x), '.17g') for x in p) + '\n')
        previous = ('', '', '', '')
        for face, label in zip(q, labels):
            state = table[int(label)]
            for key, old, new in zip(('o', 'g', 's', 'usemtl'), previous, state):
                if old != new:
                    # Empty object/group resets; default smoothing off.
                    f.write((new or ('s off' if key == 's' else key)) + '\n')
            previous = state
            f.write('f ' + ' '.join(f'{int(i)+1}/{int(i)+1}' for i in face) + '\n')
    os.replace(tmp, dest)


def verify_derived(path, v, q, uv, components, labels, table):
    ov, oq, _, info, ou, ot = read_obj(path, with_uv=True)
    out_labels, out_table = face_states(info)
    expected = [table[int(i)] for i in labels]
    actual = [out_table[int(i)] for i in out_labels]
    checks = {'source_sample_positions_exact': np.array_equal(v, ov),
              'quad_connectivity_exact': np.array_equal(q, oq),
              'uv_samples_exact': np.array_equal(uv, ou),
              'uv_indices_valid': np.array_equal(q, ot),
              'all_quads': oq.shape == q.shape,
              'per_face_metadata_preserved': expected == actual}
    if not all(checks.values()):
        raise StopUV('LOWPOLY_RELOAD_FAILED', str(checks))
    islands = []
    ranges = []
    for c in components:
        qq = oq[c['face_start']:c['face_stop']]
        ids = np.unique(qq)
        top = topology(np.searchsorted(ids, qq).astype(np.int32), len(ids))
        islands.append(validate_island(ou, qq, ids[top['boundary']]))
        ranges.append((float(ou[ids, 1].min()), float(ou[ids, 1].max())))
    if any(ranges[i][1] >= ranges[i + 1][0] for i in range(len(ranges) - 1)):
        raise StopUV('LOWPOLY_UV_OVERLAP', 'Low-poly island ranges overlap.')
    return {'file': path.name, 'sha256': sha256(path), 'bytes': path.stat().st_size,
            'checks': checks, 'islands': islands, 'island_bounds_disjoint': True}


def previews(job, v, uv, q, records):
    from PIL import Image, ImageDraw
    from preview import render, font
    paths = []
    p = job.out / 'LOWPOLY_checker.png'
    render(v, q, uv, p, title='LOW-POLY COMPANION | actual exported geometry; inspect caps')
    paths.append(p)
    p = job.out / 'LOWPOLY_layout.png'
    image = Image.new('RGB', (1800, 450), 'white')
    d = ImageDraw.Draw(image)
    d.text((24, 16), 'LOW-POLY UV | uniform scale; original attached end topology', fill='black', font=font(22))
    scale = min(1740 / max(np.ptp(uv[:, 0]), 1e-12), 340 / max(np.ptp(uv[:, 1]), 1e-12))
    screen = (uv - uv.min(0)) * scale
    screen[:, 0] += 30
    screen[:, 1] = 420 - screen[:, 1]
    for face in q:
        a = screen[np.r_[face, face[:1]]]
        d.line([tuple(x) for x in a], fill=(60, 70, 80), width=1)
    image.save(p)
    paths.append(p)
    # End-local PCA views: true source outlines over actual reduced quad wires.
    srcv = job.load('vertices.npy')
    srcuv = job.load('uv_tile.npy')
    shown = records[:8]
    image = Image.new('RGB', (1400, 400 * len(shown)), 'white')
    d = ImageDraw.Draw(image)
    for row, c in enumerate(shown):
        bd = job.load(f'c{c["component"]}_boundary.npy')
        qpart = q[c['face_start']:c['face_stop']]
        bounds = srcuv[bd]
        span = np.ptp(bounds, axis=0)
        for end in (0, 1):
            limit = bounds[:, 0].min() + 1.6 * span[1] if end == 0 else bounds[:, 0].max() - 1.6 * span[1]
            mask = bounds[:, 0] <= limit if end == 0 else bounds[:, 0] >= limit
            points = srcv[bd[mask]]
            if len(points) < 3:
                continue
            center = points.mean(0)
            axes = np.linalg.svd(points - center, full_matrices=False)[2][:2].T
            projected = (points - center) @ axes
            extent = np.maximum(np.ptp(projected, axis=0), 1e-9)
            sc = min(640 / extent[0], 300 / extent[1])
            anchor = np.array([350 + 700 * end, 220 + 400 * row])
            def project(x):
                return (x - center) @ axes * sc + anchor
            meanu = uv[qpart, 0].mean(1)
            selected = qpart[meanu <= limit] if end == 0 else qpart[meanu >= limit]
            for face in selected:
                poly = project(v[np.r_[face, face[:1]]])
                d.line([tuple(a) for a in poly], fill=(85, 95, 105), width=1)
            for i in np.flatnonzero(mask & np.roll(mask, -1)):
                poly = project(srcv[[bd[i], bd[(i + 1) % len(bd)]]])
                d.line([tuple(a) for a in poly], fill=(211, 119, 30), width=2)
            d.text((20 + 700 * end, 12 + 400 * row),
                   f'Strip {c["component"]+1} end {end+1} | source outline / low-poly wires',
                   fill='black', font=font(17))
    p = job.out / 'LOWPOLY_ends.png'
    image.save(p)
    paths.append(p)
    return paths


def run(job):
    info, cfg = job.info(), job.state['config']
    needed, edges = heavy_input(info, cfg)
    report = {'source_sha256': job.state['source_sha256'], 'source_quads': info['faces'],
              'source_edges': edges, 'heavy': needed, 'mode': cfg['lowpoly'],
              'thresholds': {'quads': cfg['lowpoly_face_threshold'], 'edges': cfg['lowpoly_edge_threshold']},
              'target_quads': cfg['lowpoly_target_faces'],
              'boundary_error_limit_fraction_of_width': cfg['lowpoly_boundary_error'],
              'surface_sample_error_limit_fraction_of_width': cfg['lowpoly_surface_error'],
              'highpoly_modified': False}
    path = job.out / 'QA_report_lowpoly.json'
    if cfg['lowpoly'] == 'off' or not needed:
        report['status'] = 'DISABLED_BY_USER' if cfg['lowpoly'] == 'off' else 'NOT_REQUIRED'
        json_write(path, report)
        return [path]
    v, uv = job.load('vertices.npy'), job.load('uv_tile.npy')
    manifest = json.loads((job.work / 'uv_manifest.json').read_text(encoding='utf-8'))
    labels, table = face_states(info)
    allv, alluv, allq, alllabels, records = [], [], [], [], []
    voffset = foffset = 0
    for comp in info['components']:
        c = comp['component']
        levels = [job.load(f'c{c}_level{i}.npy') for i in range(comp['subdivision_levels'] + 1)]
        faceids = job.load(f'c{c}_faces.npy')
        boundary = job.load(f'c{c}_boundary.npy')
        width = float(manifest['components'][c]['reference_width'])
        budget = max(1, round(cfg['lowpoly_target_faces'] * len(levels[0]) / info['faces']))
        level, attempts = choose_level(v, uv, levels, boundary, labels[faceids], width, budget,
                                      cfg['lowpoly_boundary_error'], cfg['lowpoly_surface_error'])
        sourceq = levels[level]
        ids = np.unique(sourceq)
        q = np.searchsorted(ids, sourceq).astype(np.int32)
        record = {'component': c, 'level': level, 'available_levels': len(levels)-1,
                  'source_quads': len(levels[0]), 'quads': len(q), 'vertices': len(ids),
                  'face_start': foffset, 'face_stop': foffset + len(q),
                  'source_vertex_samples_preserved': True, 'attempts': attempts}
        records.append(record)
        allv.append(v[ids]); alluv.append(uv[ids]); allq.append(q + voffset)
        alllabels.append(labels[faceids].reshape(-1, 4 ** level)[:, 0])
        voffset += len(ids); foffset += len(q)
        job.event('lowpoly_component_selected', component=c, level=level, quads=len(q))
    report['components'] = records
    if foffset >= info['faces']:
        report.update(status='BLOCKED', reason='No strictly smaller candidate passed topology, metadata and shape gates. High-poly UV remains available.')
        json_write(path, report)
        return [path]
    V, UV, Q, L = np.vstack(allv), np.vstack(alluv), np.vstack(allq), np.concatenate(alllabels)
    report.update(status='AVAILABLE_NUMERIC_PASS_VISUAL_REVIEW_REQUIRED', vertices=len(V), quads=len(Q),
                  reduction_percent=100 * (1 - len(Q) / info['faces']),
                  target_met=len(Q) <= cfg['lowpoly_target_faces'],
                  topology_method='Existing ordered subdivision levels, never UV-grid reconstruction.',
                  normals='Original normals remain in high-poly. Low-poly normals are recomputed by the importing host.',
                  limitations=['Error bounds cover original boundary/vertex samples, not the continuous surface.',
                               'No collision, thickness, texture baking or DCC round-trip test.',
                               'Components without a safe reduction remain at original density.',
                               'Numeric checks and generated previews do not constitute visual approval.'])
    modes = ['tile', '01'] if cfg['also_01'] else ['tile']
    paths, verified = [], []
    for mode in modes:
        mapping = UV if mode == 'tile' else job.load('uv_01.npy')[np.concatenate([np.unique(job.load(f'c{c["component"]}_level{c["level"]}.npy')) for c in records])]
        p = job.out / f'{job.source.stem}_lowpoly_UV_{mode}.obj'
        write_derived(p, V, Q, mapping, L, table, info.get('mtllibs', []))
        verified.append(verify_derived(p, V, Q, mapping, records, L, table))
        paths.append(p)
    report['files'] = verified
    json_write(path, report)
    paths.append(path)
    paths.extend(previews(job, V, UV, Q, records))
    return paths
