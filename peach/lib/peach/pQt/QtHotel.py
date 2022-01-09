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
# [ File Name ] QtHotel.py@python
# [ File Description ] - 2022.01.09 (Y.M.D) - 13:17
#                            *   *   *   *
#
#   This is an import wrapper for importing Qt/PyQt/PySide2 libraries
#   If PySide2 is not available, simply change the `from` section.
#
# ---------------------------------------------------------------------
from PySide2 import (QtWidgets,
                     QtGui,
                     QtCore,
                     )


_print_modules = False
if _print_modules:
    print(QtWidgets, QtGui, QtCore)
