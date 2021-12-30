import os


def printMsg(msg):
    print("[ PEACH HOUDINI ]: {}".format(msg) )


# [ Loading Hou Module ]
printMsg("Running pHoudini...")
printMsg("Try importing hou...")

# [ Getting the Peach Install Dir ]
peach_dir = os.path.realpath(".")
printMsg("Peach Dir: %s" % peach_dir)
pHoudini_dir = os.path.join(peach_dir, "pHoudini")
printMsg("pHoudini Dir: %s" % pHoudini_dir)

try:
    import hou
except ImportError:
    raise "Can not Import <hou> module"
finally:
    printMsg("Module <hou> import successfully")

# [ Loading Peach Env ]
peach_env_filepath = os.path.join(pHoudini_dir, "PeachEnv.json")
printMsg("Loading Peach Env Package")

# [ Setting $PEACH in Houdini ]
hou.putenv("PEACH", peach_dir)
# [ Setting $PEACH in Houdini ]
hou.putenv("PEACH_HOU", pHoudini_dir)

try:
    hou.ui.loadPackage(peach_env_filepath)
except FileNotFoundError:
    printMsg("package: %s can not be found" % peach_env_filepath)
finally:
    printMsg("package Found: %s" % peach_env_filepath)
    
# Setting the global path.
wd = str(os.path.realpath(".."))
hou.putenv("HIP", wd)
hou.putenv("JOB", wd)