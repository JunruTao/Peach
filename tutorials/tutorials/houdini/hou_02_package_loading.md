# Loading Custom Houdini Packages

Houdini Package, the main usage will be loading: `python modules`, `hda`, `shelve` etc. More instructions can be found on the reference section.

Now here's a simple example how you can you create a plug-in(houdini package). follow the instructions.

### 1. Create a your package content:
all the content should be allocated under specificly named folder structures:


- **_`${PackageDir}`_**
    - __`desktop`__
        > where all the custom `.desk` files sit
    - __`python3.7libs`__
        > :v: This is the place where you should store you python modules. Houdini is very name sensitive on this matter, as you should always keep the name like `python3.7libs` or older version will be `python2.7libs`.
    - __`scenes`__
        > you can simply place your demo, construction, template hip files in here.
    - __`toolbar`__
        > put the custom shelves, `.shelf` extension.
    - __`viewer_handles`__
        > python viewer states handles, python files
    - __`viewer_states_`__
        > python viewer states, python files
    - __`python_panels`__
        > `.pypanel` file in `xml` format. (need more info on this)
    - __`vex/include`__
        > `.h` c/c++ header files, 
    - __`dso`__
        > `.so`/`.dll`, `.pdb` library files, dynamic linked libraries will be sits 
    - __`geo`__
        > store some handy geometries here. (`.bgeo` files)
    - __`otls`__
        > :v: load custom HDAs here. you can separate them into differen packages if you want.

### 2. Create Package File - json
Create a file, name it something like `myPackage.json`, you can store it right next to your content folder if you like:
```
+ packages_root 
    +--- myPackage
    |       +----- python3.7libs
    |       +----- otls
    |       +----- toolbar
    |       
    +--- myPackage.json
```

inside `myPackage.json`, simply create something like this:
```json
{
    "path": "/package_root/myPackage"
}
```
and that's it, the very basic version.

### 3. Loading Your Package

:one:

the most simpiest way will be loading everything from your `package browser`. in houdini, open package browser, `file` &rarr; `load package...`. Select your package json file. 

Then you should see your package loaded in the packages tree. open it up. you should see all the recognised files.


:two:

Or, automate this process by calling python functions.

```python
hou.ui.loadPackage("/package_root/myPackage.json")
```

and now try loading your python modules or search for installed hdas.

There's other useful functions related to this.

```python
# reload/refreshing
hou.ui.reloadPackage("/package_root/myPackage.json")
# unloading
hou.ui.unloadPackage("/package_root/myPackage.json")
```

| :warning: On Windows: make sure replace all the file path `\` with `/`, when assigning those path either in python script or in the package json files.<br>This is very important as Houdini would not recognise the path with `\` as it is not a string literal. <br>(try `\\` in the code instead as well, however strongly recommend using foreslash)|
|:---|

---
### references:
- [Sidefx Configuring Houdini](https://www.sidefx.com/docs/houdini/basics/config.html)
- [Sidefx Houdini Packages](https://www.sidefx.com/docs/houdini/ref/plugins.html)
- [python hou.ui.loadPackage](https://www.sidefx.com/docs/houdini/hom/hou/ui.html#loadPackage)