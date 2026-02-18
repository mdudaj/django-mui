# QA Evaluation Spec (Contract)

This document defines the QA expectations for pull requests in this repository.

## Scope

QA evaluation applies to all changes proposed via pull requests targeting `main`.

## Hard gates (must pass)

1. CI workflow passes (`.github/workflows/qa.yml`)
2. Required review approvals are present
3. No direct pushes to `main`

## Scoring

QA scoring uses the rubric in `.governance/qa-policy.yaml`.

### Minimum bar

- Overall result: **Meets bar**
- Any category scored **0** is a block

## Required PR description elements

- What changed and why
- How to test (commands or steps)
- Any risks / migrations / rollbacks

