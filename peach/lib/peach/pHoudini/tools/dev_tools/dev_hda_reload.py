#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (c) 2022 Digital Peach Studio - Junru Tao
# This code is licensed under MIT license (see LICENSE.txt for details)
#                            *   *   *   *
# [ Info ] - Digital Peach Studio
# - Authors: Junru Tao
# - Contact: <junrtao.uk@gmail.com | junrutao@qq.com>
# - Website: digital-peach.company.site
# - Instagram: @digital.peach.studio
# ---------------------------------------------------------------------
# [ File Name ] dev_hda_reload.py@python
# [ File Description ] - 2022.02.02 (Y.M.D) - 19:12
#                            *   *   *   *
#
#   This script contains HDA reloading functions (dev only.)
#
# ---------------------------------------------------------------------
from peach import pLog, pDir
import hou

h_package_dir = pDir.join(pDir.getPeachHouDir(), "dev/packages")
packages = pDir.listdir(h_package_dir)


class HDA(object):
    def __init__(self, hda_filename="", path_="") -> None:
        super().__init__()
        self.long_name = hda_filename
        self.name = ""
        self.v_major = 0
        self.v_minor = 0
        self.path = path_
        self.name, self.v_major, self.v_minor, ext = hda_filename.split(".")
        self.version = int(self.v_major) * 1000 + int(self.v_minor)

    def printInfo(self):
        pLog.debug(". . [Found]: %s - v: %d" % (self.name, self.version))


def get_latest_hdas(hda_dir):
    hdas_ = dict()
    for f in pDir.listfiles(hda_dir):
        if f.endswith("hdalc"):
            hda_path = f
            hda_name = pDir.fileName(f)
            hda = HDA(hda_name, hda_path)
            hda.printInfo()
            if hdas_.get(hda.name):
                if hdas_[hda.name].version < hda.version:
                    hdas_[hda.name] = hda
            else:
                hdas_[hda.name] = hda
    return hdas_


def load():
    pLog.debug("scanning...")
    for path in packages:
        hda_wip_dir = pDir.join(path, "wip/hda")
        if pDir.exists(hda_wip_dir):
            if len(pDir.listfiles(hda_wip_dir)):
                pLog.debug("[HDA Wip path]: %s" % hda_wip_dir)
                # [2] Getting latest hdas
                hdas = get_latest_hdas(hda_wip_dir)
                pLog.debug("[All Latest HDAs]: ")

                for _, a in hdas.items():
                    pLog.debug(">>>> Load HDA: %s, %d" % (a.name, a.version))
                    # [3] load:
                    hou.hda.installFile(pDir.pathSlashConvert(a.path))
