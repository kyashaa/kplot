# scripts/gen_api.py
from __future__ import annotations

from pathlib import Path
import importlib
import pkgutil

import mkdocs_gen_files

PKG = "kplot"

def iter_modules(pkg_name: str) -> list[str]:
    pkg = importlib.import_module(pkg_name)
    names = []
    for m in pkgutil.walk_packages(pkg.__path__, prefix=pkg.__name__ + "."):
        names.append(m.name)
    return sorted(set(names))

nav = mkdocs_gen_files.Nav()

# 入口（Reference -> API の表紙）も生成しておくと便利
with mkdocs_gen_files.open("reference/api/index.md", "w") as f:
    f.write("# API Reference\n\n")
    f.write("This section is generated automatically.\n")

nav["API Reference"] = "reference/api/index.md"

for mod in iter_modules(PKG):
    parts = mod.split(".")  # e.g. ["kplot", "core"]
    doc_path = Path("reference/api", *parts).with_suffix(".md")  # reference/api/kplot/core.md

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(doc_path, "w") as f:
        f.write(f"# `{mod}`\n\n")
        f.write(f"::: {mod}\n")

# 左ナビ用の SUMMARY を生成
with mkdocs_gen_files.open("reference/api/SUMMARY.md", "w") as f:
    f.writelines(nav.build_literate_nav())
