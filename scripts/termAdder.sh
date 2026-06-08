#!/bin/bash

# This script is used to add terms to the fingerprint files

vpnFile="fingerprint/vpnF.txt"
proxyFile="fingerprint/proxyF.txt"
wifiFile="fingerprint/wifiF.txt"
miscFile="fingerprint/miscF.txt"
cellularFile="fingerprint/cellularF.txt"
deviceFile="fingerprint/deviceF.txt"


check=1 

# This function will allow for multiple terms to be used for a single search
getTerm(){
    echo "Would you like to use two terms for this search? (1 for yes, 0 for no)"
    read useTwoTerms
    if [ $useTwoTerms -eq 1 ]; then
        echo "Press enter after typing the first term, then type the second term."
        read term
        read term2
        echo "$term!<>!$term2" >> $1
    else
        echo "Enter the term you would like to add:"
        read term
        echo "$term" >> $1
    fi
}


while [ $check -eq 1 ]; do
    echo "What type of term would you like to add?"
    echo "1. VPN"
    echo "2. Proxy"
    echo "3. Wifi"
    echo "4. Miscellaneous"
    echo "5. Cellular"
    echo "6. Device"
    echo "7. Exit"
    read type

    if [ $type -eq 1 ]; then
        echo "VPN term selected."
        getTerm $vpnFile
    elif [ $type -eq 2 ]; then
        echo "Proxy term selected."
        getTerm $proxyFile
    elif [ $type -eq 3 ]; then
        echo "Wifi term selected."
        getTerm $wifiFile
    elif [ $type -eq 4 ]; then
        echo "Miscellaneous term selected."
        getTerm $miscFile
    elif [ $type -eq 5 ]; then
        echo "Cellular term selected."
        getTerm $cellularFile
    elif [ $type -eq 6 ]; then
        echo "Device term selected."
        getTerm $deviceFile
    elif [ $type -eq 7 ]; then
        echo "Exiting."
        check=0
    else 
        echo "Invalid option, please try again."
    fi
    clear
done