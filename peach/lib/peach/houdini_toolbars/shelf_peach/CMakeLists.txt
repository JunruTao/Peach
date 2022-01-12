set(TOOLBAR_LABEL "Peach")
set(TARGET_PKG "PeachEnv")

# [ SOURCE ] <<< ADD TOOLS THAT NEEDED TO INCLUDE IN SHELVE
list(APPEND TOOLS 
            "peach_env"
            "peach_info"
)

set(SHELF_CMAKE_LIST_DIR ${CMAKE_CURRENT_LIST_DIR})
include("${TOOLBAR_LIB_DIR}/MakeShelf.cmake")