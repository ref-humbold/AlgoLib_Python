#! /bin/bash

pushd $(dirname "$0")

mkdir -p build
sphinx-build -b html source build
sphinx-apidoc -f -d 1 -M -o source/ ../algolib/
make html

popd
