# Release and changelog process

This repository follows a lightweight, tag-driven release process.

## 1) Prepare a release

1. Ensure CI is green on the release branch.
2. Confirm user-facing changes are reflected in repository docs.
3. Group merged changes into a short release summary.

## 2) Create release tag

Create an annotated semantic version tag (for example `v0.3.0`) and push it.

## 3) Publish release notes

Create a GitHub Release from the tag and include:

- Highlights / notable changes
- Backward-compatibility notes (if any)
- Links to relevant documentation updates

## 4) Changelog source of truth

GitHub Releases are the project changelog source of truth.
