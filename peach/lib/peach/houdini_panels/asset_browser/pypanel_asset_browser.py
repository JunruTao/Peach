from peach import pImp
from peach.pQt import img
from peach.pHoudini.panels import peach_main
from peach.pHoudini.tools.dev_tools import renamer
pImp.reload(img, peach_main)


def onCreateInterface():
    widget = renamer.RenamerUI()
    return widget
