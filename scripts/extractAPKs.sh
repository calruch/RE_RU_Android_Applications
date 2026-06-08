#!/bin/bash

cat scripts/textLists/CalsArt.txt

# Pulling the apps off the phone section
adb shell pm list packages -f | grep "package:/data" > scripts/textLists/apklist.txt
ls pulledApks > scripts/textLists/installedApks.txt
python3 scripts/APKparser.py > scripts/textLists/apklistParsed.txt
while read -r line; do
    APKpath=$(echo "$line" | awk '{print $1}')
    APKname=$(echo "$line" | awk '{print $2}')
    echo "Installing :$APKname"
    adb pull "$APKpath" "./pulledApks/$APKname.apk"
done < scripts/textLists/apklistParsed.txt

# Unpacking all of the APKs
ls pulledApks > scripts/textLists/installedApks.txt
while read -r line; do 
    curAPK=$(echo "pulledApks/$line")
    echo "Unpacking $curAPK"
    ./scripts/pullAPK.sh $curAPK
done < scripts/textLists/installedApks.txt



