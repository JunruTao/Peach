# Get Parent Directory

As of CMake 2.8.12, the recommended way is to use the get_filename_component command with the DIRECTORY option:

```cmake
get_filename_component(PARENT_DIR ${MYPROJECT_DIR} DIRECTORY)
```

> reference
    > https://stackoverflow.com/questions/7035734/cmake-parent-directory