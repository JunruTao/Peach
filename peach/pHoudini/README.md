# pHoudini Tasks and Notes

----------------------------------------------------------------------------------
### :pen: [ Dcc Houdini ]
> specific section for Houdini

:heavy_minus_sign: **Houdini Init--Bootstrapping**
- [x] --- __`Houdini Package`__ Loading
    > This is something highly important. Use houdini package(.json) files should be able to configure houdini the way I wanted. Loading everything, configure path, plug-ins, otls, and extra.
    - [x] --- <s>Experiment with Houdini package. See how it can be utilised to load HDA and create workflows based on Dev, Project, User, and Shot etc.</s>
    - [x] --- <s>intergrate into dev pipeline.</s>


:heavy_minus_sign: **Houdini Package Develop**
- [x] --- <s>`HDA` Dev workflow design graph
    - [x] --- design a way develop `HDA`s in dev stage
    - [x] --- design the `HDA` shipment</s>
    
    > now The hda loading should be included in the package loading section.

- [x] --- <s>Test out Package Development Workflow</s>
    > This is important transit from the design chart to actual product.

- [x] --- <s>Split json files to separate files, using CMake configure_files to do it.</s>


:heavy_minus_sign: **Houdini General Tool Develop**
 - [x] --- <s>Test Houdini, create custom panel. (Asset Browser, etc, same goes with blender)</s>

<br><br>

-------

## Dated Tasks - :pen: [ Dcc Houdini ]

#### 2022.01.08:
- [ ] Node Renamer Tool
    > Node names should be based on several specific prefix conventions:
    > - `__IN__<name>` input node (null)
    > - `OUT_<name>` output node (null)
    > - `REF_<name>` reference node (for spare input or reference)
    > - `CTR_<name>_<opt.function>` nodes has user controls, to linked to HDA interface.
    > - `DVR_<name>_<opt.function>` nodes that driven by local nodes(same level)
    > - `PRC_<name>_<opt.function>` nodes the calculate procedurally, no need for extra parameter inputs.
    > - ... <sup>(append here)</sup>

- [x] Firgure out HDA dev in packages, and distribution.
- [ ] `Dev tool package`. set things like renamer, set project, save dev file, hda saving, etc.