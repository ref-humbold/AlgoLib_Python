#! /bin/sh

TEST_DIR="tests"
NOSETEST_OUTPUT_DIR="nosetest_results"
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

echo "${BOLD_BLUE}Running PyUnit tests with Nose:${NORMAL}"
nosetests --with-xunit $TEST_DIR
echo "${BOLD_BLUE}Moving XML report to output directory...${NORMAL}"
rm -rf $NOSETEST_OUTPUT_DIR && mkdir $NOSETEST_OUTPUT_DIR && mv nosetests.xml $NOSETEST_OUTPUT_DIR
echo ""
