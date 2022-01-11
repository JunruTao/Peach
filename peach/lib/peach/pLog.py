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
    This is an internal function that print formatted logs following the
    format, msg is not optional, cls by default is 'pLog':

        "[ <cls>(::<fn>::<state>) ]: <msg>"

    @param kwargs:
        - msg: (str) message to sent
        - fn: (str/func) __::<fn>::__ can be function pointer or string
        - cls: (str/self) <cls>::__::__ can be class instance or string
        - state: (str) __::__(::<state>)
    """
    msg = kwargs["msg"]
    fn = kwargs["fn"]
    cls = kwargs["cls"]
    state = kwargs["state"]

    # /.Log format string
    log = "[ {cl}{fn}{st} ]: {tx}"

    if not isinstance(fn, str):
        # /.fn can be a custom name or a function
        fn = fn.__name__ if fn else ""

    if not isinstance(cls, str):
        # /.cls can be a custom string or class instance
        cls = cls.__class__.__name__ if cls else "pLog"

    # /.appending scope separators
    if len(fn):
        fn = "::" + fn
    if len(state):
        state = "::" + state
    # /.print log
    print(log.format(cl=cls,
                     fn=fn,
                     st=state,
                     tx=msg))


def message(*args, fn=None, cls=None, state=""):
    """Logging Function: "Message" to terminal/console.
     This is function that print formatted logs line-by-line
     following the format, *args is not optional, cls by
     default is 'pLog':

        "[ <cls>::<fn>::<state> ]: <msg>"

    @param args: arguments of (Any), messages
    @param fn: (str/func) can be function pointer or string
    @param cls: (str/self) can be class instance or string
    @param state: (str) custom state.
    @return: None
    """
    for arg in args:
        _print(msg=arg, fn=fn, cls=cls, state=state)


def debug(*args, fn=None, cls=None):
    """Logging Function: "Debug Message" to terminal/console.
     This is function that print formatted logs line-by-line
     following the format, *args is not optional, cls by
     default is 'pLog':

        "[ <cls>::<fn>::debugMsg ]: <msg>"

    @param args: arguments of (Any), messages
    @param fn: (str/func) can be function pointer or string
    @param cls: (str/self) can be class instance or string
    @return: None
    """
    if _enable_debug:
        for arg in args:
            _print(msg=arg, fn=fn, cls=cls, state="debugMsg")


def warning(*args, fn=None, cls=None):
    """Logging Function: "Warnings" to terminal/console.
     This is function that print formatted logs line-by-line
     following the format, *args is not optional, cls by
     default is 'pLog':

        "[ <cls>::<fn>::debugMsg ]: <msg>"

    @param args: arguments of (Any), messages
    @param fn: (str/func) can be function pointer or string
    @param cls: (str/self) can be class instance or string
    @return: None
    """
    for arg in args:
        _print(msg=arg, fn=fn, cls=cls, state="Warning")


def error(msg, fn=None, cls=None, e=None):
    """Logging Function: "Error" to terminal/console and raise.
     This is function that print formatted logs line-by-line
     following the format, *args is not optional, cls by
     default is 'pLog':

        "[ <cls>::<fn>::debugMsg ]: <msg>"

    @param msg: argument of (Any), messages
    @param fn: (str/func) can be function pointer or string
    @param cls: (str/self) can be class instance or string
    @param e: (Any) error exception object/message to throw.
    @return: None
    """
    _print(msg=msg, fn=fn, cls=cls, state="Error")
    if e:
        raise e
