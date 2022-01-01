import os

# GLOBAL VARIABLES
mode = "normal"

# $dirs:
peach_dir = ""
phoudini_dir = ""
working_dir = ""

# the peach env file:
peach_env_filename = "PeachEnv.json"

# houdini environment varibles setting:
henv_PEACH = "PEACH"
henv_PEACH_HOU = "PEACH_HOU"
henv_GLOBS = ["HIP", "JOB", "HSITE"]


# Convert dir to Houdini Format
def format_dir(dir):
    return dir.replace("\\","/")


# Print Function
def printMsg(msg):
    if mode != "dev":
        print("[ PEACH HOUDINI ]: {}".format(msg) )
    else:
        print("[ PEACH-DEV HOUDINI ]: {}".format(msg) )
        

# Loading Houdini.  
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

# Loading Hou Module
if(tryImportHou()):
    import hou


def setDirAndPrint():
    global peach_dir
    global phoudini_dir
    global working_dir
    
    peach_dir = format_dir(peach_dir)
    phoudini_dir = format_dir(phoudini_dir)
    working_dir = format_dir(working_dir)

    # [ Setting $PEACH in Houdini ]
    hou.putenv(henv_PEACH, peach_dir)
    printMsg("Peach Dir: %s" % peach_dir)
    printMsg("---set as '$%s'" % henv_PEACH)
    
    # [ Setting $PEACH in Houdini ]
    hou.putenv(henv_PEACH_HOU, phoudini_dir)
    printMsg("pHoudini Dir: %s" % phoudini_dir)
    printMsg("---set as '$%s'" % henv_PEACH_HOU)
    
    # [ Getting Workfing Directroy ]
    printMsg("Current Working Directory: %s" % working_dir)
    for env in henv_GLOBS:
        hou.putenv(env, working_dir)
        printMsg("---set '$%s' to this Working Directory" % env)


def loadPeachEnvPackage():
    # [ Loading Peach Env ]
    _peach_env_filepath = format_dir(os.path.join(phoudini_dir, peach_env_filename))
    
    printMsg("Loading Peach Env Package")
    try:
        hou.ui.loadPackage(_peach_env_filepath)
    except FileNotFoundError:
        printMsg("package: %s can not be found" % _peach_env_filepath)
    finally:
        printMsg("package Found: %s" % _peach_env_filepath)

 
def loadPeachPackages():
    # TODO loading other packages.
    # should read package from pconfig
    printMsg("Loading Peach Packages...")
    pass