set(PHOUDINI_TOOLS_XML_MEMBERS_STR "") # <--- tools combined
set(PHOUDINI_TOOLS_XML_STR "") # format: <memberTool name="${TOOL_NAME}"/>...

# [ FOREACH TOOLS ]
foreach(TOOL_NAME IN LISTS TOOLS)
    message(STATUS ". . [MakeShelf::Adding Tool]: ${TOOL_NAME}")
    # Read configuration for those variables locally in panel dir
    add_subdirectory(${SHELF_CMAKE_LIST_DIR}/${TOOL_NAME})
    file(READ ${SHELF_CMAKE_LIST_DIR}/${TOOL_NAME}/tool_script.py TOOL_SCRIPT)
    string(CONFIGURE ${TOOL_TEMPLATE} TOOL_XML_UNIT)
    string(APPEND PHOUDINI_TOOLS_XML_STR ${TOOL_XML_UNIT})
    string(APPEND PHOUDINI_TOOLS_XML_MEMBERS_STR "    <memberTool name=\"${TOOL_NAME}\"/>\n")
endforeach()

# [ FIND THE BUILD PATH DEPENDS ON NAME ]
if(${TARGET_PKG} MATCHES "PeachEnv")
    set(SHELF_BUILD_PATH ${PEACH_DIR}/pHoudini/dev/PeachEnv/toolbar/${TOOLBAR_NAME}.shelf)
else()
    set(SHELF_BUILD_PATH ${PEACH_DIR}/pHoudini/dev/packages/${TARGET_PKG}/toolbar/${TOOLBAR_NAME}.shelf)
endif()

# [ BUILD FINAL TOOLBAR ]
if(BUILD_DEV_HOU)
    configure_file(
        ${TOOLBAR_TEMPLATE}
        ${SHELF_BUILD_PATH})
endif()