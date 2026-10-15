# Maintaining the book

The book is a [Jupyter Book](https://jupyterbook.org) (version 1, Sphinx Book Theme). It has two kinds of pages:

- **Generated pages:** the numbered part folders (`01-well-being/` … `10-faculty/`) and `_toc.yml`. They're built from `source/unsolicited-advice-posts.md` by `tools/build_book.py`.
- **Hand-written pages:** `intro.md`, `preface.md`, `how-to-use.md`, `checklists.md` and `about-the-series.md`. The script never touches them.

## Set up once

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Regenerate the post pages

```bash
.venv/bin/python tools/build_book.py source/unsolicited-advice-posts.md .
```

This deletes and rewrites the numbered part folders and `_toc.yml`, so make edits to post pages in the source file or the script, not in the generated files.

## Build and preview

```bash
.venv/bin/jupyter-book build .
```

Then open `_build/html/index.html` in a browser. If the sidebar looks stale, run `.venv/bin/jupyter-book clean .` first.

## Adding a new post

1. Add the post to `source/unsolicited-advice-posts.md` in the same format as the others (heading, `**Date:**`, `**URL:**`, quoted text).
2. In `tools/build_book.py`, add `("YYYY-MM-DD", "Title")` to the right part in `CHAPTERS`. The script stops with an error if any post is left unassigned.
3. Regenerate, then update the counts in `intro.md` and `about-the-series.md`.

## Publishing

Pushing to `main` on GitHub runs `.github/workflows/deploy.yml`, which builds the book and publishes it to GitHub Pages.

## Private files

`private/` is ignored by git. It holds the per-post LinkedIn analytics (`unsolicited-advice-engagement.csv`) and the full collected file, including reposts of other authors' posts, so they never end up in the public repository.
