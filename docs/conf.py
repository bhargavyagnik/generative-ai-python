import os
import sys

project = 'Generative AI Python'
copyright = '2024, Google-Gemini'
extensions = [
    'sphinx.ext.coverage',
    'myst_parser',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]


myst_url_schemes = ["http", "https", "mailto"]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
    "replacements",
    "smartquotes",
    "tasklist",
    "substitution"
]

source_suffix = ['.md','.ipynb']
master_doc = 'index'  # Set the homepage

# Configure HTML output
html_theme = 'pydata_sphinx_theme'  # Choose a theme (optional)
# html_static_path = ['_static']  # Add a static folder if needed

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']

html_theme_options = {
    'collapse_navigation': False,  
}



def setup(app):
    app.connect('source-read', process_relative_links)

def process_relative_links(app, docname, source):
    source[0] = source[0].replace(
        '../google/generativeai/',
        '/api/google/generativeai/'
    )

