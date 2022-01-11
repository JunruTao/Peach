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
# [ File Name ] pq_ico.py@python
# [ File Description ] - 2022.01.11 (Y.M.D) - 19:51
#                            *   *   *   *
#
#   This script contains Qt Functions, picture resource, icon management.
#
# ---------------------------------------------------------------------
from .qHotel import QtGui
from peach import pImp
from peach import pIco
pImp.reload(pIco)


# [ GLOBAL OBJECT ]
_ico_tank = pIco.IconTank()


# [ PUBLIC FUNCTIONS ]
def getIcon(name="", size="x25"):
    """
    [ Public Getter Function ]from name get QPixmap UI object
    @param name: (str) Icon name
    @param size: (str) Icon size/type
    @return: (QtGui.QPixmap)
    """
    path = _ico_tank.get(name).getPath(size)
    return
