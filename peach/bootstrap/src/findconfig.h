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
#define STARTUP_INIT_SHELLPATH "config/bootstrap/startup_dcc_init.sh"
#define STARTUP_INIT_PWSHLPATH "powershell config/bootstrap/startup_dcc_init.ps1"

#define IS ==
#define AND &&
#define OR ||

#define PRINT_PARSING_MSG  false 
/* [ Peach Globals ]*/
namespace Peach
{
    extern std::string init_script_command;
    extern std::string init_script_type;
}


/* [Printing Functions ]
//////////////////////////////////////////////////////////*/

// [ Print Config ]
static inline void PrintConfigMsg(const std::string& msg)
{
    std::cout << "[ Peach Config ] " << msg << std::endl;
}

// [ Print Parsing Message(Debug Mode Only) ]
static inline void PrintParserMsg(const std::string& msg)
{
    if(PRINT_PARSING_MSG)
        std::cout << "[ Peach Config::Parser ] " << msg << std::endl;
}


/* [Parsing Functions] 
//////////////////////////////////////////////////////////*/

//
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
    PrintMsg("Bash on Windows: Replace Disk name: i.g. C: with /c");

    auto replace_block = line.substr(1, 2);
    auto disk = tolower(replace_block[0]);
    std::string replacement = "/" + std::string(1, disk);

    line.replace(line.begin()+1, line.begin()+1+replace_block.size(), replacement);
    ReplaceBackslash(line);
}

static inline void ReplaceEmptySpaceInPathString(
    std::string& line, 
    const std::string& div="\\")
{
    if(line.find(" ") != std::string::npos)
    {
        std::istringstream iss(line);
        std::string item;
        std::string result = "";
        while(std::getline(iss, item, ' '))
        {
            result +=  item + div + " ";
        }
        line = std::move(result);
        line.pop_back();
        line.pop_back();
        line.pop_back();
        line += "\"";
    }
}

static inline void PathParsing(std::string& line)
{
    //for shell on windows only
    if(Peach::init_script_type == "sh")
    {
        //shell
        #ifdef _WIN32
            FormatWindowsString(line);
        #endif
        
        ReplaceEmptySpaceInPathString(line, "\\");
    }else
    {
        //power shell
        line.erase(0, 1);
        line.pop_back();
        line = "'" + line + "'";
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

inline std::string RunConfig(Type type)
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
        
        while(std::getline(startup_env_file, line))
        {
            // { Empty Line }
            if(line.empty())
                PrintParserMsg("(\\n) SKIP EMPTY LINE");
            // { Line Comments }
            else if(line.starts_with("#"))
                PrintParserMsg("(#) SKIP COMMENT");
            // { Try Parsing Tokens }
            else{
                // { Split Token and Value }
                std::string delimiter = "=";
                size_t pos = line.find(delimiter);

                if(pos != std::string::npos)
                {
                    std::string token = line.substr(0, pos);
                    line.erase(0, pos + delimiter.length());

                    if(token IS "debug")
                    {
                        PrintParserMsg("Found token : debug");
                        Peach::PEACH_BOOTSTRAP_DEBUG_MODE = 
                                            (line IS "TRUE") OR 
                                            (line IS "True") OR
                                            (line IS "true");
                        // Notes: Anything else will be treated as False
                        PrintConfigMsg("Debug Mode : " + std::to_string(Peach::PEACH_BOOTSTRAP_DEBUG_MODE));
                    }
                    else if(token IS "houdini_executable")
                    {
                        if(type IS Type::HOUDINI )
                        {
                            PrintParserMsg("Found token :" + token);
                            PrintConfigMsg("Houdini: " + line);
                            line_out = line; // Set return value
                        }
                    }
                    else if(token IS "blender_executable")
                    {
                        if(type IS Type::BLENDER)
                        {
                            PrintParserMsg("Found token :" + token);
                            PrintConfigMsg("Blender: " + line);
                            line_out = line; // Set return value
                        }
                    }
                    else if(token IS "startup_script_mode")
                    {
                        PrintParserMsg("Found token :" + token);
                        // By default, init script is shell
                        Peach::init_script_command = std::string(STARTUP_INIT_SHELLPATH);
                        Peach::init_script_type = "sh";
                        PrintParserMsg(line);
                        if(line IS "\"sh\"")
                        { 
                            /*do nothing*/ 
                            PrintParserMsg("Using Bash");
                        }
                        else if(line IS "\"ps\"") 
                        {
                            // forced using powershell
                            PrintParserMsg("Using PowerShell");
                            Peach::init_script_command = std::string(STARTUP_INIT_PWSHLPATH);
                            Peach::init_script_type = "ps";
                        }
                        else
                        {
                            //Any other value will be treated as "auto"
                            #ifdef _WIN32
                                PrintParserMsg("Auto: Using PowerShell");
                                Peach::init_script_command = std::string(STARTUP_INIT_PWSHLPATH);
                                Peach::init_script_type = "ps";
                            #else
                                PrintParserMsg("Auto: Using Bash");
                            #endif
                        }
                        // detect which script to use.
                        #ifdef _WIN32
                            ReplaceForeslash(Peach::init_script_command);
                        #endif
                    }
                    else
                    {
                        // Runtime not finding any corret token or value
                        PrintParserMsg("Unknown PConfig Script");
                    }/*end of <if in token parsing>*/

                }/*end of <if found token sentence>*/
                else
                {   
                    // Runtime not finding any corret gramma
                    PrintParserMsg("Unknown PConfig Script");
                }/*end of <not found token sentence>*/
            
            }/*end of <else>*/

        }/*end of <while readline>*/

    }/*end of <if fileopen>*/
    PathParsing(line_out);
    return line_out;
}

#endif