# Low-poly companion contract (1.1.1)

The UV-only original is mandatory. Coarsening is a separate optional-in-light-input, automatic-in-dense-input branch. Do not use the faulty 1.1.0 local ZIP as a release base; this implementation builds on the published 1.0.1 tree.

## Algorithm

1. Inspect the source as oriented open quad disks. Euler counts give actual edges `E = V + F - number_of_disks`. Trigger at the configured face OR edge threshold.
2. Keep the UV solver and the exact high-poly export/reload contract unchanged. The original file is never overwritten.
3. Read the proven ordered four-child hierarchy: level 0 = original, level 1 = F/4, level 2 = F/16. Assert this direction; do not reverse-index from the control cage.
4. For each component, consider existing coarser levels. Preserve every surviving source vertex coordinate and corresponding solved UV. Never average source positions into a newly quantized UV grid.
5. Require oriented manifold disk topology, the same boundary order, positive/non-overlapping UVs and nondegenerate, non-reversed quad triangulations. Refuse a parent whose descendants cross object/group/material/smoothing states.
6. Compare every original boundary vertex to its corresponding reduced boundary chord; require max distance <= 1% of reference strip width by default. This includes rounded ends and rails, not just the middle.
7. Prolong candidate positions through the known hierarchy and compare original surface vertex samples; require max error <= 3% of width by default. This is a sampled hierarchical bilinear check, not certified continuous Hausdorff distance or a collision test.
8. Stop on the first rejected coarser level. A soft total budget is distributed in proportion to source component faces. Keep a denser level when preservation requires it. No common grid or equal-density forcing across unrelated strips.
9. Require a strictly smaller total face count. If no safe reduction exists, preserve high-poly output, report BLOCKED, and do not create a fake low-poly file.
10. Export with original per-face metadata states and re-import to check exact surviving samples, UV references, connectivity, disk topology and UV islands. Low-poly normals are recomputed by the host; high-poly normals are unchanged.

Output `QA_report_lowpoly.json` contains tried/rejected candidates, chosen levels, sample-error statistics, exact output hashes and reload checks. `LOWPOLY_ends.png` overlays original outlines over the actual reduced wireframe in endpoint-local projections. Numeric success still requires actual visual review.

## Validation boundaries

Rounded silhouette preservation is enforced within the stated sample tolerances, not exact continuous identity. Fine sculpt details can change; keep high-poly for baking/detail reference. Edited/reordered subdivision blocks can prevent coarsening, and supported geometry may still exceed the UV solve resource limit. Do not relax guards merely to obtain a smaller count.

## References

- Existing implementation and original-input reduction evidence supplied in this project: subdivision-connectivity restoration, surviving source samples and original boundary-chord checks. This is the primary algorithm basis; customer assets are not published.
- Blender manual, Decimate / Un-Subdivide: https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/decimate.html — conceptual reference for grid subdivision reversal, not a claim that Blender's operator is called.
- Published UV-only core and preservation tests in this repository remain the source for UV behavior.
