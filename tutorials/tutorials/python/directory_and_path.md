# Directory and Path

### 1. Create a directory if it does not exist?

[1]
```python
import os
if not os.path.exists('my_folder'):
    os.makedirs('my_folder')

# You can also use the python idiom EAFP: 
# Easier to ask for forgiveness than permission.
import os
try:
    os.makedirs('my_folder')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
```
[2] 
```python
# On Python ≥ 3.5, use pathlib.Path.mkdir:

from pathlib import Path
Path("/my/directory").mkdir(parents=True, exist_ok=True)
```
> references:
> 1. https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
> 2. https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

<br><br>
### 2. Get all sub-directories

```python
import os
list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
```

> references:
> 1. https://stackoverflow.com/questions/800197/how-to-get-all-of-the-immediate-subdirectories-in-python