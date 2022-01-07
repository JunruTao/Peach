#!/bin/sh

timestamp=`date "+%Y%m%d_%H_%M_%S"`
folder="PeachBackup_$timestamp"
# mkdir "./$folder"

cp -r "/e/dev/peach_dev" "."
mv "./peach_dev" "./$folder"

rm -rf "./$folder/.git"
rm -rf "./$folder/peach/.build"

echo "create zip"
zip -r "$folder.zip" "./$folder"
rm -rf "./$folder"