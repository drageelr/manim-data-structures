# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from pathlib import Path

import manim_data_structures

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Manim Data Structures"
copyright = "2022, Hammad Nasir (aka DrageelR)"
author = "Hammad Nasir (aka DrageelR)"
release = manim_data_structures.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "manim.utils.docbuild.manim_directive",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

templates_path = ["_templates"]
exclude_patterns = []

# displays shorter function names that are documented via autodoc - sphinx.ext.autosummary
add_module_names = False

# displays type hint defaults - sphinx_autodoc_typehints
typehints_defaults = "comma"

# allows external documentation to be referred - sphinx.ext.intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "manim": ("https://docs.manim.community/en/stable/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_favicon = str(Path("_static/favicon.ico"))
html_static_path = ["_static"]
html_title = f"Manim Data Structures v{manim_data_structures.__version__}"
html_css_files = ["custom.css"]

html_theme_options = {
    "source_repository": "https://github.com/ManimCommunity/manim/",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "top_of_page_button": None,
    "light_logo": "logo-color-no-bg.svg",
    "dark_logo": "logo-white-no-bg.svg",
}
