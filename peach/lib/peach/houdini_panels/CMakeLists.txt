# ------------------------------------------------------------------------------- #
#       /${PEACH_DIR}
#             +-----/lib
#                    +-----/houdini_panels
#                              + ---> CMakeLists
# ------------------------------------------------------------------------------- #

set(PANEL_TEMPLATES_DIR ${CMAKE_CURRENT_LIST_DIR}/templates)
# [ CONFIGURE THE COMMENTS FIRST ]
set(CONFIGURED_COMMENT_FILE ${PANEL_TEMPLATES_DIR}/temp/python_panel_comment.temp)
set(PYPANEL_TEMPLATE ${PANEL_TEMPLATES_DIR}/python_panel_template.xml)
# [ DUMP COMMENT INTO A TEMP FILE ]
configure_file(
    ${PANEL_TEMPLATES_DIR}/python_panel_comment.py
    ${CONFIGURED_COMMENT_FILE})

# [ READING THE VALUE BACK ]
file(READ ${CONFIGURED_COMMENT_FILE} COMMENT_HEADER)


set(PANEL_NAME "peach_main")
file(READ ${CMAKE_CURRENT_LIST_DIR}/${PANEL_NAME}/pypanel_${PANEL_NAME}.py PANEL_SCRIPT)
set(PANEL_LABEL "Peach Main")
set(PANEL_ICON "icon_peach")
set(PANEL_MENU_POS "501")
set(PANEL_MENU_SPR "true")

if(BUILD_DEV_HOU)
configure_file(
    ${PYPANEL_TEMPLATE}
    ${PEACH_DIR}/pHoudini/dev/PeachEnv/python_panels/${PANEL_NAME}.pypanel)
endif()

if(BUILD_INSTALL_HOU)
configure_file(
    ${PYPANEL_TEMPLATE}
    ${PEACH_INSTALL_DIR}/pHoudini/PeachEnv/python_panels/${PANEL_NAME}.pypanel)
endif()

set(PANEL_NAME "asset_browser")
file(READ ${CMAKE_CURRENT_LIST_DIR}/${PANEL_NAME}/pypanel_${PANEL_NAME}.py PANEL_SCRIPT)
set(PANEL_LABEL "Peach Asset Browser")
set(PANEL_ICON "icon_peach_dev")
set(PANEL_MENU_POS "502")
set(PANEL_MENU_SPR "false")

if(BUILD_DEV_HOU)
configure_file(
    ${PYPANEL_TEMPLATE}
    ${PEACH_DIR}/pHoudini/dev/packages/PeachAsset/python_panels/${PANEL_NAME}.pypanel)
endif()

if(BUILD_INSTALL_HOU)
configure_file(
    ${PYPANEL_TEMPLATE}
    ${PEACH_INSTALL_DIR}/pHoudini/packages/PeachAsset/python_panels/${PANEL_NAME}.pypanel)
endif()
