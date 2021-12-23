CMAKE_MINIMUM_REQUIRED(VERSION 3.14)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

project(Peach)

# GLOBAL Settings
set(DEV_DIR "E:/dev")
set(PEACH_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_definitions(-DFOO="foo test")


add_subdirectory(bootstrap)
