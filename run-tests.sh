#! /bin/sh

TEST_DIR="tests"
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
echo "${BOLD_BLUE}Generating XML report...${NORMAL}"
echo ""
