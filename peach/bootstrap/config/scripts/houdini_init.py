
print("loading houdini init script..")
print("hello world")
import hou
print(hou)

node = hou.node("/obj").createNode("geo")
node.setName("my_first_geo1")