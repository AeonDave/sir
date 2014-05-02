#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/sir)
See the file 'LICENSE' for copying permission
"""

import sys, os, core, settings

from lib.logger import logger

__version__ = settings.VERSION
__author__ = settings.AUTHOR

def header():
    os.system("clear")
    
    print ""
    print "         =============================================== "
    print "        |  Skype Ip Resolver v{0}\t\t\t|".format(__version__)
    print "        |  by {0}\t\t\t\t\t|".format(__author__)
    print "         =============================================== "
    print ""

def showhelp():
    print """
    Usage: python sir.py [Name] [Output]

    Target:
        -n, --name SkypeName      Target Skype Name
        
    Options:
        -h, --help                Show basic help message
        -v, --version             Show program's version number
        -u, --update              Update program from repository
        
    Output: 
        -o, --output file         Print log on a file

    Examples:
        python sir.py -n name
        python sir.py -n name -o
        python sir.py -u
    """     

def resolve(name):
    ip = core.get_ip_by_name(name)
    msg = ip
    if msg:
        logger.info('[+] Resolved!  IP: ' + msg)
    else:
        logger.error('[-] Error: Impossible to resolve name')
