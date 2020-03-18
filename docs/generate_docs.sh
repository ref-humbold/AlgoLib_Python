#! /bin/bash

pushd $(dirname "$0")

sphinx-apidoc -f -d 1 -M -o source/ ../algolib/
make html

popd
