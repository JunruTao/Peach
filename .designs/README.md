# DESIGN and PROJECT tasks

### :pen: [ Design ]
> anything that need an abstract way of thinking :brain:. need to think outside the box, by drawing diagrams, brainstorming and connecting all those dots. 

- :purple_square: **Peach Idea Roadmap**
    - [x] --- a rough sketch of what it could be <sup>(diagram)</sup>
    - [ ] --- :warning: __`TODO:`__ a rough sketch of the Peach API <sup>(cpp/python)</sup>

- :purple_square: **Developement workflow**
    - [x] --- basic work flow diagram <sup>(diagram)</sup>
    - [x] --- document the boostrapping mechanism in doc and diagrams


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
        - [x] --- disable other project from building. <s>therefore only build selected one. (should be given an option to pass to cmake or build tools)</s>
            > Currently using a few set variables to control it.(see main cmakelist)
    - [x] Test Passing Version information to Precompiler (1/2)
        - [x] --- bootstrapper [ done ]
        - [x] --- passing to python/a configuration file?/or folder name? [ done ]
            > Solution: use `congifure_file` in cmake to replate strings.
    - [x] Move current bootstrap's config install folder to master dir. After moving bootstrap's config folder, change cmake list
