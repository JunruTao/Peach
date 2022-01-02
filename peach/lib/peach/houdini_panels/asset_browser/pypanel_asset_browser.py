from hutil.Qt import QtWidgets
from peach.pUtil import test

def onCreateInterface():
    test.Foo2()
    widget = QtWidgets.QLabel('Asset Browser New')
    return widget