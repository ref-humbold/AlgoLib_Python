#! /bin/sh

TEST_DIR="tests"
PYUNIT_OUTPUT_DIR="pyunit_results"
BOLD_BLUE="\033[1;34m"
BOLD_RED="\033[1;31m"
NORMAL="\033[0m"

echo ""

if test ! -d $TEST_DIR
then
    echo "${BOLD_RED}Test directory not found.${NORMAL}"
    exit -1
fi

echo "${BOLD_BLUE}Running PyUnit tests:${NORMAL}"
python3 -m xmlrunner discover -s $TEST_DIR -t .
echo "${BOLD_BLUE}Moving XML reports to output directory...${NORMAL}"
rm -rf $PYUNIT_OUTPUT_DIR && mkdir $PYUNIT_OUTPUT_DIR && mv TEST-*.xml $PYUNIT_OUTPUT_DIR
echo ""
