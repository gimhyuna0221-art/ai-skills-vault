# Method: rectangular body with attached ends

This describes the bundled implementation, not a new simulation or a guarantee of zero distortion. Only UV coordinates and UV references change.

## Inspect topology before solving

Read actual OBJ records, not exported count comments. Accept quad-only input. Preserve coordinates, face order, normals, object/group/smoothing/material declarations. Reject unsupported records and invalid indices. Find connected components, verify edge orientation, vertex fans, one boundary loop and Euler characteristic 1. No holes are filled and no seams are guessed on solids.

## Recover a smaller UV control problem when proven

Recognize exact ordered four-child subdivision blocks and disjoint parent/edge/center roles. Recover only the connectivity needed for UV calculation. Reordered or unrecognized faces are not assumed to have a subdivision history. The original high-resolution mesh stays intact; the solver uses positions at surviving control vertices and later propagates UVs to original edge/face points. This is not geometry decimation or inverse Catmull–Clark position reconstruction.

## Route A: regular quad grid

Traverse adjacent quads into a consistent integer grid. Check the four boundary corners and interior valences. Select the longitudinal direction by accumulated physical edge length, not just polygon count or a fixed world axis. Map accumulated lengths to U and transverse lengths to V. Existing square grid ends remain attached.

## Route B: boundary-constrained parameterization

Choose physical end candidates with mesh-geodesic distances along the connected surface, not Euclidean proximity between overlapping layers. Explicit endpoints are optional and must be valid surviving boundary vertices. Detect ambiguous path lengths or distant topological corners and stop rather than forcing an unreliable result.

Build straight longitudinal rails plus connected rounded UV caps. Estimate a reference width from surface area and boundary lengths. Solve a positive mean-value-weight interior system. Tentative cotangent U relaxation is constrained to preserve rail order and endpoint transitions. Try a finite cap/relaxation candidate schedule, checking UV signs, strict convexity and boundary validity at each attempt. Failure does not authorize removing checks.

Caps are part of the same UV parameterization; there is no geometry detach/reweld. A rounded UV cap is not a claim of distortion-free matching to every source end shape.

## Propagation and packing

Propagate accepted control UVs through proven subdivision levels using edge averages and face averages. Recheck the full-resolution result. Multiple strips share a physical reference scale, use U along length, and occupy separate V ranges. Optional 0–1 packing applies one uniform scale and translation, not independent axis scaling.

## Verify the file that was actually saved

Reload OBJ and compare original vertex text hashes, coordinate arrays, face connectivity/order, normal references and declarations. Check all corners have UVs. Require positive internal UV triangles, strictly convex quads, a simple valid boundary, matching surface/boundary area and disjoint island V ranges. These checks do not measure every form of perceptual texture distortion.

Render the actual full-resolution geometry, not generated lookalike images. Inspect layout plus angled/front checker views. A numeric pass does not certify visual quality, physical plausibility, body collision, MTL completeness or successful import/export in a DCC application.

See [sources](SOURCES.md), [failure handling](TROUBLESHOOTING.md) and the code in `scripts/parameterize.py`.
