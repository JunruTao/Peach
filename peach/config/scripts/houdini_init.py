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
import houdini_util as hu
import hou


# [ This is the Release Version ]
hu.mode = "normal"

# [ Getting the Peach Install Dir ]
hu.peach_dir = os.path.realpath(".")
hu.phoudini_dir = os.path.join(hu.peach_dir, "pHoudini")
hu.working_dir = str(os.path.realpath(".."))

# [ Run Functions ]
hu.setDirAndPrint()
hu.loadPeachEnvPackage()
hu.loadPeachPackages()