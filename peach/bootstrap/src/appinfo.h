#ifndef __APPINFO_H__
#define __APPINFO_H__
#include <iostream>
#include <string>

// Define a enum for type switching
enum class Type{
    HOUDINI,
    BLENDER,
    MAYA
};


/* [ Preprocessor ToString Function ]*/
#define STRINGIFY(x) #x
#define TOSTRING(x) STRINGIFY(x)


/* [ Console Print Headers ]*/
static constexpr std::string_view HDAPP = "[ Peach Boostrap ] ";
static constexpr std::string_view HDHOU = "[ Peach Boostrap : Houdini ]";
static constexpr std::string_view HDBLD = "[ Peach Boostrap : Blender ]";
 
 /* Peach Namespaced Headers */
namespace Peach{
    extern bool PEACH_BOOTSTRAP_DEBUG_MODE;
    extern std::string PEACH_VER;
    extern std::string PBTP_PACKAGE_VER;
    extern std::string PBTP_HOU_VERSION;
    extern std::string PBTP_BLN_VERSION;
}

inline void PrintPackageMsg()
{
    std::cout << "[ Peach Boostrap ] Init ... " << std::endl;
}

inline void PrintPackageVer()
{
    std::cout << "[ Peach ] Version: " << Peach::PEACH_VER << std::endl;
    std::cout << "[ Peach Boostrap ] Version: " << Peach::PBTP_PACKAGE_VER << std::endl;
}

inline void PrintHouVer()
{
    std::cout << HDHOU << " Version: " << Peach::PBTP_HOU_VERSION << std::endl;
}

inline void PrintBlnVer()
{
    std::cout << HDBLD << " Version: " << Peach::PBTP_BLN_VERSION << std::endl;
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


/* [ HELP: Printing Content ] */
#define HELP_MSG "Print Help... \n\n \
[ Allowed Flags ]:\n \
-v | --version ..... Display current Bootstrap version\n \
-h | --help    ..... Display help message\n \
-d | --debug   ..... Set Debug Mode as True\n"


/* [ Argument Handling Function ]
In this functions, The argument(single input) will be processed
through this function. */
///@param arg: (std::string &) argument that put in
///@param app: (enum Type) which dcc context
/////////////////////////////////////////////////////////////////
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
        Peach::PEACH_BOOTSTRAP_DEBUG_MODE = true;
        PrintMsg("Debug=True");
        return true;
    }
    else
    {
        std::string msg = "Cannot Recognise the flag "
                            + arg 
                            + ", please use --help or -h";
        PrintMsg(msg.c_str());
        return false;
    }
    return false;
}
#endif