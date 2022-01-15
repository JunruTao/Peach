from peach import pLog
from peach.pHoudini.tools.dev_tools import renamer


rn = renamer.RenamerUI()
pLog.message("Show Renamer", fn="Show", cls=rn)
rn.show()
