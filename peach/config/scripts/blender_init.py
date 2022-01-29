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

import sys
sys.path.append('./lib/python')

try:
    import peach
except ImportError as e:
    raise e
finally:
    from peach import pLog
    pLog.message("import <peach> Module SUCCESS..", fn="Import", cls="pBlender")

from peach.pBlender import pbu
pbu.purge_scene() 