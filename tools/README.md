# Maintaining the book

The book is a [Jupyter Book](https://jupyterbook.org) (version 1, Sphinx Book Theme). It has two kinds of pages:

- **Generated pages:** the numbered part folders (`01-well-being/` … `10-faculty/`) and `_toc.yml`. They're built from `source/unsolicited-advice-posts.md` (the series) and `source/more-advice-posts.md` (advice posts written without the "Unsolicited advice" opener) by `tools/build_book.py`.
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

1. Add the post to `source/unsolicited-advice-posts.md` (posts that open with "Unsolicited advice") or `source/more-advice-posts.md` (the rest) in the same format as the others (heading, `**Date:**`, `**URL:**`, quoted text).
2. In `tools/build_book.py`, add `"<activity id>": ("<part folder>", "Title")` to `LATER_SERIES` or `MORE`, matching the file you added it to. New entries go at the end of their part, so existing page links don't change. The script stops with an error if any post is left unassigned.
3. Regenerate, then update the counts in `intro.md` and `about-the-series.md`.

## Publishing

Pushing to `main` on GitHub runs `.github/workflows/deploy.yml`, which builds the book and publishes it to GitHub Pages.

## Private files

`private/` is ignored by git. It holds the per-post LinkedIn analytics (`unsolicited-advice-engagement.csv`) and the full collected file, including reposts of other authors' posts, so they never end up in the public repository.

## Spanish edition (`es/`)

`es/` is a second Jupyter Book with the same folder structure and file names as the English book, translated into Latin American Spanish. It's published at `/es/` and each edition links to the other from the banner at the top of every page.

- The Spanish pages are maintained by hand; `tools/build_book.py` doesn't touch them. When you add or change an English post, add or update the matching file under `es/` and its entry in `es/_toc.yml`.
- `tools/split_bundle.py` writes a batch of translated pages from one text file (sections start with `=== FILE: path ===`). It adds the Spanish "Publicado en LinkedIn el …" date line from the English page automatically.
- `es/_static` is a link to `_static`, so both editions share the same styling.
- Build locally with `.venv/bin/jupyter-book build es`.
