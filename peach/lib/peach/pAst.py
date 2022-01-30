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
# [ File Name ] pAst.py@python
# [ File Description ] - 2022.01.30 (Y.M.D) - 03:12
#                            *   *   *   *
#
#   This script contains peach Asset Management functions
#
# ---------------------------------------------------------------------
from peach import pImp, pDir, pGlob, pLog, pUtil
pImp.reload(pDir, pGlob, pLog, pUtil)


WORKING_DIR = ""


def set_workdir(wd=""):
    """
    [ Asset ] Set current working directory
    @param wd:
    """
    global WORKING_DIR
    WORKING_DIR = wd


def get_categories():
    """
    [ Asset ] Get Library Categories
    @return: (dict) cat_name: cat_path
    """
    _lib = pDir.getUserLibDir(WORKING_DIR)
    cats = [d for d in pDir.listdir(_lib) if pDir.exists(pDir.join(d, "__cat__"))]
    _dict = dict()
    for c in cats:
        _dict[pDir.fileName(c)] = c
    return _dict


def get_types(cat=""):
    """
    [ Asset ] Get Types in specified category
    @param cat: (str) category name
    @return: (dict) type_name: type_path
    """
    cat_d = get_categories().get(cat)
    _dict = dict()
    if cat_d:
        tps = [d for d in pDir.listdir(cat_d) if pDir.exists(pDir.join(d, "__type__"))]
        for t in tps:
            _dict[pDir.fileName(t)] = t
    return _dict


def get_assets(cat="", tp=""):
    """
    [ Asset ] Get Types in specified category
    @param cat: (str) category name
    @param tp: (str) type name
    @return: (dict) asset_name: asset_folder_path
    """
    _dict = dict()
    tp_d = get_types(cat).get(tp)
    if tp_d:
        asts = [d for d in pDir.listdir(tp_d) if pDir.exists(pDir.join(d, "__ast__"))]
        for a in asts:
            _dict[pDir.fileName(a)] = a
    return _dict
