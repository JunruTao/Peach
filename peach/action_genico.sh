#!/bin/sh

# Note: New Actions moved to ${peach for easier access from commandlines} 

# [ DEBUG ] functions here:
function pause(){
    read -s -n 1 -p "[Done] Press any key to continue . . ."
    echo ""
}

# run scripts
python ./icons/scripts/genico.py

# pause