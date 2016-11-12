#!/bin/bash
trap '. ~/.termoji/main.sh' DEBUG
export PS1="\$(python ~/.termoji/termoji.py 2>&1)"