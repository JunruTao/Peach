# ![icon](icons/25w/icon_peach_x25.png) Peach Dev Tasks

**Author: Junru Tao** <br>
Note: In order to keep a clear mind of this project, the task list will be the main section of documenting ToDos of this project. All higher level documentation should be created in the `peach_dev`'s main README. 

## :pencil: TASK LIST
### :pen: [ Design ]
> anything that need an abstract way of thinking :brain:. need to think outside the box, by drawing diagrams, brainstorming and connecting all those dots.

- :purple_square: **Peach Idea Roadmap**
    - [x] a rough sketch of what it could be <sup>(diagram)</sup>

- :purple_square: **Developement workflow**
    - [x] basic work flow diagram <sup>(diagram)</sup>
    
    <br> :warning: __`TODO:`__
    - [ ] **document the boostrapping mechanism in doc and diagrams.**
    - [ ] **HDA Dev workflow**
        - [ ] **design a way develop hdas in dev stage**
        - [ ] **design the hda shipment**

-----------------------------------------
### :pen: [ Project Management ]
> anything related to folder structure, development package management, cmake and building.

- :orange_square: **Peach Dev Folder Structure**
- :orange_square: **Peach Install Target File Structure**
    - [x] bootstrap and config/config files
- :red_square: **Peach Dev CMake**
    - [x] Build target
    - [x] Main CMake
    - [x] Subdir CMake and build mechanism
        - [ ] :warning: __`TODO:`__ disable other project from building. therefore only build selected one. (should be given an option to pass to cmake or build tools)
    - [ ] Test Passing Version information to Precompiler (1/2)
        - [x] bootstrapper [ done ]
        - [ ] passing to python/a configuration file?/or folder name?    

    - [ ] :warning: __`TODO:`__ Move current bootstrap's config install folder to master dir. After moving bootstrap's config folder, change cmake list

-----------------------------------------
### :pen: [ App: Dcc Bootstrapping ]
> specific section for the bootstrap apps.

- :green_square: **Peach Bootstrap** <sup>(c++)</sup>
    - [x] Build executable <sup>(cmake, gcc, c++)</sup>
    - [x] Bootstrap blender/Houdini, <sup>(c++/shell)</sup>
    - [x] create `.pconfig` file format
    - [x] run Houdini init script setup <sup>(py)</sup>
    - [x] run Blender init script setup <sup>(py)</sup>

-----------------------------------------
### :pen: [ Dcc Blender ]
> specific section for blender

- :green_square: **Peach Blender**


-----------------------------------------
### :pen: [ Dcc Houdini ]
> specific section for Houdini

- :green_square: **Peach Houdini**



-----------------------------------------
### :pen: [ *Misc. ]
> anything else. however including the icons, image resource and documentations.

- :yellow_square: **Peach Icon Designs**
    - [x] Main Icon
    - [x] Variant/Folder Icons
    - [x] batch exporting/management <sup>(.Ai)</sup>
    - [x] batch convert to `.ico`/generate `.rc` <sup>(py, shell)</sup>

- :yellow_square: **Documentation Tools**
    - [x] date-time based changeLogs auto generator. create new changeLog files according to the date, and append new changes to that date's changeLog with timestamps. <sup>(py, shell)</sup>
    
    <br> :warning: __`TODO:`__
    - [ ] **Auto append sub change-logs to a _main_ change-log, as `Markdown/html hyperlinks`.
    (maybe override the same file each time)**
