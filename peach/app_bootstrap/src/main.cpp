#include "main.h"

static std::string dccTypeArg;
namespace Peach{
    bool __DEBUG = false;
}

void appendArg(std::string& line, const std::string arg)
{
    line += " " + arg;
}

void appendFlaggedArg(std::string& line, const std::string flag, const std::string arg)
{
    line += " " + flag + "=" + arg;
}


int main(int argc, char** argv){
    // argument processing
    if(argc > 1){
        for(size_t i = 1; i < argc; ++i){
            std::string arg = argv[i];
            if( !ArgHandling(arg, dcc) ) { return 1; }
        }
    }

    #ifdef _WIN32
        PrintMsg("System: Running on Win32 system");
    #endif
    
    // Init:
    PrintPackageMsg();
    switch (dcc)
    {
    case Type::HOUDINI:
        PrintHouVer(); // Houdini
        system("ECHO \"Running Houdini\"");
        dccTypeArg= "houdini";
        break;
    case Type::BLENDER:
        PrintBlnVer(); // Blender
        system("ECHO \"Running Blender\"");
        dccTypeArg= "blender";
    default:
        break;
    }
    
    // Get Dcc Path
    std::string dccpath = RunConfig(dcc);

    // Run Dcc Shell scripts
    if(dccpath != "missing")
    {   
        PrintMsg("OPEN...");
        // Shell Script
        std::string startup_shell(STARTUP_INIT_SHELLPATH);
        #ifdef _WIN32
            ReplaceForeslash(startup_shell);
        #endif

        // Compile the shell command to pass to .sh script
        std::string shell_cmd; 
        appendArg(shell_cmd, startup_shell);
        appendFlaggedArg(shell_cmd, "-e", dccpath);
        appendFlaggedArg(shell_cmd, "-t", dccTypeArg);
        if(Peach::__DEBUG){
            appendArg(shell_cmd, "-d");
        }
        return system(shell_cmd.c_str());
    }
    return 0;
}