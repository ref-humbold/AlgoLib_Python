#! /bin/sh

TEST_DIR="tests"
RED="\033[1;31m"
BLUE="\033[1;34m"
NORMAL="\033[0m"

cd $(dirname "$0")
echo

if [ ! -d "$TEST_DIR" ]
then
    echo "${RED}Test directory not found.${NORMAL}"
    exit 1
fi

echo "${BLUE}Running PyUnit tests with Nose2:${NORMAL}"
nose2 $TEST_DIR
echo "${BLUE}Generating XML report...${NORMAL}"
