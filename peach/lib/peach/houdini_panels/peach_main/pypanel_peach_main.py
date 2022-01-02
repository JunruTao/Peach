from hutil.Qt import QtWidgets
from peach.pHoudini import test

def onCreateInterface():
    test.Foo()
    widget = QtWidgets.QLabel('Hello World!')
    return widget