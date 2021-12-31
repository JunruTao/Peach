# ![icon](icons/25w/icon_peach_x25.png) Peach Dev Tasks

**Author: Junru Tao** <br>
> Note: In order to keep a clear mind of this project, the task list will be the main section of documenting ToDos of this project. All higher level documentation should be created in the `peach_dev`'s main README. 


<br><br> 

| - Markers Atlas |
|:---|
|Use :warning: __`TODO:`__ to  add more noticable checkbox sections . . .|
|Use: <sup>__`[DONE]`__</sup> to express recently done TODOs . . . |





<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>

## :pencil: TASK LIST
### :pen: [ Design ]
> anything that need an abstract way of thinking :brain:. need to think outside the box, by drawing diagrams, brainstorming and connecting all those dots. 

- :purple_square: **Peach Idea Roadmap**
    - [x] --- a rough sketch of what it could be <sup>(diagram)</sup>
    - [ ] --- :warning: __`TODO:`__ a rough sketch of the Peach API <sup>(cpp/python)</sup>

- :purple_square: **Developement workflow**
    - [x] --- basic work flow diagram <sup>(diagram)</sup>
    - [x] --- document the boostrapping mechanism in doc and diagrams





<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>

----------------------------------------------------------------------------------
### :pen: [ Project Management ]
> anything related to folder structure, development package management, cmake and building.

- :orange_square: **Peach Dev Folder Structure**
- :orange_square: **Peach Install Target File Structure**
    - [x] ---bootstrap and config/config files
- :red_square: **Peach Dev CMake**
    - [x] Build target test
        - [x] --- Main CMake test
        - [x] --- Subdir CMake and build mechanism test
        - [ ] --- :warning: __`TODO:`__ disable other project from building. therefore only build selected one. (should be given an option to pass to cmake or build tools)
    - [ ] Test Passing Version information to Precompiler (1/2)
        - [x] --- bootstrapper [ done ]
        - [ ] --- passing to python/a configuration file?/or folder name?    
    - [x] <sup>__`[DONE]`__</sup>  Move current bootstrap's config install folder to master dir. After moving bootstrap's config folder, change cmake list





<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>

----------------------------------------------------------------------------------
### :pen: [ App: Dcc Bootstrapping ]
> specific section for the bootstrap apps.

- :green_square: **Peach Bootstrap** <sup>(c++)</sup>
    - [x] --- Build executable <sup>(cmake, gcc, c++)</sup>
    - [x] --- Bootstrap blender/Houdini, <sup>(c++/shell)</sup>
    - [x] --- create `.pconfig` file format
    - [x] --- run Houdini init script setup <sup>(py)</sup>
    - [x] --- run Blender init script setup <sup>(py)</sup>
    - [x] --- <sup>__`[DONE]`__</sup> Create `PowerShell` version for the `startup_dcc_init.sh`. Therefore the linux user and windows user should have the capabilities to bootstrap the apps without installing any new dependent softwares such as git-bash.





<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>

----------------------------------------------------------------------------------
### :pen: [ Dcc Blender ]
> specific section for blender

- :green_square: **Peach Blender**





<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>

----------------------------------------------------------------------------------
### :pen: [ Dcc Houdini ]
> specific section for Houdini

:green_square: **Houdini Init--Bootstrapping**
- [x] --- __`Houdini Package`__ Loading
    > This is something highly important. Use houdini package(.json) files should be able to configure houdini the way I wanted. Loading everything, configure path, plug-ins, otls, and extra.
    - [x] --- Experiment with Houdini package. See how it can be utilised to load HDA and create workflows based on Dev, Project, User, and Shot etc.
    - [x] --- intergrate into dev pipeline.


:green_square: **Houdini Package Develop**
- [x] --- <s>`HDA` Dev workflow design graph
    - [x] --- design a way develop `HDA`s in dev stage
    - [x] --- design the `HDA` shipment</s>
    
    > now The hda loading should be included in the package loading section.

- [x] --- Test out Package Development Workflow
    > This is important transit from the design chart to actual product.




<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>

----------------------------------------------------------------------------------
### :pen: [ API Design ]
> specific section for Houdini

- :red_circle: **Peach Python**





<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>

----------------------------------------------------------------------------------
### :pen: [ *Misc. ]
> anything else. however including the icons, image resource and documentations.

- :yellow_square: **Peach Icon Designs**
    - [x] --- Main Icon
    - [x] --- Variant/Folder Icons
    - [x] --- batch exporting/management <sup>(.Ai)</sup>
    - [x] --- batch convert to `.ico`/generate `.rc` <sup>(py, shell)</sup>

- :yellow_square: **Documentation Tools**
    - [x] --- date-time based changeLogs auto generator. create new changeLog files according to the date, and append new changes to that date's changeLog with timestamps. <sup>(py, shell)</sup>
    - [x] --- automatically open `code` after the shell execution. open up the change log file that needed to be editied.
    - [x] --- <sup>__`[DONE]`__</sup> Auto append sub change-logs to a _main_ change-log, as `Markdown/html hyperlinks`.
    (maybe override the same file each time)

    - [ ] :warning: __`TODO:`__ split change log into months, and format main change log into sub sections.

<br>
<br>
<br>
<p align=middle> <sup><sup><i>Peach</i></sup></sup></p>
<br>


