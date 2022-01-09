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
# [ File Name ] pDm.py@python
# [ File Description ] - 2022.01.09 (Y.M.D) - 17:01
#                            *   *   *   *
#
#   Peach Debug Manager. Handling debug message printing.
#
# ---------------------------------------------------------------------
_enable_debug = True


def _print(**kwargs):
    """[ Internal Fn ] printing log
    """
    msg = kwargs["msg"]
    state = kwargs["state"]
    subject = kwargs["subject"]
    # [ Log format string ]
    log = "[ pLog{sb}{st} ]: {tx}"
    if len(subject):
        subject = "::" + subject
    if len(state):
        state = "::" + state
    print(log.format(sb=subject, st=state, tx=msg))


def message(*args, subject="", fn=None):
    subject = fn.__name__ if fn else subject
    for arg in args:
        _print(msg=arg, subject=subject, state="")


def debug(*args, subject="", fn=None, force=False):
    subject = fn.__name__ if fn else subject
    if force or _enable_debug:
        for arg in args:
            _print(msg=arg, subject=subject, state="debugMsg")


def warning(*args, subject="", fn=None):
    subject = fn.__name__ if fn else subject
    for arg in args:
        _print(msg=arg, subject=subject, state="Warning")


def error(msg, subject="", fn=None):
    subject = fn.__name__ if fn else subject
    _print(msg=msg, subject=subject, state="Error")
    raise RuntimeError(msg)
