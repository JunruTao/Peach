#!/bin/sh


# Note: New Actions moved to ${peach for easier access from commandlines} 

debug=0
# [ DEBUG ] functions here:
function pause(){
    read -s -n 1 -p "[Done] Press any key to continue . . ."
    echo ""
}



#pause
if [ $debug != 1 ]
then
    result=`python ./dev_changeLogs/scripts/changelog_combine.py`
    echo $result
    code "$result"
else
    python ./dev_changeLogs/scripts/changelog_combine.py
fi