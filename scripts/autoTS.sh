#!/bin/bash
#
# The main goal of this script is to utilize the APKtermSearch.sh script to search through all of the fingerprint strings to see if the smali code contains any instances

# This function will print if verbose is enabled
verboseMessage() {
	if [ "$2" -eq 1 ]; then
		echo "$1"
	fi	
}

# Custom function to print to the Finger Print text file
printFile() {
	echo "|$1" >> scripts/textLists/FingerPrint.txt
}

clear

verbose=0
if [ "$#" -eq 1 ]; then
	verbose=1
	cat scripts/textLists/CalsArt.txt
fi	

# Get all of the finger print files
ls fingerprint > scripts/textLists/fingerprintFiles.txt

# Clear the fingerprint file 
> scripts/textLists/FingerPrint.txt

# Iterate through all of the fingerprint files
while read -r fingerprintFile; do
	
	# Print the File name to the Fingerprint.txt
	printFile "$fingerprintFile"	
	verboseMessage "Searching for fingerprint file: $fingerprintFile" "$verbose"

	# Read current fingerprint file and perform the term search on each
	# Then save the result to a text file for analysis later in script	
	while read -r line; do 
		verboseMessage "Searching for term: $line" "$verbose"
		printFile "$line"
		if [[ $line == *"!<>!"* ]]; then
			./scripts/APKtermSearch.sh . "$line" 5 < /dev/null
			
		else
		# Perform the search on the APK list - Concats result onto text file
			./scripts/APKtermSearch.sh . "$line" 4 < /dev/null
		fi
		cat scripts/textLists/rgWList.txt >> scripts/textLists/FingerPrint.txt
	done < "fingerprint/$fingerprintFile"
done < scripts/textLists/fingerprintFiles.txt 


cat scripts/textLists/FingerPrint.txt


