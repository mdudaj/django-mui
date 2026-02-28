# Copilot instructions for `django-mui`

- Keep changes minimal and focused on the requested issue.
- Prefer server-first Django patterns already used in this repository.
- Reuse the existing base template blocks in `django_mui/templates/django_mui/base.html` (`page_title`, `actions`, `navigation`, `content`) instead of introducing new layout patterns.
- Keep shared design tokens sourced from `django_mui/design_tokens.py`.
- Preserve the React island contract implemented by `django_mui/templatetags/django_mui_islands.py` and `django_mui/static/django_mui/react_islands.js`.
- For validation, run the same checks as CI:
  - `ruff check .`
  - `ruff check . --select S`
  - `python -m unittest discover -s tests -p "test_*.py"`
