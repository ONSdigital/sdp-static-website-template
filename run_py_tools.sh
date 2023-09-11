#!/bin/sh

CMDS=(
    "pylint freeze.py static_website_builder" 
    "flake8 ." 
    "isort --check-only ."
    "black --check --diff freeze.py static_website_builder" 
    "bandit -r freeze.py static_website_builder"
)

for i in "${CMDS[@]}"
do 
    if $i
    then
        echo "$i command successfully executed"
    else
        echo "$i command failed to execute or display errors that needs to be corrected"
    fi
done
