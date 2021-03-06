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
# [ File Name ] pImp.py@python
# [ File Description ] - 2022.01.09 (Y.M.D) - 13:18
#                            *   *   *   *
#
#   This File contains all the necessary functions that related to lib
#   importing and other configurations.
#
# ---------------------------------------------------------------------
import sys

# [ ALLOW RELOAD TOGGLE ]
ALLOW_MODULE_RUNTIME_RELOAD = True


# [ RELOAD FUNCTION ]
def reload(*args, force=False):
    """
    Function wrap around the module reload. This function
    allows users to reload multiple modules.

    param args: modules to reload
    """
    if ALLOW_MODULE_RUNTIME_RELOAD or force:
        # [ LOADING RELOADING MODULES ]
        if sys.version_info.major >= 3 and sys.version_info.minor >= 4:
            # if version greater than 3.4
            import importlib as il
        else:
            import imp as il

        if len(args):
            for module in args:
                il.reload(module)
