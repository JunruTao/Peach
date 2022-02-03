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
# [ File Name ] __init__.py@python
# [ File Description ] - 2022.02.03 (Y.M.D) - 13:33
#                            *   *   *   *
#
#   This script contains
#
# ---------------------------------------------------------------------
from peach.pBlender import pbu
from .ui import PbUiAssetPrep

classes = (
    PbUiAssetPrep,
)


bl_info = {
    "name": "bAsset",
    "blender": (3, 0, 0),
    "author": "Digital Peach Studio",
    "version": (1, 0),
    "category": "Object",
}


def register():
    pbu.r_cls(*classes)


def unregister():
    pbu.r_cls(*classes)
