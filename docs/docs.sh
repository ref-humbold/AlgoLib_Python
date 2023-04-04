#! /bin/bash

DOCS=$(dirname "$0")

sphinx-apidoc -f -d 1 -o $DOCS/source $DOCS/../algolib
sphinx-build -b html $DOCS/source $DOCS/build
