#!/bin/sh
echo "[Peach Start-Up] Dev Houdini Init"

# [ INIT SCRIPTS LOCATIONS ]
Init_Script_Houdini="config/scripts/dev_houdini_init.py"

# [ DEFAULT ARGUMENT FIELD ]
mode_debug=0
dcc_file_path="/c/Program\ Files/Side\ Effects\ Software/Houdini\ 19.0.455/bin/houdini.exe"

# [ DEBUG ] define functions here:
function pause(){
    read -s -n 1 -p "[debug] Press any key to continue . . ."
    echo ""
}

dcc_arguments="-background \"$Init_Script_Houdini\""

# [ Combine the dcc executable and input arguments ]
startup_shell_cmd="$dcc_file_path $dcc_arguments"
echo "[ Startip - DCC Run dcc_file_path] $startup_shell_cmd"

# ////////////////////////////
if [ $mode_debug == 1 ];then
    # Give user some time to read the logs.
    pause
fi

# >>>
# [ RUN SCRIPT]
eval "$startup_shell_cmd"

# ////////////////////////////
if [ $mode_debug == 1 ];then
    # Give user some time to read the logs.
    pause
fi

