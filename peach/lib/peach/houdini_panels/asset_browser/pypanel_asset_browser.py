from peach import pImp
from peach.pQt import img
from peach.pHoudini.panels import peach_main
pImp.reload(img, peach_main)


def onCreateInterface():
    widget = peach_main.PeachMainUI()
    return widget
