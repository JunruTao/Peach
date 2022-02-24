# Flip normal if scale is negative

```py
import bpy

C = bpy.context
scn = bpy.context.scene
for key, obj in C.collection.objects.items():
    if obj.scale[1] < 0:
        print("test")
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.flip_normals() # just flip normals
        bpy.ops.object.mode_set()
```