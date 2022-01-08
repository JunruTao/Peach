# ------------------------------------------------------------------------------- #
#                          THIS IS THE MAIN CMAKE FILE
#
#       /${PEACH_DIR}
#             + ---> CMakeLists
# ------------------------------------------------------------------------------- #

# [ CMAKE CONFIGURATION ]
CMAKE_MINIMUM_REQUIRED(VERSION 3.22)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# [ MAIN ]
project(Peach)


# [ GLOBAL ] Info
set(AUTHOR "Junru Tao")
set(COMPANY "Digital Peach Studio")
set(EMAIL "<junrutao.uk@gmail.com | junrutao@qq.com>")
set(WEBSITE "digital-peach.company.site")
set(INSTAGRAM "@digital.peach.studio")

# [ GLOBAL ] Versions
set(PEACH_VERSION_MAJOR "0")
set(PEACH_VERSION_MINOR "0")
set(PEACH_VERSION_PATCH "10")
set(PEACH_VERSION "${PEACH_VERSION_MAJOR}.${PEACH_VERSION_MINOR}.${PEACH_VERSION_PATCH}")


# [ DCC SETTINGS ]
set(HOU_MIN_VER "19.0")
set(HOU_MAX_VER "19.1")


# [ SOURCE PATH ] Settings
get_filename_component(DEV_DIR ${CMAKE_CURRENT_SOURCE_DIR} DIRECTORY)
get_filename_component(DEV_DIR ${DEV_DIR} DIRECTORY)

set(PEACH_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(PEACH_ICONS_DIR "${PEACH_DIR}/icons")
set(PEACH_ICONS_ICO_DIR "${PEACH_DIR}/icons/ICO")


# [ INSTALLATION OPTIONS ]
# /. Install Settings
set(INSTALL_ICON ON)
set(INSTALL_CONFIG ON)
set(BUILD_BOOTSTRAP ON)
# /. Houdini Dev Builds
set(BUILD_DEV_HOU ON)
set(BUILD_INSTALL_HOU ON)
# /. Blender Dev Builds
set(BUILD_DEV_BLD ON)
set(BUILD_INSTALL_BLD ON)

# [ TARGET PATH ] Settings
set(PEACH_DEBUG_INSTALL_DIR "${DEV_DIR}/peach_dev_projects/Peach")
set(PEACH_FINAL_INSTALL_DIR "${DEV_DIR}/Peach_v${PEACH_VERSION}")


if (CMAKE_BUILD_TYPE MATCHES Release)
    # /MODE = Release Version
    set(PEACH_INSTALL_DIR ${PEACH_FINAL_INSTALL_DIR})
    set(PEACH_BUILD "Release")
else()
    # /MODE = Debug/Test Version
    add_definitions(-DDEBUG)
    set(PEACH_INSTALL_DIR ${PEACH_DEBUG_INSTALL_DIR})
    set(PEACH_BUILD "Debug")
endif()

# [ BUILD MESSAGES ]
message(STATUS "Building Peach...")
message(STATUS "Version: Peach -v${PEACH_VERSION}")
message(STATUS "Build: Peach -${PEACH_BUILD}")

# [ PASSING TO PREPROCESSOR ]
add_definitions(
    -DPEACH_VERSION="-${PEACH_BUILD} v${PEACH_VERSION}"
    )


# ------------------------------------------------------------------------------- #
# [ SUBDIRECTORIES ]------------------------------------------------------------- #

if(BUILD_BOOTSTRAP)
    add_subdirectory(bootstrap)
endif()
add_subdirectory(lib)
add_subdirectory(pHoudini)

# ------------------------------------------------------------------------------- #


# [ INSTALL ]
# /.files and directories
if(INSTALL_CONFIG)
    install(DIRECTORY 
            ${PEACH_DIR}/config
            DESTINATION ${PEACH_INSTALL_DIR})
endif()

# /.icons
if(INSTALL_ICON)
    install(DIRECTORY 
            ${PEACH_DIR}/icons/SVG # install vector icons
            ${PEACH_DIR}/icons/25w # install small icons
            DESTINATION ${PEACH_INSTALL_DIR}/icons)
endif()

# /.license
install(FILES 
        ${PEACH_DIR}/LICENSE.txt 
        DESTINATION 
        ${PEACH_INSTALL_DIR})