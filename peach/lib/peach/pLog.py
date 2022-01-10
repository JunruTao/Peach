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
#   TODO: docstrings
#
# ---------------------------------------------------------------------
_enable_debug = True


def _print(**kwargs):
    """[ Internal Fn ] printing log
    """
    msg = kwargs["msg"]
    state = kwargs["state"]
    subject = kwargs["subject"]
    cls = kwargs["cls"]
    fn = kwargs["fn"]

    # /.Log format string
    log = "[ {cl}{fn}{st} ]: {tx}"

    if not isinstance(fn, str):
        # fn can be a custom name or a function
        fn = fn.__name__ if fn else ""

    if cls:
        # if class detected
        cls = cls.__class__.__name__
    else:
        # otherwise, look up subject.
        if subject:
            cls = subject
        else:
            cls = "pLog"
    # /.appending scope separators
    if len(fn):
        fn = "::" + fn
    if len(state):
        state = "::" + state
    print(log.format(cl=cls,
                     fn=fn,
                     st=state,
                     tx=msg))


def message(*args, sbj="", fn=None, cls=None, state=""):
    for arg in args:
        _print(msg=arg, subject=sbj, fn=fn, cls=cls, state=state)


def debug(*args, sbj="", fn=None, cls=None, f=False):
    if f or _enable_debug:
        for arg in args:
            _print(msg=arg, subject=sbj, fn=fn, cls=cls, state="debugMsg")


def warning(*args, sbj="", fn=None, cls=None):
    for arg in args:
        _print(msg=arg, subject=sbj, fn=fn, cls=cls, state="Warning")


def error(msg, sbj="", fn=None, cls=None):
    _print(msg=msg, subject=sbj, fn=fn, cls=cls, state="Error")
    raise RuntimeError(msg)
