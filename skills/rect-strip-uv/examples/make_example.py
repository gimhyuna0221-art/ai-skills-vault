"""Generate a small synthetic bent quad strip; never overwrites an existing file."""
from __future__ import annotations
import argparse
import math
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    nx, ny = 48, 8
    with args.output.open('x', encoding='utf-8', newline='\n') as out:
        out.write('# Synthetic example; not a user mesh\no SyntheticStrap\n')
        for i in range(nx + 1):
            x = i / nx * 12
            for j in range(ny + 1):
                out.write(f'v {3*math.sin(x/3):.12g} {j/ny:.12g} {3*math.cos(x/3)+.04*math.sin(3*x):.12g}\n')
        for i in range(nx):
            for j in range(ny):
                a = i * (ny + 1) + j + 1
                b = (i + 1) * (ny + 1) + j + 1
                out.write(f'f {a} {b} {b+1} {a+1}\n')
    print(f'Created {args.output}: 441 vertices, 384 quads')


if __name__ == '__main__':
    main()
