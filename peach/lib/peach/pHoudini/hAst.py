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
# [ File Name ] hAst.py@python
# [ File Description ] - 2022.02.05 (Y.M.D) - 17:24
#                            *   *   *   *
#
#   This script contains houdini Ast functions
#
# ---------------------------------------------------------------------
from peach import pAst


def export_layout(node_out=None, json_path=""):
    if node_out and json_path:
        if json_path.endswith(".json"):
            json_path = json_path.replace(".json", ".{}".format(pAst.LAY_EXT))
        geo = node_out.geometry()

        def chunks(lst, n):
            """Yield successive n-sized chunks from lst."""
            for j in range(0, len(lst), n):
                yield lst[j:j + n]

        ast_instance_data = geo.attribValue("ast_instance_data")
        data_out = dict()
        for ln, path_ in ast_instance_data.items():
            data_out[ln] = dict()
            data_out[ln]["path"] = path_
            data_out[ln]["instances"] = []

        # getting all the transforms:
        t = geo.primFloatAttribValues("t")
        r = geo.primFloatAttribValues("r")
        s = geo.primFloatAttribValues("s")
        asset_name = geo.primStringAttribValues("ast_longname")

        # get them into 3 sized vector arrays
        t = list(chunks(t, 3))
        r = list(chunks(r, 3))
        s = list(chunks(s, 3))

        for i in range(0, len(geo.prims())):
            if data_out.get(asset_name[i]):
                data = {"order": "trs",
                        "t": (t[i][0], t[i][1], t[i][2]),
                        "r": (r[i][0], r[i][1], r[i][2]),
                        "s": (s[i][0], s[i][1], s[i][2])}
                data_out[asset_name[i]]["instances"].append(data)

        import json
        json_str = json.dumps(data_out, indent=4)
        with open(json_path, 'w') as outfile:
            outfile.write(json_str)
