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
set(HOUDEV_PACKAGES_DIR ${PEACH_DIR}/pHoudini/dev/packages)
set(PHOUDINI_TEMPLATES_DIR ${PHOUDINI_DIR}/config/templates)

# [ PATH SETTING <<<OUT ]
set(INSTALL_PHOUDINI_DIR ${PEACH_INSTALL_DIR}/pHoudini)
set(INSTALL_PACKAGES_DIR ${PEACH_INSTALL_DIR}/pHoudini/packages)

# [ PACKAGE LIST ]
list(APPEND PACKAGES
        # PeachPy (from lib)
        PeachModel 
        PeachUltraUrban
    )

set(PACKAGE_LIST_STR "PeachPy\n")


# [ SETTINGS ]
set(PACKAGE_VERSION "0.1.4")
set(ULTRA_URBAN_VERSION "0.2.1")
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
        ${INSTALL_PHOUDINI_DIR}/PeachEnv.json
    )
    # /.Install: PeachEnv Package Folder 
    install(DIRECTORY 
        ${PHOUDINI_DEV_DIR}/PeachEnv
        DESTINATION ${INSTALL_PHOUDINI_DIR})
    
    # /.Install: Cofigure Each package
    foreach(PKG IN LISTS PACKAGES)
        # /.. Copy packages into dir.
        install(DIRECTORY 
            "${HOUDEV_PACKAGES_DIR}/${PKG}"
            DESTINATION ${INSTALL_PACKAGES_DIR})
        
        # /.. Create package json files
        configure_file(
            "${PHOUDINI_TEMPLATES_DIR}/__in__${PKG}.json"
            "${INSTALL_PACKAGES_DIR}/${PKG}.json")
        # /.. Create package_list.txt string
        set(PACKAGE_LIST_STR "${PACKAGE_LIST_STR}${PKG}\n")
    endforeach()

    file(WRITE ${INSTALL_PHOUDINI_DIR}/package_list.txt ${PACKAGE_LIST_STR})
endif()