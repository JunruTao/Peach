import os

main_cmake_str = ""

with open("./CMakeLists.txt", "r") as f:
    for line in f:
        if str(line).startswith("set(BUILD_DEV_NOT_INSTALL"):
            line = "set(BUILD_DEV_NOT_INSTALL FALSE)  # >>>> CONTROL [AUTO]\n"
            print("[settings-cmake]: ", line.rstrip())
        if str(line).startswith("set(BUILD_DEVLIB_ONLY"):
            line = "set(BUILD_DEVLIB_ONLY FALSE)      # >>>> CONTROL [AUTO]\n"
            print("[settings-cmake]: ", line.rstrip())
        if str(line).startswith("set(PEACH_VERSION_PATCH"):
            _, ver, _ = line.split("\"")
            line = "set(PEACH_VERSION_PATCH \"{0}\")  # [AUTO]\n".format(int(ver) + 1)
            print("[settings-cmake version up]: ", line.rstrip())
        main_cmake_str += line
    f.close()

with open("./CMakeLists.txt", "w+") as f:
    f.write(main_cmake_str)
    f.close()

main_cmake_str = ""
with open("./lib/CMakeLists.txt", "r") as f:
    for line in f:
        if str(line).startswith("set(PACKAGE_VERSION"):
            _, ver, _ = line.split("\"")
            v_major, v_minor, ver_p = ver.split(".")
            ver_p = str(int(ver_p) + 1)
            line = "set(PACKAGE_VERSION \"{0}.{1}.{2}\")  # >>>> CONTROL [AUTO]\n"
            line = line.format(v_major, v_minor, ver_p)
            print("[settings-cmake version up]: ", line.rstrip())
        main_cmake_str += line
    f.close()
    
with open("./lib/CMakeLists.txt", "w+") as f:
    f.write(main_cmake_str)
    f.close()
    
main_cmake_str = ""
with open("./pHoudini/CMakeLists.txt", "r") as f:
    for line in f:
        if str(line).startswith("set(PACKAGE_VERSION"):
            _, ver, _ = line.split("\"")
            v_major, v_minor, ver_p = ver.split(".")
            ver_p = str(int(ver_p) + 1)
            line = "set(PACKAGE_VERSION \"{0}.{1}.{2}\")  # >>>> CONTROL [AUTO]\n"
            line = line.format(v_major, v_minor, ver_p)
            print("[settings-cmake version up]: ", line.rstrip())
        main_cmake_str += line
    f.close()
    
with open("./pHoudini/CMakeLists.txt", "w+") as f:
    f.write(main_cmake_str)
    f.close()