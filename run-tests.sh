#! /bin/sh

TEST_DIR="tests"
NORMAL="\033[00m"
BOLD_BLUE="\033[01;34m"
BOLD_RED="\033[01;31m"

cd $(dirname $0)
echo ""

[ ! -d $TEST_DIR ] && echo -e "${BOLD_RED}Test directory not found.${NORMAL}" && exit 1

echo -e "${BOLD_BLUE}Running PyUnit tests with Nose2:${NORMAL}"
nose2 $TEST_DIR
echo -e"${BOLD_BLUE}Generating XML report...${NORMAL}\n"
