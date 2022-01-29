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
# [ File Name ] pUtil.py@python
# [ File Description ] - 2022.01.15 (Y.M.D) - 15:05
#                            *   *   *   *
#
#   This script contains utility functions of peach module.
#   Anything else that commonly used to convert, do math, naming
#   parsing, etc. Should be included in this module
#
# ---------------------------------------------------------------------

# [ Functions ]: Color Casting
def _col_num_to_normalize(*args):
    """[ Internal ] AnyNum -> (0.0 ~ 1.0)Value"""
    values = []
    if len(args):
        for value in args:
            if value is not None:
                if value <= 1.0:
                    values.append(max(0.0, float(value)))
                else:
                    values.append(min(float(value)/255.0, 1.0))
    return values


def _col_float_to_8bits(*args):
    """[ Internal ] AnyNum -> (0 ~ 255)Value"""
    values = []
    if len(args):
        for value in args:
            if value is not None:
                if isinstance(value, int):
                    values.append(max(0, int(value)))
                elif isinstance(value, float):
                    values.append(min(int(value * 255.0), 255))
    return values


def fRGB(*args):
    """
    From given arguments cast to RGB tuple
    @param args: (float) color values 0.0-1.0
    @return: (tuple of 3 floats)
    """
    values = _col_num_to_normalize(*args)
    if len(values) == 1:
        return values[0], values[0], values[0]
    elif len(values) == 2:
        return values[0], values[1], 0.0
    elif len(values) > 2:
        return values[0], values[1], values[2]
    else:
        return 0.0, 0.0, 0.0


def fRGBA(*args):
    """
    From given arguments cast to RGBA tuple
    @param args: (float) color values Any
    @return: (tuple of 4 floats)
    """
    values = _col_num_to_normalize(*args)
    if len(values) == 1:
        return values[0], values[0], values[0], 1.0
    elif len(values) == 2:
        return values[0], values[1], 0.0, 1.0
    elif len(values) == 3:
        return values[0], values[1], values[2], 1.0
    elif len(values) > 3:
        return values[0], values[1], values[2], values[3]
    else:
        return 0.0, 0.0, 0.0, 1.0


def sRGB(*args):
    """
    From given arguments cast to RGB tuple
    @param args: (float) color values Any
    @return: (tuple of 3 ints) 0-255 int8
    """
    values = _col_float_to_8bits(*args)
    if len(values) == 1:
        return values[0], values[0], values[0]
    elif len(values) == 2:
        return values[0], values[1], 0
    elif len(values) > 2:
        return values[0], values[1], values[2]
    else:
        return 0, 0, 0


def sRGBA(*args):
    """
    From given arguments cast to RGBA tuple
    @param args: (float) color values Any
    @return: (tuple of 4 ints) 0-255 int8
    """
    values = _col_float_to_8bits(*args)
    if len(values) == 1:
        return values[0], values[0], values[0], 1
    elif len(values) == 2:
        return values[0], values[1], 0.0, 1
    elif len(values) == 3:
        return values[0], values[1], values[2], 1
    elif len(values) > 3:
        return values[0], values[1], values[2], values[3]
    else:
        return 0, 0, 0, 255


def launch_background_blender(python_file=""):
    from peach import pDir
    import subprocess
    blender_exe = pDir.getBlenderExeDir()
    subprocess.run([blender_exe, "--background", "--python", python_file])
