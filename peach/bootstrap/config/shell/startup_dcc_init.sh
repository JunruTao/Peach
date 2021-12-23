#!/bin/sh

Init_Script_Houdini="config/scripts/houdini_init.py"
Init_Script_Blender="config/scripts/blender_init.py"

# [ DEFAULT ARGUMENT FIELD ]

DEBUG=0
dcc_file_path=""
dcc_type=""
dcc_arguments=""

# [ DEBUG ] functions here:
function pause(){
    read -s -n 1 -p "[debug] Press any key to continue . . ."
    echo ""
}

for arg in "$@"
do
    case $arg in
        -d|--debug)
        # [-d Flag: if Debug mode ]
            echo "[ Startup - Debug ]: True"
            DEBUG=1
            echo "[ Startup - Debug Value ]: $DEBUG"
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


if [ $DEBUG == 1 ];then
    pause
fi

# [ RUN SCRIPT]
eval "$startup_shell_cmd"

if [ $DEBUG == 1 ];then
    pause
fi


