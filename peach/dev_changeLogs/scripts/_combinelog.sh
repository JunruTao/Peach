#!/bin/sh

# note: this is a backup script. new script moved to ${peach}
# [ DEBUG ] functions here:
function pause(){
    read -s -n 1 -p "[Done] Press any key to continue . . ."
    echo ""
}

result=`python changelog_combine.py`
echo $result

#pause

code "$result"