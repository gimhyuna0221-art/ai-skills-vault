# Troubleshooting

Never fix a rejected UV job by silently changing geometry or weakening validation. Keep the source outside the job directory.

| Signal | Meaning | Next action |
|---|---|---|
| INPUT_MISSING / OBJ_REQUIRED | No usable OBJ at the supplied path | Confirm the mounted file; request the actual OBJ, not a screenshot or .max file |
| MISSING_DEPENDENCY / exit 3 | Python package unavailable | Install requirements in the authorized execution environment; rerun doctor |
| QUADS_REQUIRED | Triangles or n-gons are present | Report the unsupported input; do not remesh automatically |
| NOT_DISK / NOT_OPEN_STRIP / MULTIPLE_BOUNDARIES | Solid, welded closed ring, hole or another unsupported topology | A separate selection/seam workflow is required; leave the original intact |
| NONMANIFOLD / NONMANIFOLD_VERTEX / INCONSISTENT_WINDING | Invalid edge/fan connectivity or winding | Stop and report; no automatic welding or normal repair |
| LOOSE_VERTICES / ZERO_LENGTH_EDGE / ZERO_AREA_GEOMETRY | Degenerate or unused geometry | Stop; do not silently delete vertices |
| RESOURCE_LIMIT | Configured face/control-vertex safety cap exceeded | State exact count and limit; do not infer a subdivision history or decimate |
| ENDPOINT_AMBIGUITY / INVALID_ENDPOINTS | End heuristic or supplied endpoints are unreliable | Inspect actual geometry; advanced endpoint JSON uses component keys and 1-based source vertex IDs surviving the control hierarchy |
| UV_FOLDOVER / UV_QA_FAILED | All bounded UV candidates failed | Return the exact error, not a fake finished OBJ; do not remove checks |
| SOURCE_CHANGED / CONFIG_CHANGED / CODE_CHANGED | Existing job no longer matches | Use a fresh work directory; never reuse by filename alone |
| CHECKPOINT_CHANGED | A completed artifact is absent or altered | Preserve evidence and start a new job rather than editing hashes |
| JOB_LOCKED | Another job may be active | Check the process and host before changing anything; never run duplicate workers |

## After a tool timeout

Read `state.json` and `progress.jsonl`, check the process, then use `status` and `resume` on the same work path. A logged RUNNING state is not proof of an active process. Completed stages are reused only after source/code/artifact hashes match. An incomplete stage may restart internally. `.part` is not a finished file.

On the same POSIX host the CLI can recognize a dead PID and remove a stale lock. It does not perform that liveness check for a foreign host or Windows. Do not blindly delete a lock based only on its age.

Version 1.0.1 changes the script hash. Jobs created with 1.0.0 need a fresh work directory; the source stays untouched.

## Texture and display questions

UVs beyond 0–1 are intentional for repeating maps, not a multi-image UDIM export. The 0–1 alternative preserves aspect ratio and may occupy a thin area of the square. UV distortion can remain on curved ends or deep folds. MTL/textures are not invented or copied from external paths. Imported scale is not assumed centimeters.

Read `delivery/QA_report.json`, then open all three preview images. Numeric success cannot substitute for this visual check. File/ZIP creation alone also does not establish successful DCC round-trip import.
