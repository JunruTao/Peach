#ifndef __FINDCONFIG_H__
#define __FINECONFIG_H__
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>

#define STARTUP_ENV_FILEPATH "config/startup.env"
#define STARTUP_INIT_SHELLPATH "config/shell/startup_dcc_init.sh"

static const std::string win_cdisk = "C:";
static const std::string shl_cdist = "/c";

static inline void PrintConfigMsg(const std::string& msg)
{
    std::cout << "[ Peach Config ] " << msg << std::endl;
}

static inline void ReplaceBackslash(std::string& line)
{
    // this function only for converting linux scripts to shell
    std::replace(line.begin(), line.end(), '\\', '/');
}

static inline void ReplaceForeslash(std::string& line)
{
    // this function only for converting linux scripts to shell
    std::replace(line.begin(), line.end(), '/', '\\');
}

static inline void FormatWindowsString(std::string& line)
{
    PrintMsg("System: Running on Win32 system");
    line.replace(line.begin()+1, line.begin()+1+win_cdisk.size(), shl_cdist);
    ReplaceBackslash(line);
}


static inline void PassArguments(std::string& line, const std::string& arg)
{
    if(!arg.empty())
    {
        line.pop_back();
        line += " " + arg;
        line += "\"";
    }
}

static inline void ReplaceEmptySpace(std::string& line)
{
    if(line.find(" ") != std::string::npos)
    {
        std::istringstream iss(line);
        std::string item;
        std::string result = "";
        while(std::getline(iss, item, ' '))
        {
            result +=  item + "\\ ";
        }
        line = std::move(result);
        line.pop_back();
        line.pop_back();
        line.pop_back();
        line += "\"";
    }
}

inline std::string RunConfig(Type type=Type::HOUDINI, std::string dcc_args="")
{
    std::string startup_env_path(STARTUP_ENV_FILEPATH);
    #ifdef _WIN32
        /* On linux, should replace the \\ with / */
        ReplaceForeslash(startup_env_path);
    #endif

    std::ifstream startup_env_file(startup_env_path.c_str());

    if(startup_env_file.is_open())
    {
        PrintConfigMsg("Found \"config/startup.env\"");
        std::string line;
        while(std::getline(startup_env_file, line))
        {
            std::string delimiter = "=";
            size_t pos = line.find(delimiter);
            std::string token = line.substr(0, pos);

            switch (type)
            {
            case Type::HOUDINI :
                if(token=="houdini_executable")
                {
                    
                    line.erase(0, pos + delimiter.length());
                    #ifdef _WIN32
                        FormatWindowsString(line);
                    #endif
                    ReplaceEmptySpace(line);
                    PassArguments(line, dcc_args);
                    
                    PrintConfigMsg("Houdini: " + line);
                    return line;
                }
                break;
            case Type::BLENDER:
                if(token=="blender_executable")
                {
                    line.erase(0, pos+delimiter.length());
                    #ifdef _WIN32
                        FormatWindowsString(line);
                    #endif
                    ReplaceEmptySpace(line);
                    PassArguments(line, dcc_args);

                    PrintConfigMsg("Blender: " + line);
                    return line;
                }
                break;
            default:
                break;
            }
        }
    }
    return "missing";
}

#endif