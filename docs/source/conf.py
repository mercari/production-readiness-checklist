"""Sphinx configuration."""
import datetime
import pathlib
import re
import sys
from typing import Match

import emoji
from sphinx.application import Sphinx

# -- Project information -----------------------------------------------------
PACKAGE_NAME = "production-readiness-checklist"

# -- Project information -----------------------------------------------------
project = "Mercari Production Readiness Checklist"
author = "Mercari Inc."
copyright = (  # pylint: disable=redefined-builtin
    f"{datetime.datetime.now().year}, {author}"
)
version = release = "0.0.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",  # MyST .md parsing (https://myst-parser.readthedocs.io/en/latest/index.html)
    "sphinx.ext.intersphinx",  # Link to other projects’ documentation (https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
    "sphinx_rtd_theme",  # Sphinx theme used on Read The Docs (https://github.com/readthedocs/sphinx_rtd_theme)
]

# Sphinx configs
html_theme = "sphinx_rtd_theme"
# Remove 'view source code' from top of page (for html, not python)
html_show_sourcelink = False

# -- Extension configurations ---------------------------------------------------

def convert_emoji_shortcodes(app: Sphinx, exception: Exception) -> None:
    """Convert emoji shortcodes in HTML files to corresponding emoji characters

    Running separately to support Read The Docs builds.
    Adapted from: https://bitbucket.org/lbesson/bin/src/master/emojize.py
    """

    def emojize_match(match: Match) -> str:
        """Convert emoji shortcodes in match to corresponding emoji characters"""
        return emoji.emojize(match.group(), use_aliases=True, variant="emoji_type")

    def emojize_all(text: str) -> str:
        """Convert all emoji shortcodes in text to corresponding emoji characters"""
        return re.sub(r":([a-z0-9_-]+):", emojize_match, text)

    if exception is None:
        for html_file in pathlib.Path(app.outdir).rglob("*.html"):
            html_file.write_text(emojize_all(html_file.read_text()))


def setup(app: Sphinx) -> None:
    """Connects bespoke emoji shortcode conversion functions"""
    app.connect("build-finished", convert_emoji_shortcodes)


# -- External mapping --------------------------------------------------------
python_version = ".".join(map(str, sys.version_info[0:2]))
intersphinx_mapping = {
    "sphinx": ("http://www.sphinx-doc.org/en/stable", None),
    "python": ("https://docs.python.org/" + python_version, None),
}
