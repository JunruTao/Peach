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
# [ File Name ] wgt.py@python
# [ File Description ] - 2022.01.22 (Y.M.D) - 01:22
#                            *   *   *   *
#
#   This script contains Qt Widget related functions
#   TODO: Doc strings and doc
#
# ---------------------------------------------------------------------
from peach.pQt.qHotel import QtWidgets, QtCore, QtGui
from peach.pQt import img, style
from peach import pImp, pIco
pImp.reload(pIco, img, style)


def getHeaderTemplateWidget(**kwargs):
    """
    [ Get Header Widget ]
    @param kwargs: settings
    @return: (QWidget) constructed widget
    """
    wgt_main = QtWidgets.QWidget()
    for key, value in kwargs.items():
        if key == "type":
            if value == "dev_tool":
                # /.get values
                ttl = kwargs["title"]
                height = kwargs["height"]
                font_size = kwargs["font_size"]

                layout = QtWidgets.QHBoxLayout()
                # /. Create Icon
                lbl_icon = QtWidgets.QLabel()
                logo = img.getPixmap(pIco.DPS.whiteTextColorIco256())
                lbl_icon.setPixmap(logo.scaledToHeight(height, QtCore.Qt.SmoothTransformation))
                layout.addWidget(lbl_icon)
                # /. Create Label
                lbl_title = QtWidgets.QLabel(ttl)
                s_sheet = style.Sheet(lbl_title)
                s_sheet.setTextColor(1.0)
                s_sheet.setFont(style.fnt_STHupo, font_size)
                s_sheet.assign(lbl_title)
                layout.addWidget(lbl_title)
                # /. Layout
                layout.setSpacing(0)
                wgt_main.setLayout(layout)
                wgt_main.setContentsMargins(0, 0, 0, 0)

            if value == "peach_main":
                pass
    return wgt_main
