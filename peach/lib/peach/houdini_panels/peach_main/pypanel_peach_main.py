from peach.pQt.qHotel import QtWidgets
from peach import pImp
from peach.pQt import pq_ico
from peach.pHoudini.panels import ppp_peach_main
pImp.reload(pq_ico, ppp_peach_main)


def onCreateInterface():
    widget = ppp_peach_main.PeachMain()
    return widget
