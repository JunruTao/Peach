# This is pHouidni Configuration CMake File
# The main/env peach Houdini package will be generated
# from this file

# [ BUILD SETTINGS ]
set(BUILD_DEV TRUE)
set(BUILD_INSTALL TRUE)

# [ PATH SETTING ]
set(PHOUDINI_DIR ${PEACH_DIR}/pHoudini)
set(PHOUDINI_DEV_DIR ${PEACH_DIR}/pHoudini/dev)
set(ENV_FILE_INSTALL_DIR ${PEACH_INSTALL_DIR}/pHoudini)

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
    ],
    \"path\" : \"$PEACH_HOU/PeachEnv\"
}")

# [ CREATE ENV PACKAGE FILES ]
if(${BUILD_DEV})
    file(WRITE ${PHOUDINI_DEV_DIR}/PeachEnv.json ${PEACH_ENV_DATA})

    # /.Copy the `houdini_util file into this dev section as util`
    install(FILES ${PEACH_DIR}/config/scripts/houdini_util.py
            DESTINATION ${PHOUDINI_DIR}/config/scripts/util_x/)
    file(WRITE ${PHOUDINI_DIR}/config/scripts/util_x/__init__.py "#!/usr/bin/python")      
endif()

# [ CREATE INSTALL PACKAGE FILES ]
if(${BUILD_INSTALL})
    file(WRITE ${ENV_FILE_INSTALL_DIR}/PeachEnv.json ${PEACH_ENV_DATA})
    install(DIRECTORY 
        ${PHOUDINI_DEV_DIR}/PeachEnv
        DESTINATION ${ENV_FILE_INSTALL_DIR})
endif()