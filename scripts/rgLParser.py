#!/usr/bin/env python3 
import sys
def main():
    rgFileR = 'scripts/textLists/rgList.txt'
    rgFileW = 'scripts/textLists/rgWList.txt'

    # Read the temporary input file
    with open(rgFileR, 'r') as f:
        file = f.read()
    
    # Create empty dictionary
    results = {}
    
    # Count the occurrences of each app and store it into a dictionary
    for app in file.splitlines():
        app = app.strip()
        if app in results:
            results[app] += 1
        else:
            results[app] = 1
    
    # Write all of the results to the output file
    with open(rgFileW, 'w') as f:
        for app, count in results.items():
            if len(sys.argv) > 1 and sys.argv[1] == "v": print(f"{app}: {count}")
            f.write(f"{app}: {count}\n")


if __name__ == "__main__":
    main()
