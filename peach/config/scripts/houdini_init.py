import os
import houdini_util as hu
import hou


# [ This is the Release Version ]
hu.mode = "normal"

# [ Getting the Peach Install Dir ]
hu.peach_dir = os.path.realpath(".")
hu.phoudini_dir = os.path.join(hu.peach_dir, "pHoudini")
hu.working_dir = str(os.path.realpath(".."))

# [ Run Functions ]
hu.setDirAndPrint()
hu.loadPeachEnvPackage()
hu.loadPeachPackages()