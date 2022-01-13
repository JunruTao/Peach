# Delete All Geometries

```python
import bpy

for obj in bpy.context.selectable_objects:
    print(obj)
    bpy.data.objects.remove(obj)
```