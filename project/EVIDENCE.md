# Evidence log

## REPO-002 — Publish existing ignore rules — 2026-11-25
- Requirement: owner's explicit follow-up to stage, commit and push; AGENTS.md task evidence requirement. Scope: existing .gitignore edit and task records; schema/API contracts unchanged.
- Local validation: npm.cmd test passed 3/3, including existing fail-closed and readiness negative cases. git diff --check passed.
- Ignore validation: git check-ignore --no-index -q with individual path arguments passed for 12 expected ignored probes (dependencies, Google configuration/credentials, environments, keys and local records) and 2 expected trackable probes (.env.example and src/App.gs). Initial PowerShell stdin probe retained carriage returns; individual-argument rerun corrected the test transport.
- Existing edit replaces releases/, *.log and private/ exclusions with the supplied credential/local-record rules; those former patterns are no longer excluded by this file. No files from those locations are staged by this task.
- Integration: push and remote HEAD comparison follow commit creation; no application deployment or live-sheet tests required or performed. No phase gate approved. Next action remains P0 owner decision review.

## REPO-001 — Initial repository publication — 2026-11-25
- Requirement: explicit owner request to set the SSH remote and push the initial commit; AGENTS.md task recording and independent review requirements. No schema/API changes or new application behavior; existing negative tests apply.
- Fixture/version: existing scaffold baseline `3ff845b`; Git branch master. Existing .gitignore edit excluded from task changes.
- Local checks: `npm.cmd test` passed 3/3 (fail-closed RPC, half-open intervals, readiness confirmation); `git diff --check` passed. `npm test` initially hit the PowerShell npm.ps1 execution-policy restriction; npm.cmd completed successfully.
- Independent reviewer: review_initial_push acting under agents/qa-security.md. Reviewed tracked baseline including DOCX XML/relationships; no credential-pattern or email matches, no publication blocker. Live Google resource references in design documents were identified; no live records accessed. Reviewer independently ran 3/3 offline tests successfully. Pattern checks are bounded, not proof of absence of every secret.
- Remote integration: `git ls-remote origin` returned no refs before publication. `git push -u origin master` succeeded, creating remote master at baseline and configuring upstream. origin fetch/push URL confirmed as `git@github.com:Tonnix/salon-operations.git`. Sandbox initially denied .git/config writes and network; authorized elevated Git operations succeeded.
- Expected/observed: existing initial commit published without rewriting history or committing the pre-existing .gitignore change. Task records follow in a separate documentation commit.
- Deployment/production tests: not run; no application deployment, live sheet mutation, or phase gate approval. Next action: owner/orchestrator P0 decision review.
Record requirement, fixture, version, expected, observed, command, result, evidence path, reviewer and approval. Distinguish local, test deployment and production rehearsal. No phase gate passed.
