# Salon Operations V2 — agentic starter
Local-first, platform-neutral repository. No live resources have been created. The revised roadmap is the governing design; source documents are retained verbatim and extracted as text for agents. Start by reading AGENTS.md, project/STATE.md and prompts/START.md. Use Git locally (`git init`, `git add .`, `git commit -m "Starter baseline"`). Node 20+ is recommended; `npm test` runs offline without dependencies. The code is a deliberately fail-closed scaffold, not a functioning salon app.

## Workflow
1. Open this folder in your coding agent. Paste prompts/START.md. Work on P0 only initially.
2. Owner approves decisions and gates; agents cannot self-approve. Each phase produces code, tests, evidence, release notes and updated state. Use prompts/RESUME.md after a session ends.
3. Install clasp only when online: `npm install -g @google/clasp`; `clasp login`; enable Apps Script API in your account. Create a standalone **test** Apps Script project in Drive, then copy its ID into a local `.clasp.json` using config/clasp.example.json. Confirm target before `clasp push`. Use a separate production project and configuration. Never push by default.
4. Create private test operations and contact spreadsheets in Drive; configure IDs via Script Properties only after P1 approval. No credentials or live data in Git. Deployment identity and authentication must be tested with actual accounts; do not assume active-user email is available.
5. Use scripts/package-release.py to build a local release ZIP. Upload approved artifacts to the Drive layout in docs/DRIVE.md manually or via an explicitly authorized Drive connector. Record IDs, version, checksum and approval in project/DRIVE-REGISTER.md. Local source is authoritative; Drive is deliverable storage, not Git.

Offline means editing, agent work (subject to your agent's own connectivity), and local tests. Google API integration, clasp login/push and Drive uploads require internet. No agent runtime or API subscription is bundled.
