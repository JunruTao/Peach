import os


main_cmake_str = ""
with open("./CMakeLists.txt", "r") as f:
    for line in f:
        if str(line).startswith("set(BUILD_DEV_NOT_INSTALL"):
            line = "set(BUILD_DEV_NOT_INSTALL TRUE)  # >>>> CONTROL [AUTO]\n"
            print("[settings-cmake]: ", line.rstrip())
        if str(line).startswith("set(BUILD_DEVLIB_ONLY"):
            line = "set(BUILD_DEVLIB_ONLY TRUE)      # >>>> CONTROL [AUTO]\n"
            print("[settings-cmake]: ", line.rstrip())
        main_cmake_str += line
    f.close()
    

with open("./CMakeLists.txt", "w+") as f:
    f.write(main_cmake_str)
    f.close()