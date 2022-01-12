from peach import pLog
import hou

pLog.message("Hello World", fn="test", cls="PeachInfo")

# [ Message Structure]
msg = """

PEACH by 'Digital-Peach'

- Build: {build}
- Version: {version}
- Author: {author}
- Location: {dir}

{message}
"""

# [ Format Message]
msg = msg.format(build=hou.getenv("PEACH_BUILD"),
                 version=hou.getenv("PEACH_VERSION"),
                 author=hou.getenv("PEACH_CREATOR"),
                 dir=hou.getenv("PEACH"),
                 message="")

# [ Message Show ]
hou.ui.displayMessage(msg)