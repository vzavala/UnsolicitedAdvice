"""Write the files contained in a translation bundle into the Spanish edition.

A bundle is a text file of sections that each start with a line
'=== FILE: relative/path.md ===', followed by that file's contents.
For post pages, if the translated text has no "Publicado en LinkedIn" line,
one is added under the title, using the date and link from the English page.

Usage: python tools/split_bundle.py bundle.md es/
"""
import os, re, sys

MESES = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
MONTHS = "January February March April May June July August September October November December".split()

def spanish_date_line(english_path):
    s = open(english_path, encoding="utf-8").read()
    m = re.search(r"^> Posted on LinkedIn on \[(\w+) (\d+), (\d+)\]\((\S+)\)\.", s, re.M)
    if not m:
        return None
    mes = MESES[MONTHS.index(m.group(1))]
    return f"> Publicado en LinkedIn el [{int(m.group(2))} de {mes} de {m.group(3)}]({m.group(4)})."

bundle, out = sys.argv[1], sys.argv[2]
text = open(bundle, encoding="utf-8").read()
parts = re.split(r"(?m)^=== FILE: (.+?) ===\n", text)
assert parts[0].strip() == "", "bundle must start with a FILE marker"
for path, body in zip(parts[1::2], parts[2::2]):
    path = path.strip()
    body = body.strip() + "\n"
    if "Publicado en LinkedIn" not in body and os.path.exists(path):
        line = spanish_date_line(path)
        if line:
            title, _, rest = body.partition("\n")
            body = f"{title}\n\n{line}\n\n{rest.lstrip()}"
    dest = os.path.join(out, path)
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    open(dest, "w", encoding="utf-8").write(body)
    print(dest)
