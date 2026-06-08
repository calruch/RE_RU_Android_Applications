#! /usr/bin/env python3

def main():
    # Open the fingerprint file and read it into a variable
    with open('scripts/textLists/FingerPrint.txt', 'r') as f:
        file = f.read()
    
    # Create dictionary to hold the results
    results = {}

    