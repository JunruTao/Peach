# ------------------------------------------------------------------------------- #
#       /${PEACH_DIR}
#             +-----/lib
#                    + ---> CMakeLists
# ------------------------------------------------------------------------------- #
# This should build the libs copy all the files..
# [ HOU SETTINGS ] - lib
set(PACKAGE_VERSION "0.1.30")  # >>>> CONTROL [AUTO]

# [ HOUDINI LIBS ]--------------------------------------------------------------- #

# [ PATH SETTING >>>IN ]
set(PHOUDINI_DIR ${PEACH_DIR}/pHoudini)
set(PHOUDINI_DEV_DIR ${PEACH_DIR}/pHoudini/dev)
set(PHOUDINI_TEMPLATES_DIR ${PHOUDINI_DIR}/config/templates)
set(LIB_DIR ${PEACH_DIR}/lib/peach)

# [ PATH SETTINGS <<<OUT ]
set(HOUDEV_PACKAGES_DIR ${PEACH_DIR}/pHoudini/dev/packages)
set(HOUDEV_PEACHPY_DIR ${PEACH_DIR}/pHoudini/dev/packages/PeachPy/python3.7libs)
set(INSTALL_PACKAGES_DIR ${PEACH_INSTALL_DIR}/pHoudini/packages)
set(INSTALL_PEACHPY_DIR ${PEACH_INSTALL_DIR}/pHoudini/packages/PeachPy/python3.7libs)

set(README_STR "# PyPeach ${PACKAGE_VERSION}")

# [ HOU SOURCES ]
# /.source Template:
set(HOU_PY_SOURCE_JSON ${PHOUDINI_TEMPLATES_DIR}/__in__PeachPy.json )
# /.source Python Libs:
set(HOU_PY_LIBRARIES 
    ${LIB_DIR}/pHoudini
    ${LIB_DIR}/pQt
)
# /.source Python files in lib$peach
file(GLOB PEACH_DIR_FILES CONFIGURE_DEPENDS ${LIB_DIR}/*.py)
# /. remove this file and configure if later.
list(REMOVE_ITEM PEACH_DIR_FILES ${LIB_DIR}/pGlob.py)

# [ HOU: CREATE DEV PACKAGE FILES ]
if(BUILD_DEV_HOU)
    # /.configure package file
    configure_file(
        ${HOU_PY_SOURCE_JSON} 
        ${HOUDEV_PACKAGES_DIR}/PeachPy.json)
    
    # /.configure pGlob.py file
    configure_file(
        ${LIB_DIR}/pGlob.py
        ${HOUDEV_PEACHPY_DIR}/peach/pGlob.py)
    
    # /.copy
    install(
        DIRECTORY ${HOU_PY_LIBRARIES}
        DESTINATION ${HOUDEV_PEACHPY_DIR}/peach
        PATTERN
        "__pycache__" EXCLUDE
    )
    # /.copy peach/*.py
    install(
        FILES ${PEACH_DIR_FILES}
        DESTINATION ${HOUDEV_PEACHPY_DIR}/peach
    )
    file(WRITE ${PEACH_DIR}/pHoudini/dev/packages/PeachPy/README.md ${README_STR})
endif()


# [ HOU: CREATE INSTALL PACKAGE FILES ]
if(BUILD_INSTALL_HOU)
    # /.install: configure package file
    configure_file(
        ${HOU_PY_SOURCE_JSON}
        ${INSTALL_PACKAGES_DIR}/PeachPy.json)
    # /.install: copy
    install(
        DIRECTORY  ${HOU_PY_LIBRARIES}
        DESTINATION ${INSTALL_PEACHPY_DIR}/peach)
    # /.install.copy peach/*.py
    install(
        FILES ${PEACH_DIR_FILES}
        DESTINATION ${INSTALL_PEACHPY_DIR}/peach
    )
    file(WRITE ${PEACH_INSTALL_DIR}/pHoudini/packages/PeachPy/README.md ${README_STR})
endif()

add_subdirectory(peach/houdini_panels)
add_subdirectory(peach/houdini_toolbars)
# [ BLENDER LIBS ]--------------------------------------------------------------- #
