# This is pHouidni Configuration CMake File
# The main/env peach Houdini package will be generated
# from this file

# [ BUILD SETTINGS ]
set(BUILD_DEV TRUE)
set(BUILD_INSTALL TRUE)

# [ PATH SETTING ]
set(PHOUDINI_DIR ${PEACH_DIR}/pHoudini)
set(DEV_ENV_FILE_INSTALL_DIR ${PEACH_DIR}/pHoudini/dev)
set(DEBUG_ENV_FILE_INSTALL_DIR ${PEACH_DEBUG_INSTALL_DIR}/pHoudini)
set(FINAL_ENV_FILE_INSTALL_DIR ${PEACH_FINAL_INSTALL_DIR}/pHoudini)

# [ SETTINGS ]
set(PACKAGE_VERSION "0.1.0")
set(HOU_MIN_VER "19.0")
set(HOU_MAX_VER "19.1")


set(PEACH_ENV_DATA 
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

# [ CREATE ENV PACKAGE FILES ]
if(${BUILD_DEV})
    file(WRITE ${DEV_ENV_FILE_INSTALL_DIR}/PeachEnv.json ${PEACH_ENV_DATA})
endif()

# [ CREATE INSTALL PACKAGE FILES ]
if(${BUILD_INSTALL})
    if (${PEACH_BUILD} MATCHES Release)
        file(WRITE ${FINAL_ENV_FILE_INSTALL_DIR}/PeachEnv.json ${PEACH_ENV_DATA})
    else()
        file(WRITE ${DEBUG_ENV_FILE_INSTALL_DIR}/PeachEnv.json ${PEACH_ENV_DATA})
    endif()
endif()