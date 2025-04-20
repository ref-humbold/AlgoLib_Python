#! /bin/bash

DOCS=$(dirname "$0")

find source -name '*.rst' -type f ! -name 'index.rst' -exec rm {} +
sphinx-apidoc -f -e -d 2 -o $DOCS/source $DOCS/../algolib
sphinx-build -b html $DOCS/source $DOCS/build/docs -a
