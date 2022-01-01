# ------------------------------------------------------------------------------- #
#       /${PEACH_DIR}
#             +-----/pHoudini
#                       +----> CMakeLists
# ------------------------------------------------------------------------------- #
# This is pHouidni Configuration CMake File
# The main/env peach Houdini package will be generated
# from this file

# [ BUILD SETTINGS ]
set(BUILD_DEV TRUE)
set(BUILD_INSTALL TRUE)

# [ PHOU-PATH SETTING >>>IN ]
set(PHOUDINI_DIR ${PEACH_DIR}/pHoudini)
set(PHOUDINI_DEV_DIR ${PEACH_DIR}/pHoudini/dev)
set(PHOUDINI_TEMPLATES_DIR ${PHOUDINI_DIR}/config/templates)

# [ PATH SETTING <<<OUT ]
set(ENV_FILE_INSTALL_DIR ${PEACH_INSTALL_DIR}/pHoudini)

# [ SETTINGS ]
set(PACKAGE_VERSION "0.1.2")`
set(HOU_MIN_VER "19.0")
set(HOU_MAX_VER "19.1")

# [ CREATING FILES FROM TEMPLATES ]
configure_file(${PHOUDINI_TEMPLATES_DIR}/__in__PeachEnv.json 
               ${PHOUDINI_DEV_DIR}/PeachEnv.json
               )

# [ CREATE ENV PACKAGE FILES ]
if(${BUILD_DEV})    
    # /.Copy the `houdini_util file into this dev section as util`
    install(FILES ${PEACH_DIR}/config/scripts/houdini_util.py
            DESTINATION ${PHOUDINI_DIR}/config/scripts/nocopy/)
    file(WRITE ${PHOUDINI_DIR}/config/scripts/nocopy/__init__.py "#!/usr/bin/python")      
endif()

# [ CREATE INSTALL PACKAGE FILES ]
if(${BUILD_INSTALL})
    install(DIRECTORY 
        ${PHOUDINI_DEV_DIR}/PeachEnv
        DESTINATION ${ENV_FILE_INSTALL_DIR})
endif()