# CMake Intall Function

### 1. Install Directory and Exclude subdir:

Using `PATTERN` and `EXCLUDE`example:

```cmake
install(DIRECTORY "${HOUDEV_PACKAGES_DIR}/${PKG}"
                DESTINATION ${INSTALL_PACKAGES_DIR}
                PATTERN "wip" EXCLUDE 
        )

# or you can also do:
install(DIRECTORY "${HOUDEV_PACKAGES_DIR}/${PKG}"
                DESTINATION ${INSTALL_PACKAGES_DIR}
                FILES_MATCHING  # For file types
                PATTERN "*.h"   # 
                PATTERN "wip" EXCLUDE   # for directories
        )
```

> Reference:
> - https://stackoverflow.com/questions/8560122/installing-certain-files-with-cmake/8561793