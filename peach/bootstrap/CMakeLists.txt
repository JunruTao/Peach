set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
project(PEACH_Bootstraps)

set(SOURCE_HOU src/main_hou.cpp src/main.cpp)
set(SOURCE_BLN src/main_bln.cpp src/main.cpp)

include_directories(src)

set(WIN_APP_ICON_RESOURCE_HOU 
    "${CMAKE_CURRENT_SOURCE_DIR}/resource/win_appicon_hou.rc")
set(WIN_APP_ICON_RESOURCE_BLN 
    "${CMAKE_CURRENT_SOURCE_DIR}/resource/win_appicon_bln.rc")

add_executable(pHoudini_init ${SOURCE_HOU} ${WIN_APP_ICON_RESOURCE_HOU})
add_executable(pBlender_init ${SOURCE_BLN} ${WIN_APP_ICON_RESOURCE_BLN})

if (CMAKE_BUILD_TYPE MATCHES Release)
    # [ MODE ] Release Version
    set(PEACH_INSTALL_DIR ${DEV_DIR}/Peach)
else()
    # [ MODE ] Debug/Test Version
    add_definitions(-DDEBUG)
    set(PEACH_INSTALL_DIR ${DEV_DIR}/peach_dev_projects/Peach)
endif()

install(TARGETS pHoudini_init DESTINATION ${PEACH_INSTALL_DIR})
install(TARGETS pBlender_init DESTINATION ${PEACH_INSTALL_DIR})

install(DIRECTORY 
        ${CMAKE_CURRENT_SOURCE_DIR}/config
        DESTINATION ${PEACH_INSTALL_DIR})