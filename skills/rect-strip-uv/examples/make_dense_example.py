#!/usr/bin/env python3
"""Generate a dense synthetic rounded strap; never load private production data."""
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np


def subdivide(v, q):
    vertices = list(v.copy())
    edges = {}
    output = []
    for a, b, c, d in q:
        mids = []
        for i, j in ((a, b), (b, c), (c, d), (d, a)):
            key = tuple(sorted((int(i), int(j))))
            if key not in edges:
                edges[key] = len(vertices)
                vertices.append((v[i] + v[j]) * .5)
            mids.append(edges[key])
        m = len(vertices)
        vertices.append((v[a] + v[b] + v[c] + v[d]) * .25)
        ab, bc, cd, da = mids
        output.extend([[a, ab, m, da], [ab, b, bc, m], [m, bc, c, cd], [da, m, cd, d]])
    return np.array(vertices), np.array(output, np.int32)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--levels', type=int, default=5)
    args = p.parse_args()
    if args.output.exists():
        p.error('Refusing to overwrite the output. Choose a new path.')
    if not 0 <= args.levels <= 5:
        p.error('--levels must be 0 through 5.')
    nx, ny = 32, 8
    v = np.array([[12 * i / nx, j / ny, 0.] for i in range(nx + 1) for j in range(ny + 1)])
    q = np.array([[i * (ny + 1) + j, (i + 1) * (ny + 1) + j,
                   (i + 1) * (ny + 1) + j + 1, i * (ny + 1) + j + 1]
                  for i in range(nx) for j in range(ny)], np.int32)
    for _ in range(args.levels):
        v, q = subdivide(v, q)
    x, y = v[:, 0].copy(), v[:, 1].copy()
    x += .45 * (np.exp(-((12 - x) / .8) ** 2) - np.exp(-(x / .8) ** 2)) * np.sin(np.pi * y)
    v = np.c_[3 * np.sin(x / 3), y, 3 * np.cos(x / 3)]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', encoding='utf-8', newline='\n') as f:
        f.write('# Synthetic rounded strap; no customer geometry.\no SyntheticStrap\n')
        for a in v:
            f.write('v ' + ' '.join(format(float(t), '.17g') for t in a) + '\n')
        f.write('g SyntheticRoundedStrap\ns 1\n')
        for face in q:
            f.write('f ' + ' '.join(str(int(i) + 1) for i in face) + '\n')
    print(f'Synthetic input: {len(v)} vertices, {len(q)} quads -> {args.output}')


if __name__ == '__main__':
    main()
