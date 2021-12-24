#!/bin/sh


# [ DEBUG ] functions here:
function pause(){
    read -s -n 1 -p "[Done] Press any key to continue . . ."
    echo ""
}

# run scripts
python ./scripts/genico.py
pause