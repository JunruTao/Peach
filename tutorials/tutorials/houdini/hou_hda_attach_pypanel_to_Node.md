# * Tricks: Attach a PyPanel to A HDA Node:
 
In Node's OnCreate module:
```python

def selection_changed(**kwargs):
    interface = hou.pypanel.interfaces()["asset_browser"]
    if kwargs['change_type'] == hou.appearanceChangeType.Pick:
        sel = kwargs['node'].isSelected()
        paneTbs = hou.ui.paneTabs()
        for pt in paneTbs:
            if sel:
                if pt.type() == hou.paneTabType.Parm:
                    ppt = pt.setType(hou.paneTabType.PythonPanel)
                    ppt.setActiveInterface(interface)
                    break
            else:
                if pt.type() == hou.paneTabType.PythonPanel:
                    if pt.activeInterface() == interface:
                        ppt = pt.setType(hou.paneTabType.Parm)
                        break


# install and link callback to this node:
node_.addEventCallback((hou.nodeEventType.AppearanceChanged,), selection_changed)
```