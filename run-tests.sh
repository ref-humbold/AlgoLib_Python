#! /bin/sh

TEST_DIR="tests"
PYUNIT_OUTPUT_DIR="pyunit_results"

if test ! -d $TEST_DIR
then
    echo "\033[0;31mTest directory not found.\033[0m"
    exit -1
fi

echo "\033[1;34mRunning PyUnit tests:\033[0m"
python3 -m xmlrunner discover $TEST_DIR
echo "\033[1;34mMoving XML reports to output directory...\033[0m"
rm -rf $PYUNIT_OUTPUT_DIR && mkdir $PYUNIT_OUTPUT_DIR && mv TEST-*.xml $PYUNIT_OUTPUT_DIR
