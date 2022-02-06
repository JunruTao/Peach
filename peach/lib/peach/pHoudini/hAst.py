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
# [ File Name ] hAst.py@python
# [ File Description ] - 2022.02.05 (Y.M.D) - 17:24
#                            *   *   *   *
#
#   This script contains houdini Ast functions
#
# ---------------------------------------------------------------------
from peach import pImp, pAst, pDir, pUtil
pImp.reload(pAst, pDir, pUtil)


def export_layout(node_out=None, json_path=""):
    if node_out and json_path:
        if json_path.endswith(".json"):
            json_path = json_path.replace(".json", ".{}".format(pAst.LAY_EXT))
        geo = node_out.geometry()

        def chunks(lst, n):
            """Yield successive n-sized chunks from lst."""
            for j in range(0, len(lst), n):
                yield lst[j:j + n]

        ast_instance_data = geo.attribValue("ast_instance_data")
        data_out = dict()
        for ln, path_ in ast_instance_data.items():
            data_out[ln] = dict()
            data_out[ln]["path"] = path_
            data_out[ln]["instances"] = []

        # getting all the transforms:
        t = geo.primFloatAttribValues("t")
        r = geo.primFloatAttribValues("r")
        s = geo.primFloatAttribValues("s")
        asset_name = geo.primStringAttribValues("ast_longname")

        # get them into 3 sized vector arrays
        t = list(chunks(t, 3))
        r = list(chunks(r, 3))
        s = list(chunks(s, 3))

        for i in range(0, len(geo.prims())):
            if data_out.get(asset_name[i]):
                data = {"order": "trs",
                        "t": (t[i][0], t[i][1], t[i][2]),
                        "r": (r[i][0], r[i][1], r[i][2]),
                        "s": (s[i][0], s[i][1], s[i][2])}
                data_out[asset_name[i]]["instances"].append(data)

        import json
        json_str = json.dumps(data_out, indent=4)
        with open(json_path, 'w') as outfile:
            outfile.write(json_str)


_init_script_src = """#!/usr/bin/env python
import subprocess
subprocess.run(["{blender_exe}", 
                "-con", 
                "--debug-python", 
                "--python", 
                "{cmd_script}"])
"""

_init_script_bg_src = """#!/usr/bin/env python
import subprocess
subprocess.run(["{blender_exe}", 
                "--background", 
                "--python", 
                "{cmd_script}"])
"""


_init_cmd_src = """#!/usr/bin/env python
import bpy
import sys
sys.path.append("{python_lib_dir}")
try:
    import peach
except ImportError as e:
    raise e
finally:
    from peach import pLog
    pLog.message("import <peach> Module SUCCESS..", fn="Import", cls="pBlender")
from peach.pBlender import pbu
# /.load peach addons.
pbu.register_addons()
# /.remove everything in the scene.
pbu.purge_scene()
bpy.ops.wm.save_as_mainfile(filepath="{blend_file}")
bpy.ops.import_scene.fbx(filepath="{fbx_file}")
loaded = bpy.context.scene.objects.items()[0][1]
grp = bpy.data.collections.new("MDL")
bpy.context.scene.collection.children.link(grp)
grp.objects.link(loaded)
layer_collection = bpy.context.view_layer.layer_collection.children["MDL"]
bpy.context.view_layer.active_layer_collection = layer_collection
bpy.ops.peach.asset_prep_name()
bpy.data.scenes['Scene'].collection.objects.unlink(bpy.context.scene.objects.items()[0][1])
bpy.ops.wm.save_mainfile(filepath="{blend_file}")
"""


def hou_script_pub_cache_dir():
    """
    [ Asset (Beta) ] get script cache dir
    @return: (str) script_cache dir
    """
    return pDir.join(pAst.cwd(), "script_cache")


def hou_publish_init_script_dir():
    """
    [ Asset (Beta) ] get init script dir
    @return: (str) scripts' dirs
    """
    script_cache_dir = hou_script_pub_cache_dir()
    init_script_path = pDir.join(script_cache_dir, "htb_init.py")
    init_cmd_script_path = pDir.join(script_cache_dir, "bln_import_cmds.py")
    return init_script_path, init_cmd_script_path


def hou_run_publish_script(asset_path="", bg=False):
    """
    [ Asset (Beta) ] Output file and run scripts:
    @param asset_path: (str) asset path to be published
    @param bg: (bool) running in background
    """
    if asset_path:
        script_cache_dir = hou_script_pub_cache_dir()
        if not pDir.exists(script_cache_dir):
            pDir.mkdir(script_cache_dir)

        init_script_path, init_cmd_script_path = hou_publish_init_script_dir()
        # /. remove cached file
        if pDir.isFile(init_script_path):
            pDir.rm_rf(init_script_path)
        if pDir.isFile(init_cmd_script_path):
            pDir.rm_rf(init_cmd_script_path)

        out_str = _init_script_src
        if bg:
            out_str = _init_script_bg_src

        # /.Init script
        out_str = out_str.format(blender_exe=pDir.getBlenderExeDir(),
                                 cmd_script=init_cmd_script_path)
        pUtil.file_write(init_script_path, out_str)

        # /.Cmd script
        out_str = _init_cmd_src.format(python_lib_dir=pDir.getPeachBlendLibDir(),
                                       fbx_file=asset_path.replace("$<EXT>", "fbx"),
                                       blend_file=asset_path.replace("$<EXT>", "blend"),
                                       )
        pUtil.file_write(init_cmd_script_path, out_str)
