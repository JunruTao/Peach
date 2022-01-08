#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
