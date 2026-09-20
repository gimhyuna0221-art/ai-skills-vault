"""Assert actual exported dense-job artifacts and emit commit-bound CI evidence."""
from pathlib import Path
import json
import os
import sys
import zipfile

work = Path(sys.argv[1])
qa = json.loads((work / 'delivery/QA_report.json').read_text(encoding='utf-8'))
low = json.loads((work / 'delivery/QA_report_lowpoly.json').read_text(encoding='utf-8'))
receipt = json.loads((work / 'delivery/DELIVERY.json').read_text(encoding='utf-8'))
assert qa['source_quads'] >= 250000, 'Demo must exercise the real default density threshold.'
assert low['status'] == 'AVAILABLE_NUMERIC_PASS_VISUAL_REVIEW_REQUIRED', low
assert 0 < low['quads'] < qa['source_quads'], 'A high-poly duplicate is not a low-poly result.'
assert all(all(f['checks'].values()) for f in qa['files'])
assert all(all(f['checks'].values()) for f in low['files'])
assert all(i['source_vertex_samples_preserved'] for i in low['components'])
assert (work / 'delivery/LOWPOLY_ends.png').is_file()
with zipfile.ZipFile(work / 'rect_strip_uv_delivery.zip') as z:
    assert receipt['highpoly'] in z.namelist()
    assert receipt['lowpoly'] in z.namelist()
    assert z.testzip() is None
result = {'head_sha': os.environ.get('GITHUB_SHA'), 'run_id': os.environ.get('GITHUB_RUN_ID'),
          'runner_os': os.environ.get('RUNNER_OS'), 'skill_version': receipt['skill_version'],
          'code_sha256': receipt['code_sha256'], 'synthetic_input': True,
          'highpoly_quads': qa['source_quads'], 'lowpoly_quads': low['quads'],
          'highpoly_preservation_checks': 'PASS', 'lowpoly_export_reload_checks': 'PASS',
          'rounded_boundary_and_surface_sample_gates': 'PASS', 'both_resolutions_packaged': True,
          'visual_review': 'NOT_PERFORMED_BY_CI', 'DCC_roundtrip': 'NOT_PERFORMED'}
(work / 'delivery/CI_RECEIPT.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
