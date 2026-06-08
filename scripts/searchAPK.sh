#!/bin/bash
if [ "$#" -ne 1 ]; then 
	exit
fi

python3 scripts/resultsExtractor.py | grep -A 8 $1
