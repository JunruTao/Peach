# Houdini Environment Variables

Getting some basic environment variables such as `$HIP`, `$JOB`, `$HOUDINI_PATH`, `$HFS` etc. These operations can be done by calling python functions:

|1. `Getter` and `Setter` for Env|
|:---|
- python:
```python
# : run in python console

>>> print(hou.getenv("HSITE"))

# result: None

>>> hou.putenv("HSITE", "/usr/lib/myPath")
>>> print(hou.getenv("HSITE"))

# result: /usr/lib/myPath


```

|2. Getting `HOUDNI_PATH`, There are 2 ways|
|:---|

- python:
```python
# use houdiniPath function

path = hou.houdiniPath()
print(path)

# or use the env generic way

path = hou.getenv("HOUDINI_PATH")
print(path)
```


---
### References:
- [Houdini - Environment variables](https://www.sidefx.com/docs/houdini/basics/config_env.html)