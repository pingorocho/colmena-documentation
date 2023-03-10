# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Colmena'
copyright = '2022, colmena.media'
author = 'Colmena Team'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static/']
html_logo = 'colmena-logo.svg'
html_show_sourcelink = True
html_favicon = "IconColmena_color.svg"
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}



# -- Options for EPUB output
epub_show_urls = 'footnote'
