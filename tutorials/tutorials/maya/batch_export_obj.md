# Batch Export Obj

```python
from maya import cmds
import os

# folder name should use '/' forslash or `\\` double back slash
export_folder = "C:/Users/1/Desktop" # replace this with your folder

sel = cmds.ls(sl=True, l=True)
if len(sel):
    objects_names = []
    for obj in sel:
        objects_names.append(str(obj)[1:].replace("|", "_") + ".obj")
        
    print(objects_names)
    for i in range(0, len(sel)):
        cmds.select(sel[i])
        file_path = os.path.join(export_folder, objects_names[i])
        cmds.file(file_path,pr=1,typ="OBJexport",es=1,op="groups=0; ptgroups=0; materials=0; smoothing=0; normals=0")
else:
    print("Nothing is selected")

```