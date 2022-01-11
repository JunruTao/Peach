#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) 2022 Digital Peach Studio - Junru Tao
# This code is licensed under MIT license (see LICENSE.txt for details)
#                            *   *   *   *
# [ Info ] - Digital Peach Studio
# - Authors: Junru Tao
# - Contact: <junrtao.uk@gmail.com | junrutao@qq.com>
# - Website: digital-peach.company.site
# - Instagram: @digital.peach.studio
# ---------------------------------------------------------------------
# [ File Name ] pDir.py@python
# [ File Description ] - 2022.01.09 (Y.M.D) - 16:46
#                            *   *   *   *
#
#   This script contains functions and variables that related to path,
#   Directory functions.
#   *Note: all paths returned should be fore-slash format
#
# ---------------------------------------------------------------------
import os
from peach import pImp
from peach import pLog

pImp.reload(pLog)
_PEACH_DIR = None


# [ PATH FORMAT ]
def pathSlashConvert(path=""):
    """
    For windows-Houdini, Convert '\\' to '/'.
    @param path: (str) path to convert
    @return: (str) converted path string
    """
    return path.replace("\\", "/")


def remove_ext(file_name=''):
    """[ Path ] remove extension """
    return (os.path.splitext(file_name))[0]


def exists(path):
    """
    Check if the path exists
    @param path: (str) path
    @return: (bool) if exists
    """
    return os.path.exists(path)


# [ PATH FUNCTIONS ] - os.path impl
def join(*args):
    """
    Join directories
    @param args: *(str) path components
    @return: (str) joined path
    """
    return pathSlashConvert(os.path.join(*args))


def ls(path="", n=False):
    """[ List Directory ] path and files
    @param path: (str) directory
    @param n: (bool) if return name
    @return: (list)dir_name/dir_fullpath, None if not exist
    """
    if not exists(path):
        return None
    if n:
        return [f.name for f in os.scandir(path)]
    return [f.path for f in os.scandir(path)]


def listdir(path="", n=False):
    """[ List Directory ] directories only
    @param path: (str) directory
    @param n: (bool) if return name
    @return: (list)dir_name/dir_fullpath, None if not exist
    """
    if not exists(path):
        return None
    if n:
        return [f.name for f in os.scandir(path) if f.is_dir()]
    return [f.path for f in os.scandir(path) if f.is_dir()]


def listfiles(path="", n=False):
    """[ List Directory ] files only
    @param path: (str) directory
    @param n: (bool) if return name
    @return: (list)dir_name/dir_fullpath, None if not exist
    """
    if not exists(path):
        return None
    if n:
        return [f.name for f in os.scandir(path) if f.is_file()]
    return [f.path for f in os.scandir(path) if f.is_file()]


# [ PEACH DIR FUNCTION ]
def getPeachDir():
    """
    [ Peach ] Getting the installation path of the Peach.
    @note:
         This function will only search once in runtime when it
         is called, it's recursive search from the python module
         until it finds the root `${PEACH}` folder. After that,
         it will store the value in `_PEACH_DIR` file scope global
         variable.
    @return: (str) fores-lashed path
    """
    global _PEACH_DIR
    if _PEACH_DIR and exists(_PEACH_DIR):
        # /.calculate once only in runtime
        return _PEACH_DIR

    p_path = os.path.dirname(__file__)
    while not (exists(join(p_path, "config")) and exists(join(p_path, "icons"))):
        last_dir = p_path
        p_path = os.path.dirname(p_path)
        if last_dir == p_path:
            # _____PRINT_ERROR_MESSAGE_____
            # [ error ] this means it's down to root, and missing config folder.
            pLog.error("Cannot Locate Peach Dir, illegal Usage", cls="pDir", fn=getPeachDir)
            return None
    _PEACH_DIR = pathSlashConvert(p_path)
    return _PEACH_DIR


# [ PEACH SUB DIRS ]
def getPeachConfigsDir():
    """[ Peach ] Get `$PEACH/config` folder realpath """
    return join(getPeachDir(), "config")


def getPeachHouDir():
    """[ Peach ] Get `$PEACH/pHoudini` folder realpath """
    return join(getPeachDir(), "pHoudini")


def getPeachBlnDir():
    """[ Peach ] Get `$PEACH/pBlender` folder realpath """
    return join(getPeachDir(), "pBlender")


# [ PEACH IMG RESOURCE PATHS ]
def getPeachIconsDir():
    """[ Peach ] Get `$PEACH/icons` folder realpath """
    return join(getPeachDir(), "icons")
