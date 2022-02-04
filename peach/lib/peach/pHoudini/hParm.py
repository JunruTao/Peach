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
# [ File Name ] hParm.py@python
# [ File Description ] - 2022.02.04 (Y.M.D) - 14:58
#                            *   *   *   *
#
#   This script contains houdini parameter functions
#
# ---------------------------------------------------------------------
import hou
import math


def menu_get_selected_token(parm):
    """
    [ Parm::Menu ] get selected token
    <br>
    <br><code>  # In a parameter callback script...</code>
    <br><code>  token = get_selected_token(kwargs["parm"])</code>

    @param parm: (hou.Parm)
    @return: (Any) token value
    """
    # Read which item is currently selected
    selected = parm.eval()
    # Get the list of menu tokens from the parameter template
    tokens = parm.menuItems()
    # Return the token corresponding to the selected item
    return tokens[selected]


def menu_get_multi_selected_tokens(parm):
    """
    [ Parm::Menu ] get selected tokens (button script)
    <br>
    <br><code>  # In a parameter callback script...</code>
    <br><code>  token = get_selected_token(kwargs["parm"])</code>

    @param parm: (hou.Parm)
    @return: (Any) token value
    """
    # Read which item is currently selected
    bitfield = parm.eval()
    # Get the list of menu tokens from the parameter template
    tokens = parm.menuItems()
    # Return the token corresponding to the selected item
    return [token for n, token in enumerate(tokens) if bitfield & (1 << n)]
