import os
import sys

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

project = 'Generative AI Python'
copyright = '2024, Your Name'
extensions = [
    'sphinx.ext.coverage',
    'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

source_suffix = '.md'
master_doc = 'index'  # Set the homepage
# Configure autodoc to use markdown

# Configure HTML output
html_theme = 'pydata_sphinx_theme'  # Choose a theme (optional)
# html_static_path = ['_static']  # Add a static folder if needed


exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']
# Configure Read the Docs theme (if using)
html_theme_options = {
    'collapse_navigation': False,  # Show navigation by default
}




def setup(app):
    pass
