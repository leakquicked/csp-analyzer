![Python checks](https://github.com/leakquicked/csp-analyzer/actions/workflows/python-checks.yml/badge.svg)

# CSP Analyzer

Inspect a copied Content-Security-Policy value for broad directives.

## Requirements
Python 3.10+, standard library only.

## Usage
`python csp_analyzer.py --help`

Supply a local text export or copied response headers. This tool is passive: it does not contact websites or alter configuration. Findings are advisory and require review in context.

## Tests
`python -m unittest discover -s tests -v`
