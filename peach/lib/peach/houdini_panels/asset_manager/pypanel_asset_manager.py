from peach import pImp
from peach.pHoudini.panels import peach_asset_manager
pImp.reload(peach_asset_manager)


def onCreateInterface():
    widget = peach_asset_manager.AssetManagerUI()
    return widget
