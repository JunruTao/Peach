#!/bin/sh
echo "[Peach Start-Up] Dev Blender Init"


# [ INIT SCRIPTS LOCATIONS ]
Init_Script_Blender="blender_init.py"

# [ DEFAULT ARGUMENT FIELD ]
mode_debug=0
dcc_file_path="/c/Program\ Files/Blender\ Foundation/Blender\ 3.0/blender-launcher.exe"

# [ DEBUG ] define functions here:
function pause(){
    read -s -n 1 -p "[debug] Press any key to continue . . ."
    echo ""
}

dcc_arguments="-con --debug-python --python \"$Init_Script_Blender\""

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

