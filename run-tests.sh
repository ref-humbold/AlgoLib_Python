#! /bin/sh

TEST_DIR="tests"
RED="\033[1;31m"
CYAN="\033[1;36m"
NORMAL="\033[0m"

cd $(dirname "$0")
echo

if [ ! -d "$TEST_DIR" ]
then
    echo "${RED}Test directory not found.${NORMAL}"
    exit 1
fi

echo "${CYAN}Running PyUnit tests with Nose2:${NORMAL}"
nose2 $TEST_DIR
echo "${CYAN}Generating XML report...${NORMAL}"
