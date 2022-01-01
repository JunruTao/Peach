# ------------------------------------------------------------------------------- #
#       /${PEACH_DIR}
#             +-----/bootstrap
#                       + ---> CMakeLists
# ------------------------------------------------------------------------------- #

# [ CMAKE CONFIGURATIONS ]
CMAKE_MINIMUM_REQUIRED(VERSION 3.22)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# [ PROJECT ]
project(PEACH_Bootstraps)

# [ BOOTSTRAP ] Versions
set(PEACH_BOOTSTRAP_APP_VERSION_MAJOR "0")
set(PEACH_BOOTSTRAP_APP_VERSION_MINOR "2")
set(PEACH_BOOTSTRAP_APP_BLENDER_VERSION "1")
set(PEACH_BOOTSTRAP_APP_HOUDINI_VERSION "2")

# [ PASSING TO PREPROCESSOR ]
add_definitions(
    -DPEACH_BOOTSTRAP_APP_VERSION="-${PEACH_BUILD} v${PEACH_BOOTSTRAP_APP_VERSION_MAJOR}.${PEACH_BOOTSTRAP_APP_VERSION_MINOR}"
    )
add_definitions(-DPEACH_BOOTSTRAP_BLN_VERSION=${PEACH_BOOTSTRAP_APP_BLENDER_VERSION})
add_definitions(-DPEACH_BOOTSTRAP_HOU_VERSION=${PEACH_BOOTSTRAP_APP_HOUDINI_VERSION})

# [ SOURCE & INCLUDES ]
set(SOURCE_HOU src/main_hou.cpp src/main.cpp)
set(SOURCE_BLN src/main_bln.cpp src/main.cpp)
include_directories(src)

# [ BUILD EXECUTABLES CXX ]
IF (WIN32)
    # [ Windows ] Link Icon Files
    set(WIN_APP_ICON_RESOURCE_HOU 
        "${PEACH_ICONS_ICO_DIR}/icon_peach_houdini.rc")
    set(WIN_APP_ICON_RESOURCE_BLN 
        "${PEACH_ICONS_ICO_DIR}/icon_peach_blender.rc")
    add_executable(pHoudini_init ${SOURCE_HOU} ${WIN_APP_ICON_RESOURCE_HOU})
    add_executable(pBlender_init ${SOURCE_BLN} ${WIN_APP_ICON_RESOURCE_BLN})
ELSE()
    # iconless build
    add_executable(pHoudini_init ${SOURCE_HOU})
    add_executable(pBlender_init ${SOURCE_BLN})
ENDIF()


# [ INSTALLATION ]

# /.executables
install(TARGETS pHoudini_init DESTINATION ${PEACH_INSTALL_DIR})
install(TARGETS pBlender_init DESTINATION ${PEACH_INSTALL_DIR})