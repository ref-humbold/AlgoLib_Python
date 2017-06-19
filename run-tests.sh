#! /bin/bash

TEST_DIR="tests"
PYUNIT_OUTPUT_DIR="pyunit_results"

echo "Running Python tests:"
python3 -m xmlrunner discover $TEST_DIR
echo "Moving XML reports to output directory..."
rm -rf $PYUNIT_OUTPUT_DIR && mkdir $PYUNIT_OUTPUT_DIR && mv *.xml $PYUNIT_OUTPUT_DIR
