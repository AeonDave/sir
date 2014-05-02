#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/sir)
See the file 'LICENSE' for copying permission
"""

import os ,sys 

VERSION = "0.1"
AUTHOR = "AeonDave"
DESCRIPTION = "SIR: Skype Ip Resolver"
SITE = "https://github.com/AeonDave/sir.git"
ISSUES_PAGE = ""
GIT_REPOSITORY = "git://github.com/AeonDave/sir.git"

PLATFORM = os.name
ROOTDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
LIBDIR = os.path.abspath(os.path.dirname(__file__))
PYVERSION = sys.version.split()[0]
