#ifndef __APPINFO_H__
#define __APPINFO_H__

#include "basetypes.h"
#include <iostream>
#include <string>

#define PBTP_PACKAGE_VER "v1.0.0"
#define PBTP_HOU_VERSION "1.0.0"
#define PBTP_BLN_VERSION "1.0.0"

static const char* HDAPP = "[ Peach Boostrap ] ";
static const char* HDHOU = "[ Peach Boostrap : Houdini ]";
static const char* HDBLD = "[ Peach Boostrap : Blender ]";
 
namespace Peach{
    extern bool __DEBUG;
}

inline void PrintPackageMsg()
{
    std::cout << "[ Peach Boostrap ] Init ... " << std::endl;
}

inline void PrintPackageVer()
{
    std::cout << "[ Peach Boostrap ] Version: " << PBTP_PACKAGE_VER << std::endl;
}

inline void PrintHouVer()
{
    std::cout << HDHOU << " Version: " << PBTP_HOU_VERSION << std::endl;
}

inline void PrintBlnVer()
{
    std::cout << HDBLD << " Version: " << PBTP_BLN_VERSION << std::endl;
}

inline void PrintMsg(const char* msg)
{
    std::cout << HDAPP << msg << std::endl;
}

inline void PrintHouMsg(const char* msg)
{
    std::cout << HDHOU << msg << std::endl;
}

inline void PrintBlnMsg(const char* msg)
{
    std::cout << HDBLD << msg << std::endl;
}



#define HELP_MSG "Print Help... \n\n \
[ Allowed Flags ]:\n \
-v | --version ..... Display current Bootstrap version\n \
-h | --help    ..... Display help message\n \
-d | --debug   ..... Set Debug Mode as True\n"

inline bool ArgHandling(std::string &arg, Type app=Type::HOUDINI)
{
    if( arg == "--version" || arg == "-v")
    {

        // [ Package Message ]
        PrintMsg("Print Version ... ");
        PrintPackageVer();

        // [ App Message ]
        switch (app)
        {
        case Type::HOUDINI:
            PrintHouVer();
            break;
        case Type::BLENDER:
            PrintBlnVer();
            break;
        case Type::MAYA:
            // currently None;
            break;
        default:
            break;
        }
    }
    else if(arg == "--help" || arg == "-h")
    {
        PrintMsg(HELP_MSG);
    }
    else if(arg == "--debug" || arg == "-d")
    {
        Peach::__DEBUG = true;
        PrintMsg("Debug=True");
        return true;
    }
    else
    {
        std::string msg = "Cannot Recognise the flag " + arg + ", please use --help or -h";
        PrintMsg(msg.c_str());
        return false;
    }
    return false;
}
#endif