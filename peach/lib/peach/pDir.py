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
import pImp
import pLog

pImp.reload(pLog)


# [ PATH FORMAT ]
def pathSlashCvt(path=""):
    """For windows-Houdini, Convert '\\' to '/'.
    """
    return path.replace("\\", "/")


# [ PATH FUNCTIONS ] - os.path impl
def join(*args):
    """
    Join directories
    :param args: *(str) path components
    :return: (str) joined path
    """
    return pathSlashCvt(os.path.join(*args))


def exists(path):
    """
    Check if the path exists
    :param path: (str) path
    :return: (bool) if exists
    """
    return os.path.exists(path)


# [ PEACH DIR FUNCTION ]
def getPeachDir():
    """
    [ Peach ] Getting the installation path of the Peach
    :return: (str) fores-lashed path
    """
    p_path = os.path.dirname(__file__)
    while not (exists(join(p_path, "config")) and exists(join(p_path, "icons"))):
        last_dir = p_path
        p_path = os.path.dirname(p_path)
        if last_dir == p_path:
            # [ error ] this means it's down to root, and missing config folder.
            pLog.error("Cannot Locate Peach Dir, illegal Usage", subject=getPeachDir.__name__)
            return None
    return pathSlashCvt(p_path)


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

