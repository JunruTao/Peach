import os


def printMsg(msg):
    print("[DEV HOUDINI]: {}".format(msg) )
    
printMsg("Running pHoudini-DEV...")
printMsg("Try importing hou...")

try:
    import hou
except ImportError:
    raise "Can not Import <hou> module"
finally:
    printMsg("Module <hou> import successfully")

peach_env_filepath = "./dev/peach_env.json"
printMsg("Loading Peach Env Package")

try:
    hou.ui.loadPackage(peach_env_filepath)
except FileNotFoundError:
    printMsg("package: %s can not be found" % peach_env_filepath)
