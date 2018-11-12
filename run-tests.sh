#! /bin/sh

TEST_DIR="tests"
NOSE2_OUTPUT_DIR="nose2_results"
BOLD_BLUE="\033[1;34m"
BOLD_RED="\033[1;31m"
NORMAL="\033[0m"

cd $(dirname $0)
echo ""

if test ! -d $TEST_DIR
then
    echo "${BOLD_RED}Test directory not found.${NORMAL}"
    exit 1
fi

echo "${BOLD_BLUE}Running PyUnit tests with Nose2:${NORMAL}"
nose2 $TEST_DIR
echo "${BOLD_BLUE}Moving XML report to output directory...${NORMAL}"
rm -fr $NOSE2_OUTPUT_DIR && mkdir $NOSE2_OUTPUT_DIR && mv nose2-junit.xml $NOSE2_OUTPUT_DIR
echo ""
