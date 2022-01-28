# ---------------------------------------------------------------------
# Copyright (c) 2022 Digital Peach Studio - Junru Tao
# This code is licensed under MIT license (see LICENSE.txt for details)
#                             *   *   *   *
# - Digital Peach Studio
# - Authors: Junru Tao
# - Contact: <junrtao.uk@gmail.com | junrutao@qq.com>
# - Website: digital-peach.company.site
# - Instagram: @digital.peach.studio
#
# [ File Description] - 2022.01.08 (Y.M.D)
#                             *   *   *   *
#   This File is for dev-houdini init.
#
# ---------------------------------------------------------------------

import os, shutil
from tkinter import END
import nocopy.houdini_util as hu
import hou


# [ @warning: Internal Init Script ]
hu.mode = "dev"
# packages to load
hu.peach_packages = []

# [ Getting the Peach Install Dir ]
hu.peach_dir = os.path.realpath("..")
hu.phoudini_dir = os.path.join(hu.peach_dir, "pHoudini/dev")
hu.working_dir = str(os.path.realpath("./dev/packages"))

# [ Run Functions ]
hu.setDirAndPrint()
hu.loadPeachEnvPackage()
hu.loadPeachPackages()

# [ Section: Loading Latest dev hdas ]
package_dir = hou.getenv("PEACH_PACKAGES_PATH")
packages = [f.path for f in os.scandir(package_dir) if f.is_dir()]
divider = "----------------------------------"

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class HDA(object):
    def __init__(self, hda_filename="", path="") -> None:
        super().__init__()
        self.long_name = hda_filename
        self.name = ""
        self.v_major = 0
        self.v_minor = 0
        self.path = path
        self.name, self.v_major, self.v_minor, ext = hda_filename.split(".")
        self.version = int(self.v_major) * 1000 + int(self.v_minor)
        
    def printInfo(self):
        hu.printMsg(". . [Found]: %s - v: %d" % (self.name, self.version))


def get_latest_hdas(hda_dir):
    hdas = dict()
    for f in os.scandir(hda_dir):
        if f.is_file() and f.name.endswith("hdalc"):
            hda_path = f.path
            hda_name = f.name
            hda = HDA(hda_name, hda_path)
            hda.printInfo()
            if hdas.get(hda.name):
                if hdas[hda.name].version < hda.version:
                    hdas[hda.name] = hda
            else:
                hdas[hda.name] = hda
    return hdas
            

hu.printMsg(divider)
hu.printMsg("scanning...")
for path in packages:
    hda_wip_dir = os.path.join(path, "wip\\hda")
    if os.path.exists(hda_wip_dir):
        hu.printMsg(divider)
        hu.printMsg("[HDA Wip path]: %s" % hda_wip_dir)
        # [2] Getting latest hdas
        hdas = get_latest_hdas(hda_wip_dir)
        hu.printMsg("[All Latest HDAs]: ")
        
        for _, a in hdas.items():
            hu.printMsg(">>>> Load HDA:" + bcolors.OKGREEN + " %s, %d" % (a.name, a.version) + bcolors.ENDC)
            # [3] load:
            hou.hda.installFile(hu.format_dir(a.path))