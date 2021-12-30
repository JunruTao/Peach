import os

# GLOBAL VARIABLES
mode = "normal"
peach_dir = ""
phoudini_dir = ""
peach_env_filename = "PeachEnv.json"

working_dir = ""
henv_PEACH = "PEACH"
henv_PEACH_HOU = "PEACH_HOU"
henv_GLOBS = ["HIP", "JOB", "HSITE"]

# FUNCTIONS
def printMsg(msg):
    if mode != "dev":
        print("[ PEACH HOUDINI ]: {}".format(msg) )
    else:
        print("[ PEACH-DEV HOUDINI ]: {}".format(msg) )
        
        
def tryImportHou():
    # [ Loading Hou Module ]
    printMsg("Running pHoudini...")
    printMsg("Try importing module <hou>...")
    try:
        import hou
    except ImportError:
        print("Can not Import <hou> module")
        return False
    finally:
        printMsg("Module <hou> import successfully")
    return True


if(tryImportHou()):
    import hou


def setDirAndPrint():
    
    # //somespace
    printMsg("...")
    # [ Setting $PEACH in Houdini ]
    hou.putenv(henv_PEACH, peach_dir)
    printMsg("Peach Dir: %s" % peach_dir)
    printMsg("---set as '$%s'\n" % henv_PEACH)
    
    # [ Setting $PEACH in Houdini ]
    hou.putenv(henv_PEACH_HOU, phoudini_dir)
    printMsg("pHoudini Dir: %s" % phoudini_dir)
    printMsg("---set as '$%s'\n" % henv_PEACH_HOU)
    
    # [ Getting Workfing Directroy ]
    printMsg("Current Working Directory: %s" % working_dir)
    for env in henv_GLOBS:
        hou.putenv(env, working_dir)
        printMsg("---set '$%s' to this Working Directory" % env)
    printMsg("...")
    
def loadPeachEnvPackage():
    # [ Loading Peach Env ]
    _peach_env_filepath = os.path.join(phoudini_dir, peach_env_filename)
    printMsg("Loading Peach Env Package")
    try:
        hou.ui.loadPackage(_peach_env_filepath)
    except FileNotFoundError:
        printMsg("package: %s can not be found" % _peach_env_filepath)
    finally:
        printMsg("package Found: %s" % _peach_env_filepath)