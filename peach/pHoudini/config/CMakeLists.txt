# This is pHouidni Configuration CMake File
# The main/env peach Houdini package will be generated
# from this file


# [ PATH SETTING ]
set(PHOUDINI_DIR ${PEACH_DIR}/pHoudini)
set(DEV_ENV_FILE_INSTALL_DIR ${PEACH_DIR}/pHoudini/dev)
# set(DEBUG_ENV_FILE_INSTALL_DIR ${PEACH_DEBUG_INSTALL_DIR}/pHoudini)
# set(FINAL_ENV_FILE_INSTALL_DIR ${PEACH_FINAL_INSTALL_DIR}/pHoudini)

# [ SETTINGS ]
set(PACKAGE_VERSION "0.1.0")
set(HOU_MIN_VER "19.0")
set(HOU_MAX_VER "19.1")

# [ CREATE ENV PACKAGE FILES ]
file(WRITE 
${DEV_ENV_FILE_INSTALL_DIR}/peach_env.json 
"{
    \"author\" : \"${AUTHOR}\",
    \"version\": \"${PACKAGE_VERSION}\",
    \"load_package_once\": true,
    \"enable\" : \"houdini_version >= '${HOU_MIN_VER}' and houdini_version < '${HOU_MAX_VER}'\",
    \"env\" : [
        {\"PEACH_VERSION\" : \"${PEACH_VERSION}\"},
        {\"PEACH_CREATOR\" : \"${AUTHOR}\"},
        {\"PEACH_BUILD\" : \"${PEACH_BUILD}\"}
    ]
}")