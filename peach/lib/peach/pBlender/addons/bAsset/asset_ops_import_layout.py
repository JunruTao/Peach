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
# [ File Name ] asset_ops_import_layout.py@python
# [ File Description ] - 2022.02.05 (Y.M.D) - 21:40
#                            *   *   *   *
#
#   This script contains layout data import operator class
#
# ---------------------------------------------------------------------
import json
import bpy
import mathutils
import math
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from peach import pDir, pUtil, pImp, pLog, pAst
from peach.pBlender import pbu
pImp.reload(pUtil, pDir, pLog, pbu)


def fn_load_layout(context, filepath, use_some_setting):
    pLog.message("running Peach::B::Load Layout", fn=fn_load_layout, cls="Peach")
    # loading json
    json_file_dir = filepath
    json_file_name = pDir.fileNameBare(json_file_dir)
    with open(json_file_dir, 'r', encoding='utf-8') as json_file:
        layout_data = json.load(json_file)
        if not layout_data:
            json_file.close()
            pLog.error("json data is not loaded", e=RuntimeError)
        json_file.close()

    # /.Add Layout group to the scene
    layout_name = "LAY_{}_GRP".format(json_file_name)
    if bpy.data.collections.find(layout_name) < 0:
        layout_clt = bpy.data.collections.new(layout_name)
        bpy.context.scene.collection.children.link(layout_clt)
    else:
        layout_clt = bpy.data.collections.get(layout_name)
        for obj_ in layout_clt.all_objects.items():
            bpy.data.objects.remove(obj_[1])

    # /.set to scene collections as active collection
    layer_collection = bpy.context.view_layer.layer_collection
    bpy.context.view_layer.active_layer_collection = layer_collection

    # /.Adding A master transform.
    mst_name = "MASTER_TRANSFORM_{}_EPT".format(json_file_name)
    transform_ctr_ETP = bpy.data.objects.new("empty", None)
    transform_ctr_ETP.name = mst_name
    transform_ctr_ETP.empty_display_type = 'ARROWS'
    transform_ctr_ETP.show_name = True
    layout_clt.objects.link(transform_ctr_ETP)

    # /.Create the main group for file instances
    linked_clt_name = "instance_geo_GRP"
    if bpy.data.collections.find(linked_clt_name) < 0:
        # /..the group does not exist
        linked_clt = bpy.data.collections.new(linked_clt_name)
        bpy.context.scene.collection.children.link(linked_clt)
    else:
        # /..the group has been created
        linked_clt = bpy.data.collections.get(linked_clt_name)

    for key, data in layout_data.items():
        f = data["path"]
        f_name = pDir.fileName(f)
        to_link = True
        if pDir.exists(f):
            # /. Found Existing Collections in Data
            if linked_clt.children.find(key) != -1:
                for lib_item in bpy.data.libraries.items():
                    file_bare = f_name.split(".")[0]
                    if file_bare in lib_item[0]:
                        if f_name != lib_item[0]:
                            # /.in the scene has an older version
                            to_link = True
                            bpy.data.collections.remove(bpy.data.collections.get(key))
                            pLog.message(lib_item[0], fn="Remove Other Versions", cls="Peach.pBlender")
                            bpy.data.libraries.remove(lib_item[1])
                        else:
                            # /.in the scene and latest.
                            to_link = False
                            pLog.message(lib_item[0], fn="ReloadLib", cls="Peach.pBlender")
                            lib_item[1].reload()
                        break

            if to_link:
                # /..link files
                bpy.ops.wm.link(
                        filepath=f,
                        directory=f + "\\Collection\\",  # this is hard coded blender standard
                        filename=key)
                pLog.message(f_name, fn="LinkFile", cls="Peach.pBlender")

                # /..remove linked from scene
                if bpy.context.scene.collection.objects.find(key) >= 0:
                    # /..this is the first create.
                    bpy.context.scene.collection.objects.unlink(bpy.data.objects[key])

                co_data = bpy.data.collections[key]
                linked_clt.children.link(co_data)
            else:
                co_data = linked_clt.children.get(key)

            counter = 0
            for items in data["instances"]:
                counter += 1
                ins_EPT = bpy.data.objects.new("empty", None)
                ins_EPT.name = "INS_{0}_id{1:03d}".format(key, counter)
                layout_clt.objects.link(ins_EPT)
                t = list(items['t'])
                r = list(items['r'])
                s = list(items['s'])

                r[0] -= 90
                s = pUtil.y_to_z_up_s(*s)
                c = 0
                for rv in r:
                    r[c] = math.radians(rv)
                    c += 1

                ins_EPT.location = mathutils.Vector(tuple(t))
                ins_EPT.rotation_euler = mathutils.Euler(tuple(r), 'XYZ')
                ins_EPT.scale = mathutils.Vector(tuple(s))
                ins_EPT.instance_type = 'COLLECTION'
                ins_EPT.instance_collection = co_data
                ins_EPT.parent = transform_ctr_ETP
                ins_EPT.matrix_parent_inverse = transform_ctr_ETP.matrix_world.inverted()
                ins_EPT.empty_display_size = 0.0001
                ins_EPT.hide_select = True

    # /.Rotate the master transform to get the right axis.
    transform_ctr_ETP.rotation_euler = mathutils.Euler((math.pi/2, 0, 0), 'XYZ')
    pbu.deselect_all()
    pbu.select(transform_ctr_ETP)
    pbu.apt_A()
    # /.put the geo container at the bottom of the outliner
    bpy.context.scene.collection.children.unlink(linked_clt)
    bpy.context.scene.collection.children.link(linked_clt)
    # /..make the instance group inviable from render
    bpy.context.layer_collection.children[linked_clt_name].exclude = True
    return {'FINISHED'}


class PbOpImportLayout(Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "peach.read_layout"
    bl_label = "Load Layout Data"

    # ImportHelper mixin class uses this
    filename_ext = ".{}".format(pAst.LAY_EXT)

    filter_glob: StringProperty(
        default="*.playout",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="Example Boolean",
        description="Example Tooltip",
        default=True,
    )

    type: EnumProperty(
        name="Example Enum",
        description="Choose between two items",
        items=(
            ('OPT_A', "First Option", "Description one"),
            ('OPT_B', "Second Option", "Description two"),
        ),
        default='OPT_A',
    )

    def execute(self, context):
        return fn_load_layout(context, self.filepath, self.use_setting)
