#!/bin/sh

echo "[Peach Start-Up] Running Bash Script"

# [ INIT SCRIPTS LOCATIONS ]
Init_Script_Houdini="config/scripts/houdini_init.py"
Init_Script_Blender="config/scripts/blender_init.py"

# [ DEFAULT ARGUMENT FIELD ]
mode_debug=0
dcc_file_path=""
dcc_type=""
dcc_arguments=""

# [ DEBUG ] define functions here:
function pause(){
    read -s -n 1 -p "[debug] Press any key to continue . . ."
    echo ""
}

# >>>[ PROCESS ARGUMENTS ]
for arg in "$@"
do
    case $arg in
        -d|--debug)
        # [-d Flag: if Debug mode ]
            echo "[ Startup - Debug ]: True"
            mode_debug=1
            echo "[ Startup - Debug Value ]: $mode_debug"
        ;;

        -e=*|--executable=*)
        # [-e Input: DCC executable file path ]
            dcc_file_path="${arg#*=}"
            echo "[ Startup - DCC Path ]: $dcc_file_path"
        ;;

        -t=*|--dcc_type=*)
        # [ -t Input: DCC Type Identifier ]
            dcc_type="${arg#*=}"
            echo "[ Startup - DCC-ID Type Argument ]: $dcc_type"
        ;;
    esac
done


# [ DEFINE INIT ARGUMENTS HERE ]
if [ $dcc_type == 'blender' ];
then
    dcc_arguments="-con --debug-python --python \"$Init_Script_Blender\""
elif [ $dcc_type == 'houdini' ];
then 
    dcc_arguments="-background \"$Init_Script_Houdini\""
fi

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

# [Note]: In the dev stage, Houdini will NOT start from vscode's powershell or cmds,
# as the working dir is limited to the vscode file scope. the solution is run the 
# bootstrap app from the folder(windows, .exe) or call the bootstrap from other shells.

# ////////////////////////////
if [ $mode_debug == 1 ];then
    # Give user some time to read the logs.
    pause
fi

