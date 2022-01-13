# Run Blender headlessly

use the following command in shell:
```bash
eval "/c/Program\ Files/Blender\ Foundation/Blender\ 3.0/blender.exe --background --python \"./blender_save_test.py\""
```

key point:
- `--background`
- `--python "<path_to_pythonfile>"`

combined:

`blender --background --python "<path_to_pythonfile>"`