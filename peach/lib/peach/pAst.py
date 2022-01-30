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

# [ Asset ] Global Data Containers
_WORKING_DIR = ""
_LIBS_CONTAINER = dict()

_cw_lvl = ""    # current working level i.g. __lib__
_cw_ast = None  # current asset
_cw_typ = None  # current type
_cw_cat = None  # current cat
_cw_lib = None  # current lib

# [ Asset ] Identifier names
__LIB__ = pGlob.PEACH_GLOBAL_ASSET_LIB_ID
__CAT__ = "__cat__"
__TYP__ = "__type__"
__AST__ = "__ast__"


class Struct(object):
    def __init__(self, name="", path="", parent=None):
        self._name = name
        self._path = path
        self._parent = parent
        self._items = dict()

    def replaceItemData(self, data=None):
        if isinstance(data, dict):
            self._items = data

    def updateItemData(self, data=None):
        if isinstance(data, dict):
            self._items.update(data.copy())

    def addItem(self, key="", st_item=None):
        if isinstance(st_item, Struct):
            self._items[key] = st_item

    def name(self):
        return self._name

    def path(self):
        return self._path

    def parent(self):
        return self._parent

    def children_dict(self):
        return self._items

    def children(self):
        return list(self._items.values())


class Lib(Struct):
    def __init__(self, name="library"):
        super(Lib, self).__init__(name, _get_lib_path(), None)
        self._lib_type = _get_lib_type()
        # /.construct library
        for key, path in _get_categories().items():
            self.addItem(key, Cat(key, path, self))

    def libType(self):
        return self._lib_type

    def set_name(self, n=""):
        self._name = n


class Cat(Struct):
    def __init__(self, name="", path="", parent=None):
        super(Cat, self).__init__(name, path, parent)
        self._prefix = _get_cat_prefix(self._name)
        # /.construct types:
        for key, path in _get_types(self._name).items():
            self.addItem(key, Typ(key, path, self))

    def prefix(self):
        return self._prefix


class Typ(Struct):
    def __init__(self, name="", path="", parent=None):
        super(Typ, self).__init__(name, path, parent)
        # /.construct types:
        for key, path in _get_assets(self.parent().name(), self._name).items():
            self.addItem(key, Ast(key, path, self))


class Ast(Struct):
    def __init__(self, name="", path="", parent=None):
        super(Ast, self).__init__(name, path, parent)
        self._base_name, self._variant = tuple(name.split("_"))


def init_lib(wd=""):
    """
    [ Asset ] Initialize Current Lib object
    @param wd: (str) working dir
    """
    global _LIBS_CONTAINER, _cw_lib
    set_wd(wd)
    _cw_lib = Lib()
    _cw_lib.set_name("{}_library".format(_cw_lib.libType()))
    _LIBS_CONTAINER["current"] = _cw_lib


def get_libs():
    """
    [ Asset ] Get Libs
    @return: (dict) dict of registered  peach.pAst.Lib object instances
    """
    return _LIBS_CONTAINER


def set_wd(wd=""):
    """
    [ Asset ] Set current working directory
    @param wd: (str) working directory
    """
    global _WORKING_DIR
    _WORKING_DIR = pDir.pathSlashConvert(str(wd))


def cwd():
    """
    [ Asset ] Get Current working directory
    @return: (str) wd
    """
    return _WORKING_DIR


def _get_lib_path():
    """
    [ Asset ] Get Library path
    @return: (str) library file path
    """
    return pDir.getUserLibDir(_WORKING_DIR)


def _get_lib_type():
    """
    [ Asset ] Get Library type:
    <br> in lib_path/__lib__ file should contain i.g. <code>type:project</code> data
    @return: (str) library type
    """
    data_ = pUtil.read_keys(pDir.join(_get_lib_path(), __LIB__), ":")
    type_ = data_.get("type")
    if type_:
        return type_
    pLog.warning("Can not find any information in __lib__ file", cls="pAst")
    return ""


def _get_categories():
    """
    [ Asset ] Get Library Categories
    @return: (dict) cat_name: cat_path
    """
    _lib = _get_lib_path()
    cats = [d for d in pDir.listdir(_lib) if pDir.exists(pDir.join(d, __CAT__))]
    _dict = dict()
    for c in cats:
        _dict[pDir.fileName(c)] = c
    return _dict


def _get_cat_prefix(cat=""):
    """
    [ Asset ] Get Library Categories
    @param cat: (str) cat_name
    @return: (str) prefix of category
    """
    cat_d = _get_categories().get(cat)
    if cat_d:
        cat_d = pDir.join(cat_d, __CAT__)
        data_ = pUtil.read_keys(cat_d, ":")
        prf_ = data_.get("prefix")
        if prf_:
            return prf_
    pLog.warning("Can not find any information in __cat__ file", cls="CatPrefix", fn=cat)
    return ""


def _get_types(cat=""):
    """
    [ Asset ] Get Types in specified category
    @param cat: (str) category name
    @return: (dict) type_name: type_path
    """
    cat_d = _get_categories().get(cat)
    _dict = dict()
    if cat_d:
        tps = [d for d in pDir.listdir(cat_d) if pDir.exists(pDir.join(d, __TYP__))]
        for t in tps:
            _dict[pDir.fileName(t)] = t
    return _dict


def _get_assets(cat="", tp=""):
    """
    [ Asset ] Get Types in specified category
    @param cat: (str) category name
    @param tp: (str) type name
    @return: (dict) asset_name: asset_folder_path
    """
    _dict = dict()
    tp_d = _get_types(cat).get(tp)
    if tp_d:
        asts = [d for d in pDir.listdir(tp_d) if pDir.exists(pDir.join(d, __AST__))]
        for a in asts:
            _dict[pDir.fileName(a)] = a
    return _dict


def resolve(wd="", ):
    """
    [ Asset ] resolve all the information from current working directory
    @param wd: (str) working directory
    @return: (dict) data
    """
    if _LIBS_CONTAINER or _cw_lib:
        # /. already resolved.
        return -1
    if _WORKING_DIR:
        wd = _WORKING_DIR
    init_lib(wd)

    # /. resolving
    global _cw_lvl, _cw_cat, _cw_typ, _cw_ast
    if isinstance(_cw_lib, Lib):
        for cat_ in _cw_lib.children():
            if cat_.path() in cwd():
                _cw_cat = cat_
                for typ_ in _cw_cat.children():
                    if typ_.path() in cwd():
                        _cw_typ = typ_
                        for ast_ in _cw_typ.children():
                            if ast_.path() in cwd():
                                _cw_ast = ast_
                                _cw_lvl = __AST__
                                return 3
                        _cw_lvl = __TYP__
                        return 2
                _cw_lvl = __CAT__
                return 1
        _cw_lvl = __LIB__
        return 0


def reset():
    """
    [ Asset ] Clear Local Data (rest)
    """
    global _cw_lvl, _cw_lib, _cw_cat, _cw_typ, _cw_ast, _WORKING_DIR, _LIBS_CONTAINER
    _cw_lvl = ""
    _cw_lib = None
    _cw_cat = None
    _cw_typ = None
    _cw_ast = None
    _WORKING_DIR = ""
    _LIBS_CONTAINER = dict()


def assets():
    """
    [ Asset ] Get Registered asset objects
    @return:
    """
    _ASSET_CONTAINER = []
    if isinstance(_cw_lib, Lib):
        for cat in _cw_lib.children():
            for typ in cat.children():
                for ast in typ.children():
                    _ASSET_CONTAINER.append(ast)
    return _ASSET_CONTAINER


def cwl():
    """
    [ Asset ] get Current Working Level
    @return: (str) level identifier
    """
    return _cw_lvl


def current_lib():
    """
    [ Asset ] get Current working Lib
    @return: (peach.pAst.Lib) object instance
    """
    return _cw_lib


def current_cat():
    """
    [ Asset ] get Current working Category
    @return: (peach.pAst.Cat) object instance
    """
    return _cw_cat


def current_type():
    """
    [ Asset ] get Current working Type
    @return: (peach.pAst.Typ) object instance
    """
    return _cw_typ


def current_asset():
    """
    [ Asset ] get Current working Asset
    @return: (peach.pAst.Ast) object instance
    """
    return _cw_ast
