#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
# [ File Description] - 2022.01.08 (Y.M.D)
#                             *   *   *   *
#   This file is purposed for loading configuration and packages.
#
# ---------------------------------------------------------------------

import os
from turtle import pd

# GLOBAL VARIABLES
mode = "normal"

# $dirs:
peach_dir = ""
phoudini_dir = ""
working_dir = ""

# the peach env file:
peach_env_filename = "PeachEnv.json"
peach_packages = []


# houdini environment varibles setting:
henv_PEACH = "PEACH"
henv_PEACH_HOU = "PEACH_HOU"
henv_GLOBS = ["HIP", "JOB", "HSITE"]

# Convert dir to Houdini Format
def format_dir(dir):
    return dir.replace("\\","/")


# Print Function
def printMsg(msg):
    if mode != "dev":
        print("[ PEACH HOUDINI ]: {}".format(msg) )
    else:
        print("[ PEACH-DEV HOUDINI ]: {}".format(msg) )
        

# Loading Houdini.  
def tryImportHou():
    # [ Loading Hou Module ]
    printMsg("Running pHoudini...")
    printMsg("Try importing module <hou>...")
    try:
        import hou
    except ImportError:
        print("Can not Import <hou> module")
        return False
    finally:
        printMsg("Module <hou> import successfully")
    return True

# Loading Hou Module
if(tryImportHou()):
    import hou


def loadPeachEnvPackage():
    # [ Loading Peach Env ]
    _peach_env_filepath = format_dir(os.path.join(phoudini_dir, peach_env_filename))
    
    printMsg("Loading Peach Env Package")
    try:
        hou.ui.loadPackage(_peach_env_filepath)
    except FileNotFoundError:
        printMsg("package: %s can not be found" % _peach_env_filepath)
    finally:
        printMsg("---package Found: %s" % _peach_env_filepath)

 
def loadPeachPackages():    
    package_dir = format_dir(os.path.join(phoudini_dir, "packages"))
    
    if not len(peach_packages):
        # find package list:
        printMsg("Finding package_list.txt...")
        pkg_list = format_dir(os.path.join(phoudini_dir, "package_list.txt"))
        
        if not os.path.exists(pkg_list):
            # Here should find packages by searching directory:
            dirs = [f.path for f in os.scandir(package_dir) if f.is_dir()]
            if len(dirs):
                for d in dirs:
                    package_name = os.path.basename(d)
                    if os.path.exists(os.path.join(package_dir, "%s.json" % package_name)):
                        printMsg("Found Package: \"%s.json\" file" % package_name)
                        printMsg("Appending Package: %s" % package_name)
                        peach_packages.append(package_name)
                    else:
                        printMsg("Warning: illegal directory in package path [ %s ]" % package_name)
            else:
                printMsg("Warning: No Peach Package is Found")
        else:
            printMsg("Found package_list.txt")
            with open(pkg_list, 'r') as f:
                for line in f:
                    if len(line):
                        line = line.replace('\n','')
                        printMsg("---Package to load: { %s }" % line)
                        peach_packages.append(line)
            f.close()
    
    printMsg("Loading Peach Packages...")
    for pkg in peach_packages:
        pkg_dir = format_dir(os.path.join(package_dir, "%s.json" % pkg))
        printMsg("---Loading <%s> Package" % pkg)
        try:
            hou.ui.loadPackage(pkg_dir)
        except FileNotFoundError:
            printMsg("---package: <%s> can not be found" % pkg)
        finally:
            printMsg("---+ ---package <%s> Found" % pkg)
            printMsg("---+ ---path: %s" % pkg_dir)
            

def setDirAndPrint():
    global peach_dir
    global phoudini_dir
    global working_dir
    
    peach_dir = format_dir(peach_dir)
    phoudini_dir = format_dir(phoudini_dir)
    working_dir = format_dir(working_dir)
    
    with open(os.path.join(peach_dir, "config", "startup.pconfig")) as f:
        cf_wd = ""
        for line in f:
            if line.startswith("working_dir"):
                cf_wd = line.split("\"")[1]
                break
        if os.path.isdir(cf_wd):
            printMsg("Found WD Override! in startup.pconfig")
            working_dir = format_dir(cf_wd)

    # [ Setting $PEACH in Houdini ]
    hou.putenv(henv_PEACH, peach_dir)
    printMsg("Peach Dir: %s" % peach_dir)
    printMsg("---set as '$%s'" % henv_PEACH)
    
    # [ Setting $PEACH in Houdini ]
    hou.putenv(henv_PEACH_HOU, phoudini_dir)
    printMsg("pHoudini Dir: %s" % phoudini_dir)
    printMsg("---set as '$%s'" % henv_PEACH_HOU)
    
    # [ Getting Workfing Directroy ]
    printMsg("Current Working Directory: %s" % working_dir)
    for env in henv_GLOBS:
        hou.putenv(env, working_dir)
        printMsg("---set '$%s' to this Working Directory" % env)