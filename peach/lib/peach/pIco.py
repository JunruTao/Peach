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
# [ File Name ] pIco.py@python
# [ File Description ] - 2022.01.09 (Y.M.D) - 21:38
#                            *   *   *   *
#
#   This script contains key functions and class for handling icon and
#   image resources.
#
# ---------------------------------------------------------------------
from peach import (pImp, pDir, pLog)
pImp.reload(pDir, pLog)

# [ global-variables ] Private
_PEACH_ICON_DIR = ""


# [ global-functions ] Public
def configure_icon_path():
    """
    Configure path only once, the value will be stored.
    """
    global _PEACH_ICON_DIR
    if _PEACH_ICON_DIR == "":
        _PEACH_ICON_DIR = pDir.getPeachIconsDir()


class Icon(object):
    # [ Constructor ]
    def __init__(self, name="", types=None):
        """
        [ Icon ] Constructor
        @param name: (str) icon name
        @param types: (list[str]) i.g. "x25", "SVG" etc.
        """
        self._name = name
        self._data = dict()

        # /.make sure there's valid path
        configure_icon_path()

        # /.ensure there are types
        if types:
            # /..cast a single value to list
            if isinstance(types, str):
                types = [types, ]
            # /..then make sure it's a list
            if isinstance(types, list):
                # /..Map in keys -> { size/type : filepath }
                for t in types:
                    folder = "%sw" % t
                    suffix = "_x%s" % t
                    ext = "png"
                    if t == "SVG":
                        suffix = ""
                        ext = "svg"
                        folder = t
                    p = pDir.join(
                        _PEACH_ICON_DIR,
                        folder,
                        "icon_%s%s.%s" % (self._name, suffix, ext))
                    if pDir.exists(p):
                        self._data[str(t)] = p
                    else:
                        # _____PRINT_WARNINGS_____
                        pLog.warning("File Missing: %s" % p, cls=self, fn="Constructor")

    def getPath(self, size="SVG"):
        """
        [ Icon ] getter
        Get Icon File Path, size default will be getting "SVG"
        @param size: (str) i.g. "x25", "SVG" etc.
        @return: (str/None) filepath of the icon
        """
        return self._data[size] if size in self._data else None

    def getName(self):
        """
        [ Icon ] getter
        Getting the name of this icon object.
        @return: (str) name
        """
        return self._name


class IconTank(object):
    # [ Class Static Data ]
    _icon_types = []
    _data = dict()

    # [ Constructor ]
    def __init__(self):
        """[ IconTank ] Constructor"""
        # /.construct icon database once only
        if not len(self._icon_types):
            self._construct_library()

    def _construct_library(self):
        """
        [ IconTank ] Private
        Construct/Log in all the found icons. by scanning the directory.
        This function will be only running once. unless refresh is called.
        """
        # /.find ./icons folder
        configure_icon_path()
        folders = pDir.listdir(_PEACH_ICON_DIR, n=True)
        # /.remove exceptions
        exclusions = ["scripts", "ICO"]
        for e in exclusions:
            if e in folders:
                folders.remove(e)
        # /.found folders
        if len(folders):
            # /..log in types
            for f in folders:
                f = str(f)
                if f.endswith("w"):
                    f = f[:-1]
                self._icon_types.append(f)

            # /..list all the objects in the first icon directory
            for name in pDir.listfiles(pDir.join(_PEACH_ICON_DIR, folders[0]), n=True):
                # /...extract pure name:
                # /... ..."icon_<name>{opt._x<size>}.<ext>"
                name = pDir.remove_ext(name).replace("icon_", "")
                name = name.replace("_" + name.split("_")[-1], "")
                # /...create icon objects
                self._data[name] = Icon(name, self._icon_types)
        else:
            # _____PRINT_WARNINGS_____
            pLog.warning("No Icon-sub-folders found under: %s" % _PEACH_ICON_DIR,
                         cls=self,
                         fn="Constructor")

    def refresh(self):
        """
        [ IconTank ] Public
        Clear Icon Database and rescan directory.
        @return:
        """
        self._icon_types.clear()
        self._data.clear()
        self._construct_library()

    def getTypes(self) -> list:
        """
        [ IconTank ] getter
        @return: (list) icon types
        """
        return self._icon_types

    def getNames(self) -> list:
        """
        [ IconTank ] getter
        @return: (list) icon names
        """
        names = []
        for key, ico in self._data.items():
            names.append(key)
        return names

    def get(self, name=""):
        """
        [ IconTank ] getter
        @param name: (str) name of icon to look up
        @return: (Icon) object
        """
        return self._data[name] if name in self._data else None

    def printTypes(self):
        """[ IconTank ] Debug Function"""
        # _____PRINT_DEBUG_MESSAGE_____
        pLog.debug(*self.getTypes(), fn="Types", cls=self)

    def printNames(self):
        """[ IconTank ] Debug Function"""
        # _____PRINT_DEBUG_MESSAGE_____
        pLog.debug(*self.getNames(), fn="Names", cls=self)
