# Synthetic example

From the skill root:

```bash
python examples/make_example.py --output "demo-input/strap.obj"
python scripts/rect_strip_uv.py run --input "demo-input/strap.obj" --work "demo-job" --also-01
```

The generator creates 441 vertices and 384 quads, a curved thin strip with no customer geometry. It uses exclusive file creation and refuses to overwrite existing data. Use fresh paths for another independent run.

Inspect demo-job/delivery/UV_layout.png, UV_checker.png and UV_checker_front.png, and read QA_report.json. The demonstration is a simple grid case; it is not a substitute for testing arbitrary rounded ends, private production assets or other models. The automated suite separately exercises explicit capsule endpoints, subdivision and rejection paths.
