# Lessons learned

Use this file to prevent repeated mistakes across sessions.

## Entry template

* Date:
* Failure signature:
* Root cause:
* Preventive rule:
* Verification added:

---

* Date: 2026-03-02
* Failure signature: Integration screenshot showed mostly unstyled default HTML, causing confusion about missing MUI library modules.
* Root cause: Base template shipped design tokens and JS islands but no shared stylesheet to style existing `.mui-*` server-rendered classes.
* Preventive rule: Keep a baseline stylesheet linked from `django_mui/base.html` whenever new shared utility classes are introduced.
* Verification added: Template contract test now asserts `django_mui/base.css` is linked and stylesheet includes `.mui-alert` classes.
