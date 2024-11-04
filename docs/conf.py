import os
import sys

import sphinx.ext.pygments
sphinx.ext.pygments.lexer_mapping['console'] = 'posix-terminal'

project = 'Generative AI Python'
copyright = '2024, Your Name'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'myst_parser',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

source_suffix = '.md'
master_doc = 'index'  # Set the homepage

extensions = ['myst_nb']
# Configure autodoc to use markdown
autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']
autodoc_member_order = 'bysource'

# Configure markdown processing
napoleon_use_param = True  # Enable napoleon for docstrings

# Configure HTML output
html_theme = 'pydata_sphinx_theme'  # Choose a theme (optional)
html_static_path = ['_static']  # Add a static folder if needed
html_sidebars = {
    '**': [
        'relations.html',  # Include related pages
        'sources.html',  # Include source code links
        'search.html',    # Include search box
    ]
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']
# Configure Read the Docs theme (if using)
html_theme_options = {
    'collapse_navigation': False,  # Show navigation by default
}

# MyST Markdown parser settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
    "replacements",
    "smartquotes",
    "tasklist",
]


def setup(app):
    pass
