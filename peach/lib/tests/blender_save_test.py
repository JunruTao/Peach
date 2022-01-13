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
# [ File Name ] blender_save_test.py@python
# [ File Description ] - 2022.01.13 (Y.M.D) - 18:09
#                            *   *   *   *
#
#   This script contains
#
# ---------------------------------------------------------------------
import bpy

#  .sh
# /c/Program\ Files/Blender\ Foundation/Blender\ 3.0/blender-launcher.exe --background --python ./blender_save_test.py
print("hello world")
for obj in bpy.context.selectable_objects:
    print(obj)
    bpy.data.objects.remove(obj)

bpy.ops.import_scene.fbx(filepath="E:/test.fbx")
bpy.ops.wm.save_as_mainfile(filepath="E:/test.blend")
