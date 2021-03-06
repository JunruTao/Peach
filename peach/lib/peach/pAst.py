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
#       +-------- variant/__vrt__  A, B, C...
#       +------------ step/MDL_A, ANM_AxA ... ---> files: Todo:
#
#       ../wallAcUnit_A
#        __ast__
#             ./ A
#             __vrt__
#             *====[ wallAcUnit_A_MDL_A.v001 ] * .blend, .fbx(mid), .bgeo (static)
#             *====[ wallAcUnit_A_MDL_A.v002 ] .blend
#             *====[ wallAcUnit_A_ANM_AxA.v001 ] .blend (different in motion)
#             ./ B
#             __vrt__
#             *====[ wallAcUnit_A_MDL_B.v001 ] .blend (only different in shading)
#             *====[ wallAcUnit_A_ANM_BxA.v001 ] .blend (different in motion, ...)
#             *====[ wallAcUnit_A_ANM_BxB.v001 ] .blend (different in motion, ...)
#      ../wallAcUnit_B
#        __ast__
#             ./ A
#             __vrt__
#             *====[ wallAcUnit_B_MDL_A.v001 ] *
#             *====[ wallAcUnit_B_MDL_A.v002 ] *
#             ./ B
#             __vrt__
#             *====[ wallAcUnit_B_MDL_B.v001 ] *
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
__VRT__ = "__vrt__"

# [ Asset ] Templates:
_MDL_t = "{ast}_MDL_{var}"
_ANM_t = "{ast}_ANM_{var}"
_VER_t = ".v{0:03d}"
ABCDs = pGlob.ALPHA

LAY_EXT = "playout"


# [ Asset ]: OBJECTS ------------------------------------------
class Struct(object):
    def __init__(self, name="", path="", parent=None):
        self._name = name
        self._path = path
        self._parent = parent
        self._items = dict()
        self._id_key = ""
        self._id_key_child = ""

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

    def get(self, key=""):
        return self._items.get(key)

    def children(self):
        return list(self._items.values())

    def has_children(self):
        return len(self._items) > 0

    def id_key(self):
        return self._id_key

    def id_key_child(self):
        return self._id_key_child

    def _new_child(self, name="", extra_data=""):
        if not self._id_key_child:
            pLog.warning("Can not create new child: this object has no id_key_child",
                         fn=self._new_child, cls=self)
            return ""
        if not name:
            pLog.warning("Can not create new child: Please specify a name",
                         fn=self._new_child, cls=self)
            return ""
        if self._items.get(name):
            pLog.warning("Can not create new child: it already has a child with the same name",
                         fn=self._new_child, cls=self)
            return ""
        child_path = pDir.mkdir(pDir.join(self._path, name))
        pUtil.file_write(pDir.join(child_path, self._id_key_child), extra_data)
        return child_path
    
    def _pop_child(self, key=""):
        self._items.pop(key)

    @staticmethod
    def _standard_name(name=""):
        return pUtil.format_split_with_underscore(name)

    def deletable(self):
        dir_items = pDir.ls(self._path)
        if len(dir_items) == 1:
            if dir_items[0].endswith(self._id_key):
                return True
        return False

    def delete(self):
        if self.deletable():
            result = pDir.rm_rf(self._path)
            if result:
                if isinstance(self._parent, Struct):
                    self._parent._pop_child(self._name)
            return result
        return False


class Lib(Struct):
    def __init__(self, name="library"):
        super(Lib, self).__init__(name, _get_lib_path(), None)
        self._lib_type = _get_lib_type()
        self._id_key = __LIB__
        self._id_key_child = __CAT__
        # /.construct library
        for key, path in _get_categories().items():
            self.addItem(key, Cat(key, path, self))

    def libType(self):
        return self._lib_type

    def set_name(self, n=""):
        self._name = self._standard_name(n)

    def new_cat(self, ch_name="", cat_codename=""):
        ch_name = self._standard_name(ch_name)
        cat_codename = cat_codename if cat_codename else ch_name
        ch_dir = self._new_child(ch_name, _cat_data_prefix(cat_codename))
        if ch_dir:
            _out = Cat(ch_name, ch_dir, self)
            self.addItem(ch_name, _out)
            return _out
        return None


class Cat(Struct):
    def __init__(self, name="", path="", parent=None):
        super(Cat, self).__init__(name, path, parent)
        self._prefix = _get_cat_prefix(self._name)
        self._id_key = __CAT__
        self._id_key_child = __TYP__
        # /.construct types:
        for key, path in _get_types(self._name).items():
            self.addItem(key, Typ(key, path, self))

    def prefix(self):
        return self._prefix

    def new_type(self, ch_name=""):
        # /.TypesShouldUseCamelCase
        ch_name = pUtil.format_CamelCase(ch_name)
        ch_dir = self._new_child(ch_name)
        if ch_dir:
            _out = Typ(ch_name, ch_dir, self)
            self.addItem(ch_name, _out)
            return _out
        return None


class Typ(Struct):
    def __init__(self, name="", path="", parent=None):
        super(Typ, self).__init__(name, path, parent)
        self._id_key = __TYP__
        self._id_key_child = __AST__
        # /.construct types:
        for key, path in _get_assets(self.parent().name(), self._name).items():
            self.addItem(key, Ast(key, path, self))

    def new_asset(self, ch_name=""):
        counter = 0
        base_name = pUtil.format_camelCase(ch_name)

        # /.Lib data is an exception, i.g.textures, materials
        is_lib_data = False
        if self.parent().name().startswith("lib_"):
            is_lib_data = True

        if not is_lib_data:
            ch_name = "{}_{}".format(base_name, ABCDs[counter])
            while self.get(ch_name):
                ch_name = "{}_{}".format(base_name, ABCDs[counter])
                counter += 1

        ch_dir = self._new_child(ch_name)
        if ch_dir:
            _out = Ast(ch_name, ch_dir, self)
            if not is_lib_data:
                _out.new_step_variant()
            self.addItem(ch_name, _out)
            return _out
        return None


class Ast(Struct):
    def __init__(self, name="", path="", parent=None):
        super(Ast, self).__init__(name, path, parent)
        self._id_key = __AST__
        self._id_key_child = __VRT__
        self._base_name, self._suf = "", ""
        if not self.parent().parent().name().startswith("lib_"):
            self._base_name, self._suf = tuple(name.split("_"))
        for key, path in _get_variants(self.path()).items():
            self.addItem(key, Vrt(key, path, self))

    def base_name(self):
        return self._base_name

    def suffix_name(self):
        return self._suf

    def new_asset_variant(self):
        return self._parent.new_asset(self._base_name)

    def get_step_variant_names(self):
        return list(self.children_dict().keys())

    def new_step_variant(self):
        names = self.get_step_variant_names()
        counter = 0
        ch_name = ABCDs[counter]

        while ch_name in names:
            ch_name = ABCDs[counter]
            counter += 1

        ch_dir = self._new_child(ch_name)
        if ch_dir:
            _out = Vrt(ch_name, ch_dir, self)
            self.addItem(ch_name, _out)
            return _out
        return None


class Vrt(Struct):
    def __init__(self, name="", path="", parent=None):
        super(Vrt, self).__init__(name, path, parent)
        self._id_key = __VRT__
        self._mdl_tpl = _MDL_t.format(ast=self.parent().name(), var=self.name())
        self._anm_tpl = _ANM_t.format(ast=self.parent().name(), var=self.name())

    def valid(self):
        return len(self.mdl_versions()) > 0

    def mdl_versions(self):
        files = pDir.listfiles(self._path, n=True)
        vers = []
        if not files:
            return vers
        for f in files:
            base_n = pDir.remove_ext(f)
            # /.is MDL step
            if self._mdl_tpl in f:
                # /..Has both FBX and Blend Files (valid version)
                check_path = pDir.join(self._path, base_n)
                if pDir.isFile(check_path + ".fbx") and pDir.isFile(check_path + ".blend"):
                    vers.append(int(base_n.split(".v")[-1]))
        return list(set(vers))

    def mdl_latest_version(self):
        return max(self.mdl_versions() + [0, ])

    def mdl_latest_fbx(self):
        if self.mdl_versions():
            name = self._mdl_tpl + _VER_t.format(self.mdl_latest_version())
            path_ = pDir.join(self.path(), name + ".fbx")
            if pDir.exists(path_):
                return path_
        return ""

    def mdl_latest_blend(self):
        if self.mdl_versions():
            name = self._mdl_tpl + _VER_t.format(self.mdl_latest_version())
            path_ = pDir.join(self.path(), name + ".blend")
            if pDir.exists(path_):
                return path_
        return ""

    def anm_variants(self):
        files = pDir.listfiles(self._path, n=True)
        vats = []
        for f in files:
            if self._anm_tpl in f and f.endswith(".blend"):
                f = f.replace(self._anm_tpl, "")
                vats.append(pDir.remove_ext(f).split(".v")[0][-1])
        if vats:
            vats = list(set(vats))
            vats.sort()
        return vats

    def anm_variants_l(self):
        vats = []
        avs = self.anm_variants()
        if avs:
            for av in avs:
                vats.append("{}x{}".format(self.name(), av))
        return vats

    def anm_get_latest_blends(self):
        avs = self.anm_variants()
        avf = []
        files = pDir.listfiles(self._path)
        files.sort()
        for av in avs:
            av_filepath = pDir.join(self._path, "{}x{}".format(self._anm_tpl, av))
            vs_fs = [f for f in files if av_filepath in f]
            if len(vs_fs):
                avf.append(vs_fs[-1])
        return avf

    def form_new_filename_mdl_mE(self):
        return self._mdl_tpl + _VER_t.format(self.mdl_latest_version() + 1)

    def _object_name_pref(self):
        typ_ = self.parent().parent()
        cat_ = typ_.parent()
        typ_mf = typ_.name()
        cat_pf = cat_.prefix()
        return "{}_{}_".format(cat_pf, typ_mf)

    def get_object_name_mdl(self):
        prefix_ = self._object_name_pref()
        return prefix_ + self._mdl_tpl

    def get_object_name_anm(self, anim_var="A"):
        prefix_ = self._object_name_pref()
        return prefix_ + self._anm_tpl + "x" + anim_var

    def get_object_names_list_anm(self):
        name_list_ = []
        vrs = self.anm_variants()
        if vrs:
            for av in vrs:
                name_list_.append(self.get_object_name_anm(anim_var=av))
        return name_list_


# [ Asset ]: PROTECTED ------------------------------------------
def _init_lib(wd=""):
    """
    [ Asset ] Initialize Current Lib object
    @param wd: (str) working dir
    """
    global _LIBS_CONTAINER, _cw_lib
    set_wd(wd)
    _cw_lib = Lib()
    if _cw_lib.path():
        _cw_lib.set_name("{}_{}_library".format(pDir.parent(_cw_lib.path(), n=True),
                                                _cw_lib.libType()))
        _LIBS_CONTAINER["current"] = _cw_lib
    else:
        _cw_lib = None


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


def _cat_data_prefix(name=""):
    """
    [ Asset ] Create Cat prefix
    @param name: (str) prefix
    @return: (str) prefix formatted data
    """
    return "prefix : {}".format(name.upper())


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


def _get_variants(ast_dir=""):
    """
    [ Asset ] Get Asset Variants
    @param ast_dir: (str) asset filepath
    @return: (dict) variant: variant_folder_path
    """
    _dict = dict()
    vrt_list = [d for d in pDir.listdir(ast_dir) if pDir.exists(pDir.join(d, __VRT__))]
    for v in vrt_list:
        _dict[pDir.fileName(v)] = v
    return _dict


def resolve(wd="", ):
    """
    [ Asset ] resolve all the information from current working directory
    @param wd: (str) working directory
    @return: (dict) data
    """
    if len(_LIBS_CONTAINER.keys()) and _cw_lib:
        # /. already resolved.
        return -1
    if _WORKING_DIR:
        wd = _WORKING_DIR

    _init_lib(wd)
    if not _cw_lib:
        return -2
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


# [ Asset ]: API ------------------------------------------
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
    _LIBS_CONTAINER.clear()


def all_assets():
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


# [ Asset ]: LIBRARY ------------------------------------------
def is_lib():
    """
    [ Asset ] has working Lib
    @return: (bool)
    """
    return isinstance(_cw_lib, Lib)


def current_lib():
    """
    [ Asset ] get Current working Lib
    @return: (peach.pAst.Lib) object instance
    """
    return _cw_lib if isinstance(_cw_lib, Lib) else None


def current_lib_name():
    """
    [ Asset ] get Current working Lib name
    @return: (str) name
    """
    out = current_lib()
    return out.name() if out else ""


def current_lib_path():
    """
     [ Asset ] get Current working Library path
    @return:
    """
    out = current_lib()
    return out.path() if out else ""


# [ Asset ]: CATEGORY ------------------------------------------
def is_cat():
    """
    [ Asset ] has working Category
    @return: (bool)
    """
    return isinstance(_cw_cat, Cat)


def current_cat():
    """
    [ Asset ] get Current working Category
    @return: (peach.pAst.Cat) object instance
    """
    return _cw_cat if isinstance(_cw_cat, Cat) else None


def current_cat_name():
    """
    [ Asset ] get Current working Category name
    @return: (str) name
    """
    out = current_cat()
    return out.name() if out else ""


def current_cat_path():
    """
     [ Asset ] get Current working Category path
    @return:
    """
    out = current_cat()
    return out.path() if out else ""


# [ Asset ]: TYPE --------------------------------------------
def is_type():
    """
    [ Asset ] has working Type
    @return: (bool)
    """
    return isinstance(_cw_typ, Typ)


def current_type():
    """
    [ Asset ] get Current working Type
    @return: (peach.pAst.Typ) object instance
    """
    return _cw_typ if isinstance(_cw_typ, Typ) else None


def current_type_name():
    """
    [ Asset ] get Current working Type name
    @return: (str) name
    """
    out = current_type()
    return out.name() if out else ""


def current_type_path():
    """
     [ Asset ] get Current working Type path
    @return:
    """
    out = current_type()
    return out.path() if out else ""


# [ Asset ]: ASSET --------------------------------------------
def is_asset():
    """
    [ Asset ] has working Asset
    @return: (bool)
    """
    return isinstance(_cw_ast, Ast)


def current_asset():
    """
    [ Asset ] get Current working Asset
    @return: (peach.pAst.Ast) object instance
    """
    return _cw_ast if isinstance(_cw_ast, Ast) else None


def current_asset_name():
    """
    [ Asset ] get Current working Asset name
    @return: (str) name
    """
    out = current_asset()
    return out.name() if out else ""


def current_asset_path():
    """
     [ Asset ] get Current working Asset path
    @return:
    """
    out = current_asset()
    return out.path() if out else ""
