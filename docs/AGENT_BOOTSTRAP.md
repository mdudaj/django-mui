```
AGENT_BOOTSTRAP.md
```

---

# 🧠 GitHub CLI Agent Bootstrap Specification

## Project: django-mui (Internal Phase)

---

# Objective

The agent must initialize governance, CI scaffolding, and project structure for `django-mui` using GitHub CLI (`gh`) and standard git workflows.

The repository already exists and `main` is active.

The agent must NOT:

* Push directly to `main`
* Bypass branch protection
* Skip governance files

---

# Phase 1 — Create Bootstrap Branch

The agent must create a feature branch for governance setup.

```bash
git checkout -b chore/governance-bootstrap
```

---

# Phase 2 — Create Governance Structure

Create:

```
.governance/
docs/
.github/workflows/
```

Commands:

```bash
mkdir -p .governance
mkdir -p .github/workflows
mkdir -p docs
```

---

# Phase 3 — Create Required Governance Files

Create:

```
.governance/qa-policy.yaml
.governance/workflow.yaml
docs/OSS_MATURITY_MODEL.md
docs/QA_EVALUATION_SPEC.md
```

These must contain:

* QA scoring policy
* Multi-agent governance flow
* OSS maturity ladder
* QA evaluation contract

(Use previously defined content.)

---

# Phase 4 — Add Minimal QA Workflow

Create:

```
.github/workflows/qa.yml
```

Minimal placeholder:

```yaml
name: QA

on:
  pull_request:
    branches:
      - main

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Basic Validation
        run: echo "QA pipeline initialized"
```

This establishes CI gate.

---

# Phase 5 — Commit Bootstrap Changes

```bash
git add .
git commit -m "chore: governance bootstrap (qa policy + workflow + maturity model)"
git push origin chore/governance-bootstrap
```

---

# Phase 6 — Create Pull Request via GitHub CLI

```bash
gh pr create \
  --title "Governance Bootstrap" \
  --body "Initial governance setup: QA policy, multi-agent workflow, OSS maturity model, CI scaffold." \
  --base main \
  --head chore/governance-bootstrap
```

---

# Phase 7 — Label PR

```bash
gh pr edit --add-label governance
```

If label doesn’t exist:

```bash
gh label create governance --color F29513
```

---

# Phase 8 — Merge Only After Approval

The agent must:

* Wait for QA workflow to pass
* Obtain approval
* Merge using squash strategy

```bash
gh pr merge --squash
```

Direct pushes to `main` are forbidden.

---

# Phase 9 — Initialize Project Board (Optional but Recommended)

Create project:

```bash
gh project create --title "django-mui Internal Phase"
```

Create milestone:

```bash
gh api repos/mdudaj/django-mui/milestones \
  -f title="Phase 1 - Audit & Architecture"
```

Create issue:

```bash
gh issue create \
  --title "Phase 1: django-material Repository Audit" \
  --body "Perform feature inventory and architectural proposal."
```

---

# Governance Enforcement Rules

After bootstrap:

1. All work must be done on feature branches.
2. All merges must go through PR.
3. QA workflow must pass.
4. Architect approval required before merge.
5. No direct push to `main`.

---

# Expected Repository State After Bootstrap

```
django-mui/
├── README.md
├── docs/
│   ├── OSS_MATURITY_MODEL.md
│   └── QA_EVALUATION_SPEC.md
├── .governance/
│   ├── qa-policy.yaml
│   └── workflow.yaml
└── .github/
    └── workflows/
        └── qa.yml
```

---

# Success Criteria

Bootstrap is successful if:

* Governance files exist
* CI workflow runs on PR
* Branch protection active
* First milestone issue created
* No direct commits on main after bootstrap

---
