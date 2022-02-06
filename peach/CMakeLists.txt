# ------------------------------------------------------------------------------- #
#                          THIS IS THE MAIN CMAKE FILE
#
#       /${PEACH_DIR}
#             + ---> CMakeLists
# ------------------------------------------------------------------------------- #
# [ QUICK BUILD OPTIONS ]
# /. build the dev version only
set(BUILD_DEV_NOT_INSTALL FALSE)  # >>>> CONTROL [AUTO]
# /. build lib only
set(BUILD_DEVLIB_ONLY FALSE)      # >>>> CONTROL [AUTO]

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
set(PEACH_VERSION_MINOR "1")
set(PEACH_VERSION_PATCH "32")  # [AUTO]
set(PEACH_VERSION "${PEACH_VERSION_MAJOR}.${PEACH_VERSION_MINOR}.${PEACH_VERSION_PATCH}")

# [ DCC SETTINGS ]
set(HOU_MIN_VER "19.0")
set(HOU_MAX_VER "19.1")

# [ META-DATA ]
string(TIMESTAMP STR_DATE_YMD "%Y.%m.%d")
string(TIMESTAMP STR_TIME_HMS "%H:%M:%S")

# [ SOURCE PATH ] Settings
get_filename_component(DEV_DIR ${CMAKE_CURRENT_SOURCE_DIR} DIRECTORY)
get_filename_component(DEV_DIR ${DEV_DIR} DIRECTORY)

set(PEACH_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(PEACH_ICONS_DIR "${PEACH_DIR}/icons")
set(PEACH_ICONS_ICO_DIR "${PEACH_DIR}/icons/ICO")


# [ INSTALLATION OPTIONS ]
# /. Install Settings
set(INSTALL_ICON ON)      # >>>> CONTROL [AUTO]
set(INSTALL_CONFIG ON)
set(INSTALL_CONFIG_OVRD OFF)
set(BUILD_BOOTSTRAP ON)      # >>>> CONTROL [AUTO]
# /. Houdini Dev Builds
set(BUILD_DEV_HOU ON)
set(BUILD_INSTALL_HOU ON)
# /. Blender Dev Builds
set(BUILD_DEV_BLD ON)
set(BUILD_INSTALL_BLD ON)

# /. Do Not Install in install dir
if (BUILD_DEV_NOT_INSTALL)
    set(INSTALL_ICON OFF)
    set(INSTALL_CONFIG OFF)
    set(BUILD_BOOTSTRAP OFF)
    set(BUILD_INSTALL_HOU OFF)
    set(BUILD_INSTALL_BLD OFF)
endif()

# Only Build devlib
if (BUILD_BUILD_DEVLIB_ONLY)
    # /. Install Settings
    set(INSTALL_ICON OFF)
    set(INSTALL_CONFIG OFF)
    set(BUILD_BOOTSTRAP OFF)
    # /. Houdini Dev Builds
    set(BUILD_DEV_HOU ON)
    set(BUILD_INSTALL_HOU OFF)
    # /. Blender Dev Builds
    set(BUILD_DEV_BLD ON)
    set(BUILD_INSTALL_BLD OFF)
endif()


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
message(STATUS "[Peach]Building Peach...")
message(STATUS ". [Peach::Version]: Peach -v${PEACH_VERSION}")
message(STATUS ". [Peach::Build]: Peach -${PEACH_BUILD}")

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
            DESTINATION ${PEACH_INSTALL_DIR}
            PATTERN "desktop.ini" EXCLUDE
            PATTERN "startup.pconfig" EXCLUDE)
    if(INSTALL_CONFIG_OVRD)
        install(FILES 
                ${PEACH_DIR}/config/startup.pconfig
                DESTINATION ${PEACH_INSTALL_DIR}/config)
    endif()
endif()

# /.icons
if(INSTALL_ICON)
    install(DIRECTORY 
            ${PEACH_DIR}/icons/SVG # install vector icons
            ${PEACH_DIR}/icons/25w # install small icons
            ${PEACH_DIR}/icons/HICON # houdini icons
            DESTINATION ${PEACH_INSTALL_DIR}/icons)
    install(DIRECTORY
            ${PEACH_DIR}/images
            DESTINATION ${PEACH_INSTALL_DIR}
            PATTERN "desktop.ini" EXCLUDE)
    install(DIRECTORY
            ${PEACH_DIR}/fonts
            DESTINATION ${PEACH_INSTALL_DIR}
            PATTERN "desktop.ini" EXCLUDE)
endif()


if(NOT BUILD_DEV_NOT_INSTALL)
    # /.license
    install(FILES 
            ${PEACH_DIR}/LICENSE.txt 
            DESTINATION 
            ${PEACH_INSTALL_DIR})
endif()