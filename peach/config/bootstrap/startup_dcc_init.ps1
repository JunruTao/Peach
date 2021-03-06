# ---------------------------------------------------------------------
# Copyright (c) 2022 Digital Peach Studio - Junru Tao
# This code is licensed under MIT license (see LICENSE.txt for details)
#                             *   *   *   *
# - Digital Peach Studio
# - Authors: Junru Tao
# - Contact: <junrtao.uk@gmail.com | junrutao@qq.com>
# - Website: digital-peach.company.site
# - Instagram: @digital.peach.studio
#
# ---------------------------------------------------------------------

write-host "[Peach Start-Up] Running PowerShell Script"

# [ INIT SCRIPTS LOCATIONS ]
$Init_Script_Houdini="config/scripts/houdini_init.py"
$Init_Script_Blender="config/scripts/blender_init.py"


# [ DEFAULT ARGUMENT FIELD ]
$mode_debug = $false
$dcc_file_path=""
$dcc_type=""
$dcc_arguments=@()

# >>>[ PROCESS ARGUMENTS ]
for ( $i = 0; $i -lt $args.count; $i++ ) 
{
    $arg = "$($args[$i])"

    if ( ($arg.StartsWith('-d')) -or ($arg.StartsWith('--debug')) )
    {
        # [-d Flag: if Debug mode ]
        $mode_debug = $true
        write-host "[ Startup - Debug ]: $mode_debug"
    }
    elseif ( ($arg.StartsWith('-e=')) -or ($arg.StartsWith('--executable')) )
    {
        # [-e Input: DCC executable file path ]
        $dcc_file_path = $arg.split("=")[1]
        write-host "[ Startup - DCC Path ]: $dcc_file_path"
    }
    elseif ( ($arg.StartsWith('-t=')) -or ($arg.StartsWith('--dcc_type')) )
    {
        # [ -t Input: DCC Type Identifier ]
        $dcc_type = $arg.split("=")[1]
        write-host "[ Startup - DCC-ID Type Argument ]: $dcc_type"
    }
} 


if($mode_debug)
{
    Pause
}

# [ DEFINE INIT ARGUMENTS HERE ]
if ( $dcc_type -eq 'blender' )
{
    $dcc_arguments=@('-con', '--debug-python', '--python',"`"$Init_Script_Blender`"")
    # [ Combine the dcc executable and input arguments ]
    $startup_shell_cmd = $dcc_arguments -join ' '
    write-host "[ Startip - DCC Run dcc_file_path] $startup_shell_cmd"
    Start-Process -NoNewWindow -FilePath $dcc_file_path -ArgumentList $dcc_arguments
}
elseif ( $dcc_type -eq 'houdini' )
{
    $dcc_arguments=@("-background", "`"$Init_Script_Houdini`"")
    $startup_shell_cmd = $dcc_arguments -join ' '
    write-host "[ Startip - DCC Run dcc_file_path] $startup_shell_cmd"
    Start-Process -Wait -NoNewWindow -FilePath $dcc_file_path -ArgumentList $dcc_arguments
}