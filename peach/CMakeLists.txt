CMAKE_MINIMUM_REQUIRED(VERSION 3.22)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

project(Peach)

# [ GLOBAL ] Versions
set(PEACH_VERSION_MAJOR "0")
set(PEACH_VERSION_MINOR "0")
set(PEACH_VERSION_PATCH "1")

# [ SOURCE PATH ] Settings
set(DEV_DIR "E:/dev")
set(PEACH_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(PEACH_ICONS_DIR "${PEACH_DIR}/icons")
set(PEACH_ICONS_ICO_DIR "${PEACH_DIR}/icons/ICO")

# [ TARGET PATH ] Settings
set(PEACH_DEBUG_INSTALL_DIR "${DEV_DIR}/peach_dev_projects/Peach")
set(PEACH_FINAL_INSTALL_DIR "${DEV_DIR}/Peach")
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

# [ PASSING TO PREPROCESSOR ]
add_definitions(
    -DPEACH_VERSION="-${PEACH_BUILD} v${PEACH_VERSION_MAJOR}.${PEACH_VERSION_MINOR}.${PEACH_VERSION_PATCH}"
    )


# [ SUBDIRECTORIES ]
add_subdirectory(bootstrap)


# [ INSTALL ]
# /.files and directories
install(DIRECTORY 
        ${PEACH_DIR}/config
        DESTINATION ${PEACH_INSTALL_DIR})