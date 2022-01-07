# ------------------------------------------------
# Houdini Panel CMake Configuration

set(PANEL_NAME "asset_browser")
file(READ ${CMAKE_CURRENT_LIST_DIR}/pypanel_${PANEL_NAME}.py PANEL_SCRIPT)
set(PANEL_LABEL "Peach Asset Browser")
set(PANEL_ICON "icon_peach_dev")
set(PANEL_MENU_POS "502")
set(PANEL_MENU_SPR "false")
