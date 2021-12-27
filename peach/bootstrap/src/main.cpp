#include "main.h"

// Definition field
namespace Peach{
    bool PEACH_BOOTSTRAP_DEBUG_MODE = false;
    std::string PEACH_VER = "v0.0.0";
    std::string PBTP_PACKAGE_VER = "v0.0";
    std::string PBTP_HOU_VERSION = "v0.0";
    std::string PBTP_BLN_VERSION = "v0.0";
    std::string init_script_command = "";
    std::string init_script_type = "";
}

void appendArg(std::string& line, const std::string arg)
{
    line += " " + arg;
}

void appendFlaggedArg(std::string& line, const std::string flag, const std::string arg)
{
    line += " " + flag + "=" + arg;
}


void configurations()
{
    #ifdef _WIN32
        PrintMsg("System: Running on Win32 system");
    #endif
    
    #ifdef PEACH_BOOTSTRAP_APP_VERSION
        Peach::PBTP_PACKAGE_VER = std::string(TOSTRING(PEACH_BOOTSTRAP_APP_VERSION));
        Peach::PBTP_PACKAGE_VER.erase(0,1);
        Peach::PBTP_PACKAGE_VER.pop_back();
        Peach::PBTP_BLN_VERSION = Peach::PBTP_PACKAGE_VER;
        Peach::PBTP_HOU_VERSION = Peach::PBTP_PACKAGE_VER;
        
    #endif

    #ifdef PEACH_BOOTSTRAP_BLN_VERSION
        Peach::PBTP_BLN_VERSION += "." + std::string(TOSTRING(PEACH_BOOTSTRAP_BLN_VERSION));
    #endif

    #ifdef PEACH_BOOTSTRAP_HOU_VERSION
        Peach::PBTP_HOU_VERSION += "." + std::string(TOSTRING(PEACH_BOOTSTRAP_HOU_VERSION));
    #endif

    #ifdef PEACH_VERSION
        Peach::PEACH_VER = std::string(TOSTRING(PEACH_VERSION));
        Peach::PEACH_VER.erase(0,1);
        Peach::PEACH_VER.pop_back();
    #endif
}

int main(int argc, char** argv){
    
    configurations();
    // argument processing
    if(argc > 1){
        for(size_t i = 1; i < argc; ++i){
            std::string arg = argv[i];
            if( !ArgHandling(arg, dcc) ) { return 1; }
        }
    }

    // DCC Type
    static std::string dccType;

    // Init:
    PrintPackageMsg();
    switch (dcc)
    {
    case Type::HOUDINI:
        PrintHouVer(); // Houdini
        dccType= "houdini";
        break;
    case Type::BLENDER:
        PrintBlnVer(); // Blender
        dccType= "blender";
    default:
        break;
    }
    
    // Get Dcc Path
    std::string dccpath = RunConfig(dcc);

    // Run Dcc Shell scripts
    if(!dccpath.empty())
    {   
        PrintMsg("OPEN...");

        // Compile the shell command to pass to .sh script
        std::string shell_cmd; 
        appendArg(shell_cmd, Peach::init_script_command);
        appendFlaggedArg(shell_cmd, "-e", dccpath);
        appendFlaggedArg(shell_cmd, "-t", dccType);

        if(Peach::PEACH_BOOTSTRAP_DEBUG_MODE){
            appendArg(shell_cmd, "-d");
            PrintMsg(shell_cmd.c_str());
        }

        return system(shell_cmd.c_str());
    }
    return 0;
}