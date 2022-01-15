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


# Color Cast
def fRGB(*args):
    """
    From given arguments cast to RGB tuple
    @param args: (float) color values 0.0-1.0
    @return: (tuple of 3 floats)
    """
    if len(args) == 1:
        greyscale = float(args[0])
        return greyscale, greyscale, greyscale
    if len(args) == 2:
        return args[0], args[1], 0.0
    if len(args) > 2:
        return args[0], args[1], args[2]


def fRGBA(*args):
    """
    From given arguments cast to RGBA tuple
    @param args: (float) color values 0.0-1.0
    @return: (tuple of 4 floats)
    """
    if len(args) == 1:
        greyscale = float(args[0])
        return greyscale, greyscale, greyscale, 1.0
    if len(args) == 2:
        return args[0], args[1], 0.0, 1.0
    if len(args) == 3:
        return args[0], args[1], args[2], 1.0
    if len(args) > 3:
        return args[0], args[1], args[2], args[3]
