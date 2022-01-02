# ------------------------------------------------------------------------------- #
#       /${PEACH_DIR}
#             +-----/pHoudini
#                       +----> CMakeLists
# ------------------------------------------------------------------------------- #
# This is pHouidni Configuration CMake File
# The main/env peach Houdini package will be generated
# from this file

# [ BUILD SETTINGS ]
set(BUILD_DEV_HOU TRUE)
set(BUILD_INSTALL_HOU TRUE)

# [ PHOU-PATH SETTING >>>IN ]
set(PHOUDINI_DIR ${PEACH_DIR}/pHoudini)
set(PHOUDINI_DEV_DIR ${PEACH_DIR}/pHoudini/dev)
set(PHOUDINI_TEMPLATES_DIR ${PHOUDINI_DIR}/config/templates)

# [ PATH SETTING <<<OUT ]
set(ENV_FILE_INSTALL_DIR ${PEACH_INSTALL_DIR}/pHoudini)

# [ SETTINGS ]
set(PACKAGE_VERSION "0.1.3")

# [ HOU SOURCES ]
# /.source Template:
set(HOU_ENV_SOURCE_JSON ${PHOUDINI_TEMPLATES_DIR}/__in__PeachEnv.json )

# [ CREATE ENV PACKAGE FILES ]
if(${BUILD_DEV_HOU})
    # /.CREATING FILES FROM TEMPLATES
    configure_file(
        ${HOU_ENV_SOURCE_JSON}
        ${PHOUDINI_DEV_DIR}/PeachEnv.json
    )
    # /.Copy the `houdini_util file into this dev section as util`
    install(FILES ${PEACH_DIR}/config/scripts/houdini_util.py
            DESTINATION ${PHOUDINI_DIR}/config/scripts/nocopy/)
    file(WRITE ${PHOUDINI_DIR}/config/scripts/nocopy/__init__.py "#!/usr/bin/python")      
endif()

# [ CREATE INSTALL PACKAGE FILES ]
if(${BUILD_INSTALL_HOU})
    # /.Install: CREATING FILES FROM TEMPLATES
    configure_file(
        ${HOU_ENV_SOURCE_JSON}
        ${ENV_FILE_INSTALL_DIR}/PeachEnv.json
    )
    # /.Install: PeachEnv Package Folder 
    install(DIRECTORY 
        ${PHOUDINI_DEV_DIR}/PeachEnv
        DESTINATION ${ENV_FILE_INSTALL_DIR})
endif()