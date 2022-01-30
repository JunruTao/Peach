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
#   [README]:
#   peach asset pipe v1 follows template:
#
#   < $LIB/$CAT/$TYPE/$ASSET_$VARIANTS/$ASSET_$VARIANTS_$STEP_$STEP-VAR.Version >
#
#       + library/__lib__ (type:project, type:user_lib)
#       +-- categories/__cat__ (prefix:nickname i.g.BPS for building_parts)
#       +---- type/__type__ ---> ./addon, ./wall, ./windows (short as possible)
#       +------ asset/__ast__ ---> asset name as `wallAcUnit_A` <- A is variant
#       +-------- step_lvl/__stp__ ---> files:
#             *====[ wallAcUnit_A_MDL_A.v001 ] * .blend, .fbx(mid), .bgeo (static)
#             *====[ wallAcUnit_A_MDL_A.v002 ] .blend
#             *====[ wallAcUnit_A_MDL_B.v001 ] .blend (only different in shading)
#             *====[ wallAcUnit_A_ANM_A.v001 ] .blend (different in motion)
#             *====[ wallAcUnit_A_ANM_B.v001 ] .blend (different in motion, ...)
#
#
# ---------------------------------------------------------------------
from peach import pImp, pDir, pGlob, pLog, pUtil
pImp.reload(pDir, pGlob, pLog, pUtil)


WORKING_DIR = ""


def set_workdir(wd=""):
    """
    [ Asset ] Set current working directory
    @param wd: (str) working directory
    """
    global WORKING_DIR
    WORKING_DIR = str(wd)


def get_lib_path():
    """
    [ Asset ] Get Library path
    @return: (str) library file path
    """
    return pDir.getUserLibDir(WORKING_DIR)


def get_lib_type():
    """
    [ Asset ] Get Library type:
    <br>TODO: this function should implement in a dictionary level.
    <br> in lib_path/__lib__ file should contain i.g. <code>type:project</code> data
    @return: (str) library type
    """
    data_ = pUtil.read_keys(pDir.join(get_lib_path(), "__lib__"), ":")
    type_ = data_.get("type")
    if type_:
        return type_
    pLog.warning("Can not find any information in __lib__ file", cls="pAst")
    return ""


def get_categories():
    """
    [ Asset ] Get Library Categories
    @return: (dict) cat_name: cat_path
    """
    _lib = get_lib_path()
    cats = [d for d in pDir.listdir(_lib) if pDir.exists(pDir.join(d, "__cat__"))]
    _dict = dict()
    for c in cats:
        _dict[pDir.fileName(c)] = c
    return _dict


def get_cat_prefix(cat=""):
    """
    [ Asset ] Get Library Categories
    @param cat: (str) cat_name
    @return: (str) prefix of category
    """
    cat_d = get_categories().get(cat)
    if cat_d:
        cat_d = pDir.join(cat_d, "__cat__")
        data_ = pUtil.read_keys(cat_d, ":")
        prf_ = data_.get("prefix")
        if prf_:
            return prf_
    pLog.warning("Can not find any information in __cat__ file", cls="CatPrefix", fn=cat)
    return ""


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


def resolve(wd=""):
    """
    [ Asset ] resolve all the information from current working directory
    @param wd: (str) working directory
    @return: (dict) data
    """
    if wd:
        set_workdir(wd)
    lib_dir = get_lib_path()
    data = dict()
    if lib_dir in WORKING_DIR:
        # /.it's currently working on an asset.
        # todo: should store in +class or global variable.
        pass
