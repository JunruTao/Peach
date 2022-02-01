# ------------------------------------------------------------------------------- #
#       /${PEACH_DIR}
#             +-----/lib
#                   +-----/peach
#                       +-----/houdini_panels
#                              + ---> CMakeLists
# ------------------------------------------------------------------------------- #

# [ PATH >>> SOURCE ] Settings
set(PANEL_TEMPLATES_DIR ${CMAKE_CURRENT_LIST_DIR}/templates)
# [ XML PYPANEL TEMPLATE ]
set(PYPANEL_TEMPLATE ${PANEL_TEMPLATES_DIR}/python_panel_template.xml)
# [ READING COMMENT HEADER TEMPLATE ]
file(READ ${PANEL_TEMPLATES_DIR}/python_panel_comment.py COMMENT_TEMPLATE)
# [ CONFIGURE STRING ]
string(CONFIGURE ${COMMENT_TEMPLATE} COMMENT_HEADER)

# [ SUBDIRS OF PANELS ]
list(APPEND PANEL_NAMES 
        "peach_main"
        "asset_manager"
)

set(COUNTER 500)

message(STATUS "[houdini_panel]: Building PyPanels...")
# [ FOREACH PANELS ]
foreach(PANEL_NAME IN LISTS PANEL_NAMES)
    message(STATUS ". [houdini_panel]: Building Python Panel < ${PANEL_NAME} >")
    # Read configuration for those variables locally in panel dir
    add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/${PANEL_NAME})
    math(EXPR COUNTER "${COUNTER}+1")
    set(PANEL_MENU_POS "${COUNTER}")
    file(READ ${CMAKE_CURRENT_LIST_DIR}/${PANEL_NAME}/pypanel_${PANEL_NAME}.py PANEL_SCRIPT)

    if(${TARGET_PKG} MATCHES "PeachEnv")
        set(PANEL_BUILD_PATH ${PEACH_DIR}/pHoudini/dev/PeachEnv/python_panels/${PANEL_NAME}.pypanel)
    else()
        set(PANEL_BUILD_PATH ${PEACH_DIR}/pHoudini/dev/packages/${TARGET_PKG}/python_panels/${PANEL_NAME}.pypanel)
    endif()
    # ${TARGET_PKG} is set under subdir. check the naming and templates.
    if(BUILD_DEV_HOU)
        configure_file(
            ${PYPANEL_TEMPLATE}
            ${PANEL_BUILD_PATH})
    endif()

endforeach()
