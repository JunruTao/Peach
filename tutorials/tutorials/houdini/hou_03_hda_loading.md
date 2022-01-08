# HDA Loading

### Loading Example:

```python
import hou

# This code is the equivalent of running Assets -> Install Asset Library
hou.hda.installFile('path_to_your_hda_file_on_disk')

# Then you could create the HDA as you would normally with any other node
hda_node = hou_parent.createNode("OperatorType”, “Name”) # Operator Type is your hda type
```

> reference:
> - https://www.sidefx.com/forum/topic/68915/
> - https://www.sidefx.com/docs/houdini/hom/hou/hda.html