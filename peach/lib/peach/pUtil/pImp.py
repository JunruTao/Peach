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
# ---------------------------------------------------------------------
# [ File Description] - 2022.01.08 (Y.M.D)
#                             *   *   *   *
#   This File contains all the necessary functions that related to lib
#   importing and other configurations.
#
# ---------------------------------------------------------------------

import sys


# [ PYTHON VERSION ]
python_version = sys.version_info[0]

# [ LOADING RELOADING MODULES ]
if sys.version_info[0] >= 3.4:
    from importlib import reload
else:
    from imp import reload


# [ RELOAD FUNCTION ]
def reload_modules(*args):
    """
    Function wrap around the module reload. This function
    allows users to reload multiple modules.

    :param args: modules to reload
    """
    if len(args):
        for module in args:
            reload(module)
