# Batch From Textures to Shaders

```python

from maya import cmds
import glob, os


# # README: 
# # Note:
# # Files under directory should follow: `<name_whatever>_<map_type>.<ext>`

# [ Search Dir ] Where maps are stored:
# ////TODO
dir_to_scan = "C:/Users/1/Desktop/Test_Shaders"

# [ Map File Extention ] Change it to `jpg`, `tiff` etc.
# ////TODO
ext = "png"

# [ Maps ]
maps_dict = ["diffuse", "normal", "roughness", "specular"] # note: removed '"height" from list

# [ place2dUV -> File Connection reference directed ]
texture_connections = ['coverage', 
                       'translateFrame', 'rotateFrame', 
                       'mirrorU', 'mirrorV',
                       'stagger',
                       'wrapU', 'wrapV', 'repeatUV', 'rotateUV', 
                       'offset','noiseUV', 
                       'vertexUvOne','vertexUvTwo',
                       'vertexUvThree', 'vertexCameraOne']   
# [ place2dUV -> File Connection reference ]
texture_connections_out = {'outUV':'uv',
                           'outUvFilterSize': 'uvFilterSize'}


def create_file_node(name="", filepath=""):
    """Create Shader
    @param name: (str) Shader Name
    @param filepath: (str) File path to texture
    """
    file_node = cmds.shadingNode('file', name="FILE", asTexture=True)
    uv_node = cmds.shadingNode('place2dTexture', name="SHR_UV_%s" % name, asUtility=True)
    
    # create UV -> File node connections
    for n1nC in texture_connections:
        cmds.connectAttr("%s.%s"%(uv_node, n1nC), "%s.%s"%(file_node, n1nC))
        
    for out, to in texture_connections_out.items():
        cmds.connectAttr("%s.%s"%(uv_node, out), "%s.%s"%(file_node, to))
        
    # set map values:
    cmds.setAttr( '%s.fileTextureName' % file_node, filepath, type = "string")
    return file_node


def create_shader(name="shr"):
    """Create Shader
    @param name: (str) Shader Name
    """
    shader = cmds.shadingNode("standardSurface",asShader=True, n="SHR_%s" % name)
    shading_group = cmds.sets(renderable=True,noSurfaceShader=True,empty=True)
    
    for mp in maps_dict:
        map_dir = os.path.join(dir_to_scan, "%s_%s.%s" % (name, mp, ext) )
        if os.path.exists(map_dir):
            file_node = create_file_node("%s_%s" % (name, mp), map_dir)
            if mp == "diffuse":
                #connect file texture node to shader's color
                cmds.connectAttr('%s.outColor' % file_node, '%s.baseColor' % shader)
            elif mp == "normal":
                cmds.connectAttr('%s.outColor' % file_node, '%s.normalCamera' % shader)
            elif mp == "roughness":
                #connect file texture node to shader's color
                cmds.connectAttr('%s.outColorR' % file_node, '%s.diffuseRoughness' % shader)
                cmds.connectAttr('%s.outColorR' % file_node, '%s.specularRoughness' % shader)
            else:
                cmds.connectAttr('%s.outColorR' % file_node, '%s.%s' % (shader, mp))
                
    # connect shader to sg surface shader
    cmds.connectAttr('%s.outColor' % shader ,'%s.surfaceShader' % shading_group)
    
shader_names = []

# scan dir and log in shader names
for f in glob.glob(os.path.join(dir_to_scan, "*.%s" % ext)):
    f_path = f
    filename = os.path.basename(f)
    filename_b = filename.replace(".%s" % ext, "")
    if "diffuse" in filename_b:
        shader_names.append(filename_b.replace("_diffuse", ""))

print(shader_names)

# construct shaders
for SHR in shader_names:
    create_shader(SHR)
```