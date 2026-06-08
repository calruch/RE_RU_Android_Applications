#! /usr/bin/env python3

import sys


def tracker(apkResults, apk, file):
    fileMap = {
        'miscF.txt': 0,
        'cellularF.txt': 1,
        'deviceF.txt': 2,
        'proxyF.txt': 3,
        'vpnF.txt': 4,
        'wifiF.txt': 5
    }

    # Create a new entry for the apk if it doesn't exist
    if apk not in apkResults:
        apkResults[apk] = [0,0,0,0,0,0]

    # Increment the matching file type for the apk
    if file in fileMap:
        index = fileMap[file]
        apkResults[apk][index] += 1
        
def printResults(apkResults):
    for apk, results in apkResults.items():
        print("---------------------------------")
        print(f"|APK: {apk}:\t")
        print("|===============================|")
        print(f"|Misc matches: {results[0]}\t\t|\n|Cellular matches: {results[1]}\t\t|\n|Device matches: {results[2]}\t\t|\n|Proxy matches: {results[3]}\t\t|\n|VPN matches: {results[4]}\t\t\t|\n|WiFi matches: {results[5]}\t\t|")
        print("---------------------------------")
def main():

    if len(sys.argv) > 1:
        if sys.argv[1] == "v":
            verbose = True
        else:
            verbose = False
    else:
        verbose = False
    
    # Open the fingerprint file and read it into a variable
    with open('scripts/textLists/FingerPrint.txt', 'r') as f:
        file = f.read()
    
    results = {}
    apkList = set()
    apkResults = {}
    sTctr = 0
    fileCtr = 0
    curFile = 0
    curST = 0


    for line in file.splitlines():
        # Strip whitespace and skip empty lines
        line = line.strip()
        if line == "": continue

        # Capture the file names and search terms
        if line[0] == '|':
            line = line[1:]

            # Get the file names
            if line.endswith('.txt'):
                fileCtr += 1
                curST = -1
                curFile += 1

                if verbose: print(f"File {fileCtr}: {line}")

                results[curFile] = {"file": line, "searchTerms": []}
            # Get the search terms for the file
            else:
                curST += 1
                if '!<>!' in line:
                    sTctr += 1

                    # Split the custom delimiter for verbose output
                    splitLine = line.split('!<>!')

                    if verbose: print(f"    Search Term a: {splitLine[0]}")
                    if verbose: print(f"    Search Term b: {splitLine[1]}")

                    results[curFile]["searchTerms"].append({"term": line, "results": []})
                else:
                    if verbose: print(f"    Search Term: {line}")
                    results[curFile]["searchTerms"].append({"term": line, "results": []})

        # Get the apk results for the search terms
        else:
            if verbose: print(f"        Result: {line}")
            results[curFile]["searchTerms"][curST]["results"].append(line)
            apkList.add(line.split(':')[0])

    apkList = list(apkList)

    for apk in apkList:
        for file in results:
            for searchTerm in results[file]["searchTerms"]:
                for result in searchTerm["results"]:
                    if apk == result.split(':')[0]:
                        tracker(apkResults, apk, results[file]["file"])
    

    printResults(apkResults)
    #print(apkResults)  
                    
if __name__ == "__main__":
    main()

