CMAKE_MINIMUM_REQUIRED(VERSION 3.14)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

project(appBoostTrap)
set(DEV_DIR "E:/dev")
set(SOURCE_HOU src/main_hou.cpp src/main.cpp)
set(SOURCE_BLN src/main_bln.cpp src/main.cpp)
include_directories(src)

add_executable(pHoudini_init ${SOURCE_HOU})
add_executable(pBlender_init ${SOURCE_BLN})


if (CMAKE_BUILD_TYPE MATCHES Release)
    set(PEACH_INSTALL_DIR ${DEV_DIR}/Peach)
else()
    set(PEACH_INSTALL_DIR ${DEV_DIR}/peach_dev_projects/Peach)
    # setting the debug flag by force as long as it is not release mode
    add_definitions(-DDEBUG)
endif()


install(TARGETS pHoudini_init DESTINATION ${PEACH_INSTALL_DIR})
install(TARGETS pBlender_init DESTINATION ${PEACH_INSTALL_DIR})

install(DIRECTORY 
        ${CMAKE_SOURCE_DIR}/config
        DESTINATION ${PEACH_INSTALL_DIR})