# Houdini Network Image

## 1. Creation Simple:

```python
editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
image = hou.NetworkImage()
image.setPath('$HFS/houdini/pic/Mandril.pic')
image.setRect(hou.BoundingRect(0, 0, 5, 5))
editor.setBackgroundImages([image])

```

## 2. Link Network Image to Node:
```python
relativeToPath() → str 
```
> Images can be tied to network items such as nodes, network boxes, or sticky notes. This method returns the path to the network item to which this image is tied (or an empty string if its location is not relative to any network item).


## 3. Very Good Example
```python
import hou
import os
import subprocess
import nodegraphutils as utils
from time import gmtime, strftime

widthRatio = 4                      # change to make screenshot bigger or smaller, this is ~x4 node width

def takeScreenShot(savePath):
    '''change to your preferred capture app /!\ no error checking for now '''
    subprocess.check_call([r"C:\Users\me\MiniCap.exe","-captureregselect","-save",savePath,"-exit"])

def removeBackgroundImage(**kwargs):
    ''' erases bg image from tuples of backgroundImages() if it can find it, updates bg '''
    deletingNode = [x[1] for x in  kwargs.items()][0]
    image = deletingNode.parm('houdinipath').eval()
    editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    backgroundImagesDic = editor.backgroundImages()
    backgroundImagesDic = tuple(x for x in backgroundImagesDic if x.path() != image)
    editor.setBackgroundImages(backgroundImagesDic)
    utils.saveBackgroundImages(editor.pwd(), backgroundImagesDic)

def changeBackgroundImageBrightness(event_type,**kwargs):
    ''' changes brightness/visibility if template or bypass flags are checked -- its poorly written/thought but i was tired'''
    nullNode = [x[1] for x in  kwargs.items()][0]
    image = nullNode.parm('houdinipath').eval()
    brightness = 1.0
    if nullNode.isBypassed():
        brightness = 0.0
    elif nullNode.isTemplateFlagSet():
        brightness = 0.5
    editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    backgroundImagesDic = editor.backgroundImages()
    i = 0
    for item in backgroundImagesDic:
        if item.path() == image:
            backgroundImagesDic[i].setBrightness(brightness)
            break
        i = i + 1
    editor.setBackgroundImages(backgroundImagesDic)
    utils.saveBackgroundImages(editor.pwd(), backgroundImagesDic)
    
#generate unique(ish) path for screenshot
timestamp = strftime('%Y%m%d_%H%M%S', gmtime())
hipname = str(hou.getenv('HIPNAME'))
hippath = str(hou.getenv('HIP')) + '/screenshots'
screenshotName = hipname + '.' + timestamp + '.png'
systempath = hippath + '\\' + screenshotName
houdinipath = '$HIP/screenshots/'+screenshotName

#take screenshot with capture region
takeScreenShot(systempath)


#set up background image plane
editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
image = hou.NetworkImage()
image.setPath(houdinipath)
sel = hou.selectedNodes()
nullNode = ''

if sel:
    lastSel = sel[-1]
    nullNode = lastSel.parent().createNode('null','screenshot')
    if lastSel.outputConnections():
        nullNode.setInput(0,lastSel)                   

else:
    nullNode = editor.pwd().createNode('null','screenshot') 
    nullNode.moveToGoodPosition()
    lastSel = nullNode

#configure image plane placement
nullNode.setUserData('nodeshape','task')
nullNode.setPosition(lastSel.position())
nullNode.setColor(hou.Color(.3,.3,.3))
nullNode.move([lastSel.size()[0]*2,-lastSel.size()[1]*2])

rez = hou.imageResolution(systempath)
ratio = 1.0*rez[1]/rez[0]
rect = hou.BoundingRect(0,-lastSel.size()[1]*1.1,widthRatio,-widthRatio*ratio-lastSel.size()[1]*1.1)
image.setRelativeToPath(nullNode.path())
image.setRect(rect)

#following is adding a spare parm with image path to be able to know which node corresponds to which background image
#could have used a user attribute or relativeToPath() and smarter logic but it works and it helps me visualize filepath

hou_parm_template_group = hou.ParmTemplateGroup()
hou_parm_template = hou.LabelParmTemplate("houdinipath", "Label", column_labels=(['\\'+houdinipath]))
hou_parm_template.hideLabel(True)
hou_parm_template_group.append(hou_parm_template)
nullNode.setParmTemplateGroup(hou_parm_template_group)


#attach a function that deletes the background image plane if the corresponding node is deleted (faster than doing it by hand)
nullNode.addEventCallback((hou.nodeEventType.BeingDeleted,), removeBackgroundImage)

#attach a function to change visibility or opacity if corresponding node flags are changed
nullNode.addEventCallback((hou.nodeEventType.FlagChanged,), changeBackgroundImageBrightness)

#add image to network background
backgroundImagesDic = editor.backgroundImages()
backgroundImagesDic = backgroundImagesDic + (image,)
editor.setBackgroundImages(backgroundImagesDic)
utils.saveBackgroundImages(editor.pwd(), backgroundImagesDic)
```

### 3.1 * Reference
> https://forums.odforce.net/topic/32581-networkimage/