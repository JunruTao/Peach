set(TOOLBAR_LABEL "Peach Dev")
set(TARGET_PKG "PeachEnv")

# [ SOURCE ] <<< ADD TOOLS THAT NEEDED TO INCLUDE IN SHELVE
list(APPEND TOOLS 
            "renamer"
            "hda_manager"
)

set(SHELF_CMAKE_LIST_DIR ${CMAKE_CURRENT_LIST_DIR})
include("${TOOLBAR_LIB_DIR}/MakeShelf.cmake")
