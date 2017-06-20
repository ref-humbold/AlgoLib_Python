#! /bin/sh

TEST_DIR="tests"
PYUNIT_OUTPUT_DIR="pyunit_results"

if test ! -d $TEST_DIR
then
    echo "Test directory not found."
    exit -1
fi

echo "Running Python tests:"
python3 -m xmlrunner discover $TEST_DIR
echo "Moving XML reports to output directory..."
rm -rf $PYUNIT_OUTPUT_DIR && mkdir $PYUNIT_OUTPUT_DIR && mv TEST-*.xml $PYUNIT_OUTPUT_DIR
