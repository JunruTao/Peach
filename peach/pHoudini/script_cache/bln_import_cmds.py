#!/usr/bin/env python
import bpy
import sys
sys.path.append("E:/dev/peach_dev/peach/lib")
try:
    import peach
except ImportError as e:
    raise e
finally:
    from peach import pLog
    pLog.message("import <peach> Module SUCCESS..", fn="Import", cls="pBlender")
from peach.pBlender import pbu
from peach import pDir
# /.load peach addons.
pbu.register_addons()
# /.remove everything in the scene.
pbu.purge_scene()
bpy.ops.wm.save_as_mainfile(filepath="E:/dev/peach_dev_projects/ACPS/scene/dev_houdini/pData/extentions/extention/PEXT_extention.v001.blend")
bpy.ops.import_scene.fbx(filepath="E:/dev/peach_dev_projects/ACPS/scene/dev_houdini/pData/extentions/extention/PEXT_extention.v001.fbx")
loaded = bpy.context.scene.objects.items()[0][1]
name_ = pDir.fileNameBare("E:/dev/peach_dev_projects/ACPS/scene/dev_houdini/pData/extentions/extention/PEXT_extention.v001.fbx")
grp = bpy.data.collections.new("EXT_%s_GRP" % name_)
bpy.context.scene.collection.children.link(grp)
grp.objects.link(loaded)
bpy.data.scenes['Scene'].collection.objects.unlink(bpy.context.scene.objects.items()[0][1])
bpy.ops.wm.save_mainfile(filepath="E:/dev/peach_dev_projects/ACPS/scene/dev_houdini/pData/extentions/extention/PEXT_extention.v001.blend")
