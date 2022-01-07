# For-each Loop in CMake


```cmake

list(APPEND PANEL_NAMES 
        "peach_main"
        "asset_browser"
    )

foreach(PANEL_NAME IN LISTS ${PANEL_NAMES})

    # do stuff
    
endforeach()
```
> reference:
> - https://cmake.org/cmake/help/latest/command/foreach.html