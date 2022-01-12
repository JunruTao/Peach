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
from peach.pQt.qHotel import QtGui
from peach import pImp
from peach import pDir
from peach import pLog
from peach import pIco
pImp.reload(pIco, pDir, pLog)


# [ GLOBAL OBJECT ]
_ico_tank = pIco.IconTank()


# [ PUBLIC FUNCTIONS ]
def getPixmap(name="", size="x25"):
    """
    [ Public Getter Function ]from name get QPixmap UI object
    @param name: (str) Icon name
    @param size: (str) Icon size/type
    @return: (QtGui.QPixmap or None)
    """
    path = _ico_tank.get(name).getPath(size)
    if not path:
        # _____PRINT_WARNINGS_____
        pLog.warning("icon \"%s_%s\" not found" % (name, size),
                     fn=getPixmap,
                     cls=pDir.fileNameBare(__file__))
        return None
    return QtGui.QPixmap(path)


# [ ICON MANAGER CLASS ]
class IconManager(object):
    # [ IconManager::Static ] Data Container
    pixmap_dict = dict()

    def __init__(self, size="x25"):
        """[ IconManager ] Constructor"""
        self._size = size
        pass

    def _create_key(self, name, size_=""):
        if not size_:
            size_ = self._size
        return "{name}_{size}".format(name=name, size=size_)

    def stash(self, *args):
        """
        [ IconManager ]
        @param args: *(str) icon names to create
        """
        for icon_name in args:
            key = self._create_key(icon_name)
            if key not in self.pixmap_dict:
                # this size of the same icon exists in the database.
                ico = _ico_tank.get(icon_name)
                if ico:
                    self.pixmap_dict[key] = getPixmap(icon_name, self._size)
            else:
                # _____PRINT_DEBUG_____
                pLog.debug("qt_pixmap-icon \"%s\" has already been created." % key,
                           fn=self.stash,
                           cls=self)

    def stash_all(self):
        """
        [ IconManager ] Scan existing Data base and log all.
        """
        self.stash(*_ico_tank.getNames())

    def get(self, name, size_=""):
        """
        [ IconManager ] Getter
        @param name: (str) icon name
        @param size_: (str) size/type
        @return: (QtGui.QPixmap or None)
        """
        key = self._create_key(name, size_)
        if key not in self.pixmap_dict:
            # _____PRINT_WARNINGS_____
            pLog.warning("icon \"%s_%s\" not found" % (name, key),
                         fn=self.get,
                         cls=self)
            return None
        return self.pixmap_dict[key]
