# CLAUDE.md

## Project

Personal blog at [dupli.co](https://dupli.co) — a [Pelican](https://getpelican.com/) static site built from Markdown in [content/](content/). Deployed to GitHub Pages by [.github/workflows/pelican.yml](.github/workflows/pelican.yml) on every push to the `default` branch (this repo's main branch is named `default`, not `main`).

## Build & preview

Common commands (see [Makefile](Makefile) for the full list):

- `make devserver` — local dev server with auto-regeneration (default port 8000)
- `make html` — one-shot build into [output/](output/) using [pelicanconf.py](pelicanconf.py)
- `make publish` — production build using [publishconf.py](publishconf.py)
- `make clean` — wipe [output/](output/)

Don't run `make github` — deployment is handled by the GitHub Actions workflow, not locally.

## Writing posts

Posts live under `content/categories/<category>/<slug>.md`. Filename = slug (e.g. [content/categories/ccdc/2025.md](content/categories/ccdc/2025.md)).

Frontmatter uses Pelican's Markdown-metadata style (no YAML fences):

```text
Title: Southwest CCDC Regionals 2025
Date: 2025-03-27
Modified: 2025-03-29
Category: CCDC
```

`Modified:` is optional. To stage a draft, comment in `<!-- Status: draft -->` (or use `Status: draft` without the comment).

**Voice — important:** Do not draft post prose in George's first-person voice unless he explicitly asks for it. Boilerplate, scaffolding (creating the file, frontmatter, directory), build/tooling work, theme/template edits, fixing typos he points out, and technical features are all fair game without asking. If he hands you an outline or rough notes and asks for help shaping prose, that counts as initiating — proceed.

Category creation/reuse guidance is intentionally not specified here yet — ask before adding a new category.

## Images & photo galleries

The photo pipeline is a work in progress. Don't change `PHOTO_*` settings in [pelicanconf.py](pelicanconf.py), the [photos/](photos/) directory layout, or inline-gallery patterns without asking — George is still figuring out where he wants this to land.

Inline images in posts use Pelican's `{lightbox}` / `{photo}` placeholders (see [content/categories/ccdc/2025.md](content/categories/ccdc/2025.md) for examples).

## Don't

- Don't change [pelicanconf.py](pelicanconf.py), [publishconf.py](publishconf.py), or the theme without asking.
- Don't draft post prose in George's voice unless he initiates.
- Don't commit [output/](output/) — it's gitignored and built by CI.
- Don't run `make github` — CI deploys.
- Don't commit to or push the `default` branch without explicit permission — pushes deploy to production. Direct commits to `default` are fine when George says so; just ask first.

## Post backlog

Future post ideas live in [TODO.md](TODO.md). Check it when he asks "what was I going to write about next?" or similar; otherwise leave it alone.
