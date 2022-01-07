# ------------------------------------------------
# Houdini Panel CMake Configuration

set(PANEL_NAME "peach_main")
file(READ ${CMAKE_CURRENT_LIST_DIR}/pypanel_${PANEL_NAME}.py PANEL_SCRIPT)
set(PANEL_LABEL "Peach Main")
set(PANEL_ICON "icon_peach")
set(PANEL_MENU_POS "501")
set(PANEL_MENU_SPR "true")