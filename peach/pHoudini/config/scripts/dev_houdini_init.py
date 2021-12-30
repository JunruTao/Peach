import os
import util_x.houdini_util as hu
import hou

hu.mode = "dev"

# [ Getting the Peach Install Dir ]
hu.peach_dir = os.path.realpath("..")
hu.phoudini_dir = os.path.join(hu.peach_dir, "pHoudini/dev")
hu.working_dir = str(os.path.realpath("./sandbox"))
hu.setDirAndPrint()
hu.loadPeachEnvPackage()
