#!/bin/sh


# Note: New Actions moved to ${peach for easier access from commandlines} 

# [ DEBUG ] functions here:
function pause(){
    read -s -n 1 -p "[Done] Press any key to continue . . ."
    echo ""
}

result=`python ./dev_changeLogs/scripts/changelog_combine.py`
echo $result

#pause

code "$result"