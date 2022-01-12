from peach import pImp
from peach.pQt import pq_ico
from peach.pHoudini.panels import peach_main
pImp.reload(pq_ico, peach_main)


def onCreateInterface():
    widget = peach_main.PeachMainUI()
    return widget
