# ------------------------------------------------------------------------------- #
#       /${PEACH_DIR}
#             +-----/lib
#                   +-----/peach
#                       +-----/houdini_toolbars
#                              + ---> CMakeLists
# ------------------------------------------------------------------------------- #
# Read from templates
#   ---> compile tool, compile tools into the shelves.
# [ PATH >>> SOURCE ] Settings
set(TOOLBAR_LIB_DIR ${CMAKE_CURRENT_LIST_DIR})
set(TOOLBAR_TEMPLATE_DIR ${CMAKE_CURRENT_LIST_DIR}/templates)
# [ XML TOOLBAR TEMPLATE ]
set(TOOLBAR_TEMPLATE ${TOOLBAR_TEMPLATE_DIR}/toolbar_template.xml)

# [ READING COMMENT HEADER TEMPLATE ]
file(READ ${TOOLBAR_TEMPLATE_DIR}/python_toolbar_comment.py COMMENT_TEMPLATE)
file(READ ${TOOLBAR_TEMPLATE_DIR}/tool_template.xml TOOL_TEMPLATE)
# [ CONFIGURE STRING ]
string(CONFIGURE ${COMMENT_TEMPLATE} COMMENT_HEADER)

# [ SUBDIRS OF SHELVES ]
list(APPEND SHELVES 
        "shelf_peach"
        "shelf_peach_dev"
)

message(STATUS "[houdini_toolbars]: Building Toolbars...")
foreach(TOOLBAR_NAME IN LISTS SHELVES)
    message(STATUS ". [houdini_toolbars]: Configure Toolbar < ${TOOLBAR_NAME} >")
    add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/${TOOLBAR_NAME})
endforeach()
