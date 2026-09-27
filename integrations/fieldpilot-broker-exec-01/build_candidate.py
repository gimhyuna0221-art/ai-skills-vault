"""Build a complete candidate from an exact rc04 Git snapshot; never install it."""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import tarfile

BASE = 'cbfe0f10ef849200450cf1c826586aedcbec6450'
TREE = 'ae50b6294558c35ac7a909aa1dca78fe13844a62'
BLOB = '9d9c837abe600f8a21ac73689825544fe9ccf859'
SUBTREE = 'skills/fieldpilot'
EXTENSION = '''## BROKER-EXEC-01 — PURPOSE, METHOD REUSE, DELIVERY

After STEP 0, preserve company/industry understanding, research interviews, career/event preparation, or the existing product lifecycle without inventing a user product. For substantial research, specialist source/service selection or file delivery, load `references/modules/BROKER_RESEARCH_DELIVERY.md`. Discover new contenders where coverage fails; popularity is not quality. Reuse adequate analysis and investigate material gaps. Curation does not remove a promised report. Route B still recognizes ordinary-language research requests. Verify actual files and substantive QA separately; no second file request is needed.

Only when reusable-method design, economical execution or escalation is relevant, load `references/modules/QUALIFIED_METHOD_EXECUTION.md`. Retrieve an applicable method first. Use a capable designer for new methods/uncertainties and a task/method/runtime-qualified economical executor for repeat work. Refresh volatile facts and escalate affected exceptions. A skill cannot switch models itself. Without authorized dispatch, continue honestly with the current capable host. `tools/broker_control.py` checks declared records and file integrity, not source truth or model intelligence. Deterministic work uses scripts when suitable.

'''


def digest(data):
    return hashlib.sha256(data).hexdigest()


def blob(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def invariants(text):
    body = text.split('## ALWAYS-LOADED INVARIANT KERNEL', 1)[1].split('## STEP 0', 1)[0]
    return dict(re.findall(r'^(\d+)\. (\*\*[^\n]+)', body, re.M))


def transform(data):
    if blob(data) != BLOB:
        raise ValueError('Unreviewed source; no force/rebase-by-guessing option')
    text = data.decode('utf-8')
    original = invariants(text)
    if set(original) != {str(i) for i in range(1, 20)}:
        raise ValueError('Expected 19 rc04 invariants')
    replacements = {
        '  version: "1.9.9-rc04"': '  version: "1.9.9-rc04"\n  extension_revision: "broker-exec-01"',
        '## ROUTE A — ORDINARY BUILDER / MARKET→BUILD': EXTENSION + '## ROUTE A — ORDINARY BUILDER / MARKET→BUILD',
        '- `references/modules/RENDERING_CONTRACT.md` when file rendering is requested/required':
        '- `references/modules/RENDERING_CONTRACT.md` for REPORT or REPORT_PLUS_APPENDIX; do not require a second file request',
        "A full/professional answer is complete only under Route B's existing report/provenance/delivery contracts.":
        "A full/professional answer is complete only under Route B's existing report/provenance/delivery contracts.\n\nBroker curation never cancels report delivery. Check actual nonempty files and usable delivery links, with substantive QA separate from physical-file checks. If file tools are unavailable, provide the full supported output and explicitly disclose ARTIFACT_BLOCKED; never claim a file was delivered."
    }
    for old, new in replacements.items():
        if text.count(old) != 1:
            raise ValueError('Entrypoint anchor drift: ' + old)
        text = text.replace(old, new, 1)
    if invariants(text) != original:
        raise ValueError('Invariant regression')
    return text.encode('utf-8')


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], timeout=60)


def manifest(root):
    return {str(p.relative_to(root)): digest(p.read_bytes()) for p in sorted(root.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts}


def build(output):
    here = Path(__file__).resolve().parent
    repo = Path(git(here, 'rev-parse', '--show-toplevel').decode().strip())
    if git(repo, 'rev-parse', BASE + ':' + SUBTREE).decode().strip() != TREE:
        raise ValueError('Pinned subtree mismatch')
    output = output.resolve()
    if output.exists() or output.is_relative_to(repo):
        raise ValueError('Output must be a new directory outside the source repository')
    output.mkdir(parents=True)
    skill = output / 'fieldpilot'; skill.mkdir()
    raw = git(repo, 'archive', '--format=tar', BASE, SUBTREE)
    if len(raw) > 50_000_000:
        raise ValueError('Archive exceeds bounded size')
    with tarfile.open(fileobj=io.BytesIO(raw)) as archive:
        for entry in archive.getmembers():
            parts = PurePosixPath(entry.name).parts
            if entry.name.startswith('/') or '..' in parts:
                raise ValueError('Unsafe archive path')
            if entry.isdir():
                continue
            if not entry.isfile() or parts[:2] != ('skills', 'fieldpilot'):
                raise ValueError('Only regular files in pinned skill are allowed')
            target = skill.joinpath(*parts[2:]); target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.extractfile(entry).read())
            os.chmod(target, 0o755 if entry.mode & 0o111 else 0o644)
    before = manifest(skill)
    (skill / 'SKILL.md').write_bytes(transform((skill / 'SKILL.md').read_bytes()))
    for incoming in sorted((here / 'overlay').rglob('*')):
        if not incoming.is_file() or '__pycache__' in incoming.parts:
            continue
        if incoming.is_symlink():
            raise ValueError('Overlay links rejected')
        target = skill / incoming.relative_to(here / 'overlay')
        if target.exists():
            raise ValueError('New-file collision: ' + str(target))
        target.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(incoming, target)
    after = manifest(skill)
    changed = sorted(k for k in before if before[k] != after.get(k))
    if changed != ['SKILL.md'] or before.keys() - after.keys():
        raise ValueError('Out-of-scope change')
    report = {'status': 'INTEGRATED_CANDIDATE_TESTS_PENDING', 'base_commit': BASE,
              'base_subtree': TREE, 'base_skill_blob': BLOB,
              'builder_commit': git(repo, 'rev-parse', 'HEAD').decode().strip(),
              'extension': 'broker-exec-01', 'modified': changed,
              'added': sorted(after.keys() - before.keys()), 'unchanged_existing_files': len(before)-1,
              'invariants_preserved': 19, 'files_sha256': after,
              'live_model_eval': 'NOT_RUN', 'quota_or_cost_savings': 'NOT_MEASURED',
              'installed': False, 'merged': False, 'prior_G1_G6_debt': 'INHERITED_NOT_CLOSED'}
    (output / 'BUILD_MANIFEST.json').write_text(json.dumps(report, indent=2, ensure_ascii=False)+'\n')
    return output


def verify(output):
    output = output.resolve(); skill = output / 'fieldpilot'
    proc = subprocess.run(['python', '-m', 'unittest', 'discover', '-s', str(skill / 'tests'),
                           '-p', 'test_*.py', '-v'], capture_output=True, text=True, timeout=180)
    (output / 'TEST_LOG.txt').write_text((proc.stdout + proc.stderr).replace(str(output), 'CANDIDATE_ROOT'))
    if proc.returncode:
        raise ValueError('Candidate tests failed; inspect TEST_LOG.txt')
    smoke = output / 'renderer_smoke'; smoke.mkdir()
    doc = '# Synthetic renderer test\n\nNo real market findings.\n\n## Findings\n\nFixture number: 12.\n\nReference: [https://example.org/fixture](https://example.org/fixture)\n\n`UNKNOWN`\n'
    (smoke / 'REPORT.md').write_text(doc)
    rendering = subprocess.run(['python', str(skill / 'tools/render_report.py'), '--input', str(smoke/'REPORT.md'),
                                '--outdir', str(smoke), '--no-pdf'], capture_output=True, text=True, timeout=60)
    (output / 'RENDER_LOG.txt').write_text((rendering.stdout+rendering.stderr).replace(str(output), 'CANDIDATE_ROOT'))
    if rendering.returncode or not list(smoke.glob('*.html')):
        raise ValueError('HTML smoke failed')
    for cache in skill.rglob('__pycache__'):
        shutil.rmtree(cache)
    meta = json.loads((output / 'BUILD_MANIFEST.json').read_text())
    if manifest(skill) != meta['files_sha256']:
        raise ValueError('Tests modified candidate source')
    count = re.search(r'Ran (\d+) tests?', proc.stdout+proc.stderr)
    meta.update(status='INTEGRATED_CANDIDATE_CONTRACT_TESTS_PASS',
                actual_test_count=int(count.group(1)) if count else None,
                html_smoke='PASS_SYNTHETIC_INPUT', pdf='NOT_RUN')
    (output / 'BUILD_MANIFEST.json').write_text(json.dumps(meta, indent=2, ensure_ascii=False)+'\n')
    (output / 'VALIDATION_STATUS.md').write_text('# Candidate, not production approval\n\nExisting and extension contract tests passed on this generated snapshot. HTML rendering passed on synthetic input. No live economical-model comparison, semantic research benchmark, token/quota saving, PDF QA or G1-G6 completion is claimed. See manifest and logs. Do not replace an approved installation automatically.\n')
    print(json.dumps({k:v for k,v in meta.items() if k!='files_sha256'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    if args.verify:
        verify(args.output)
    else:
        build(args.output)
