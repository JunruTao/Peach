import os
import nocopy.houdini_util as hu
import hou


# [ @warning: Internal Init Script ]
hu.mode = "dev"
# packages to load
hu.peach_packages = ["PeachPy", ]

# [ Getting the Peach Install Dir ]
hu.peach_dir = os.path.realpath("..")
hu.phoudini_dir = os.path.join(hu.peach_dir, "pHoudini/dev")
hu.working_dir = str(os.path.realpath("./dev/packages"))

# [ Run Functions ]
hu.setDirAndPrint()
hu.loadPeachEnvPackage()
hu.loadPeachPackages()