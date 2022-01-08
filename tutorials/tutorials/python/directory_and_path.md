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


<br><br>
### 3. Remove File, Directory and `rm -rf` in Python



- `os.remove()` removes a file.
- `os.rmdir()` removes an empty directory.
- `shutil.rmtree()` deletes a directory and all its contents.

> If the file doesn't exist, os.remove() throws an exception, so it may be necessary to check os.path.isfile() first, or wrap in a try. 

> reference:
> - https://stackoverflow.com/questions/6996603/how-to-delete-a-file-or-folder-in-python

<br><br>
### 4. File Copy
use `shutil`
```python
from shutil import copyfile
copyfile(src, dst)

# 2nd option
copy(src, dst)  # dst can be a folder; use copy2() to preserve timestamp

```



- Copy the contents of the file named `src` to a file named `dst`. Both `src` and `dst` need to be the entire filename of the files, including path.
- The destination location must be writable; otherwise, an IOError exception will be raised.
- If `dst` already exists, it will be replaced.
- Special files such as character or block devices and pipes cannot be copied with this function.
With copy, `src` and `dst` are path names given as strs.

Another shutil method to look at is shutil.copy2(). It's similar but preserves more metadata (e.g. time stamps).

If you use os.path operations, use copy rather than copyfile. copyfile will only accept strings.

| Function         | Copies<br>metadata | Copies<br>permissions | Uses file object | Destination<br>may be directory |
|------------------|-----------------|--------------------|------------------|------------------------------|
|[shutil.copy][1]       |   No            |    Yes             |    No            |      Yes                     |
|[shutil.copyfile][2]   |   No            |     No             |    No            |       No                     |
|[shutil.copy2][3]      |  Yes            |    Yes             |    No            |      Yes                     |
|[shutil.copyfileobj][4]|   No            |     No             |   Yes            |       No                     |

  [1]: https://docs.python.org/3/library/shutil.html#shutil.copy
  [2]: https://docs.python.org/3/library/shutil.html#shutil.copyfile
  [3]: https://docs.python.org/3/library/shutil.html#shutil.copy2
  [4]: https://docs.python.org/3/library/shutil.html#shutil.copyfileobj


`Copy2` Example:
```python
import shutil
shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
```

> reference:
> - https://stackoverflow.com/questions/123198/how-to-copy-files/30359308#30359308