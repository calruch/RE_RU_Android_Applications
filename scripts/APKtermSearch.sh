#!/bin/bash
# This program is used to find all of the smali files in an extracted apk, that have the string matching the third argument.
# A more efficient version of this could be made but ripgrep made for easy fingerprinting 
#
# Barely any error checking - enter the correct directory or it will run this over all of the extracted apk directories

# Make sure there is 3 args 
# $1 = extracted apk directory to search
# $2 = search term
# $3 = option
# - 1 = get all file names - only smali files
# - 2 = get all file names
# - 3 = get all of the text (normal ripgrep style)
# - 4 = Use custom chain of commands for script
# 

# Ripgrep flags
# -F = fixed string search, not using regex to search for strings
# -l = Get the File name that the matching string was in (option 3 does have this)

# Sed command
# 's|/.*||' - This will Chop everything off after '/', so I can get the name of the APK
# 's#!<>!.*##' - This will get the first part of my custom delimiter
# 's#^.*!<>!##' - This will get the second part of my custom delimiter

# Error handling if there isn't 3 arguments
if [ $# -ne 3 ]; then
	echo "Arg 1: Directory to search (use . to search everything)"
	echo "Arg 2: Search term to look for"
	echo "Arg 3: Option to use (Default is 1)"
	echo "Arg 4: get APKs that contain the search term"
	exit
fi	


# This will get you into the pulled APKs directory
cd $(echo "pulledApks/$1")

# This part is for the actual ripgrep portion
if [ $3 -eq '1' ]; then 	
	rg -l -F $2 | grep ".smali"
elif [ $3 -eq '2' ]; then
	rg -l -F $2 
elif [ $3 -eq '3' ]; then
	rg $2 -F
elif [ $3 -eq '4' ]; then
	touch ../scripts/textLists/rgList.txt
	rg -l -F $2 | grep ".smali" | sed 's|/.*||' > ../scripts/textLists/rgList.txt
	cd ..
	python3 scripts/rgLParser.py
elif [ $3 -eq '5' ]; then
	string1=$(echo $2 | sed 's#!<>!.*##')
	string2=$(echo $2 | sed 's#^.*!<>!##')
	# This is a custom chain of ripgrep commands to search for two terms.
	rg $string1 -F | xargs rg -l -F $string2 | sed 's|/.*||' > ../scripts/textLists/rgList.txt
	cd ..
	python3 scripts/rgLParser.py

fi


