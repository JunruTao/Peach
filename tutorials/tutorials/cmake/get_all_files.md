# How to get all the files in the directory

use `file(GLOB ...)` function

`[1]`
```cmake
cmake_minimum_required(VERSION 2.8)

file(GLOB helloworld_SRC
     "*.h"
     "*.cpp"
)

add_executable(helloworld ${helloworld_SRC})
```

`[2]` As of CMake 3.12, you can pass the `CONFIGURE_DEPENDS` flag to `file(GLOB` to automatically check and reset the file lists any time the build is invoked. You would write:
```cmake
cmake_minimum_required(VERSION 3.12)
file(GLOB helloworld_SRC CONFIGURE_DEPENDS "*.h" "*.cpp")
```


> reference:
> - https://cmake.org/cmake/help/latest/command/file.html#glob
> - https://stackoverflow.com/questions/3201154/automatically-add-all-files-in-a-folder-to-a-target-using-cmake