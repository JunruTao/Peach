#ifndef __FINDCONFIG_H__
#define __FINECONFIG_H__

/* [ Header Includes ]*/
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>

/* [ Start-up File Locations ] */
#define STARTUP_ENV_FILEPATH "config/startup.pconfig"
#define STARTUP_INIT_SHELLPATH "config/shell/startup_dcc_init.sh"

/* [ windows OS helper Data ] */
static const std::string win_cdisk = "C:";
static const std::string shl_cdist = "/c";

static inline void PrintConfigMsg(const std::string& msg)
{
    std::cout << "[ Peach Config ] " << msg << std::endl;
}

static inline void PrintParserMsg(const std::string& msg)
{
    std::cout << "[ Peach Config::Parser ] " << msg << std::endl;
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

static inline void StripWhiteSpace(std::string& line)
{
    if(!line.empty()){
        while(line.starts_with(" "))
        {
            line.erase(0);
        }
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
    std::string line = "";
    std::string line_out = "";

    if(startup_env_file.is_open())
    {
        PrintConfigMsg("Found - \"config/startup.pconfig\"");
        PrintParserMsg("Parsing startup.pconfig...");
        
        while(std::getline(startup_env_file, line, '\n'))
        {
            if(line.empty())
                PrintParserMsg("(\\n) SKIP EMPTY LINE");
            if(line.starts_with("#"))
                PrintParserMsg("(#) SKIP COMMENT");
            else{
                std::string delimiter = "=";
                size_t pos = line.find(delimiter);
                if(pos != std::string::npos)
                {
                    std::string token = line.substr(0, pos);
                    line.erase(0, pos + delimiter.length());
                    if(token=="debug")
                    {
                        PrintParserMsg("Found token : debug");
                        Peach::__DEBUG = line == "TRUE";
                        PrintConfigMsg("Debug Mode : " + std::to_string(Peach::__DEBUG));
                    }
                    if(token=="houdini_executable" && type==Type::HOUDINI )
                    {
                        PrintParserMsg("Found token : houdini_executable");
                        #ifdef _WIN32
                            FormatWindowsString(line);
                        #endif
                        ReplaceEmptySpace(line);
                        PassArguments(line, dcc_args);

                        PrintConfigMsg("Houdini: " + line);
                        line_out = line;
                    }
                    if(token=="blender_executable" && type==Type::BLENDER)
                    {
                        PrintParserMsg("Found token : blender_executable");
                        #ifdef _WIN32
                            FormatWindowsString(line);
                        #endif
                        ReplaceEmptySpace(line);
                        PassArguments(line, dcc_args);

                        PrintConfigMsg("Blender: " + line);
                        line_out = line;

                    }/*end of <if in token parsing>*/

                }/*end of <if found token sentence>*/
            
            }/*end of <else>*/

        }/*end of <while readline>*/

    }/*end of <if fileopen>*/

    return line_out;
}

#endif