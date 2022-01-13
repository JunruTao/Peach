#!/usr/bin/python
import os, shutil

base_path = os.path.dirname(os.path.dirname(__file__))
package_dir = os.path.join(base_path, "packages")  # executed in sh script
packages = [f.path for f in os.scandir(package_dir) if f.is_dir()]
empty_dir = True
divider = "----------------------------------"

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
        print("---[HDA::path]: ", self.path)
        # print("---> name: {0}\n---> major_version: {1}\n---> minor_version: {2}".format(
        #         self.name,
        #         self.v_major,
        #         self.v_minor
        #     ))
        print("---> VERSION_INT: %d" % self.version)
        print(divider)


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
            

print(divider)
print("scanning...")
for path in packages:
    hda_wip_dir = os.path.join(path, "wip\\hda")
    if os.path.exists(hda_wip_dir):
        print(divider)
        print("[HDA Wip path]: %s" % hda_wip_dir)
        
        # [1] Emty Otls, update with new empty dir
        otl_dir = os.path.join(path, "pdev_otls")
        if empty_dir:
            print("---[OS::Dir] Empty Filepath, create New `otls` dir")
            if os.path.exists(otl_dir):
                shutil.rmtree(otl_dir)    
            os.makedirs(otl_dir)
        # [2] Getting latest hdas
        hdas = get_latest_hdas(hda_wip_dir)
        print("[All Latest HDAs]: ")
        
        for _, a in hdas.items():
            print(">>>> to copy: ", a.name, a.version)
            
            # copy HDA to this packages otls folder
            shutil.copy(a.path, os.path.join(otl_dir, a.long_name))