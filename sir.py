#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/sir)
See the file 'LICENSE' for copying permission
"""

import sys, getopt, logging

from lib import update
from lib import actions
from lib.logger import logger
     
# Tilt Setup

try:
    options, args = getopt.getopt(sys.argv[1:], 'n:vhu', ['name=', 'version', 'help', 'update', 'output'])
except getopt.GetoptError:
    actions.showhelp()
    sys.exit(1)

name=None
output=None

for opt, arg in options:
    if opt in ('-h', '--help'):
        actions.showhelp()
        sys.exit(0)
    elif opt in ('-v', '--version'):
        actions.header()
        sys.exit(0)
    elif opt in ('-u', '--update'):
        actions.header()
        update.update()
        sys.exit(0)
    elif opt in ('-n', '--name'):
        name = arg
    elif opt in ('-o', '--output'):
        output = arg
    else:
        actions.header()
        actions.showhelp()
        sys.exit(1)

if not name:
    actions.header()
    actions.showhelp()
    msg = "[-] ERROR: You must provide a Skype Name."
    logger.error(msg)
    sys.exit(1) 

def main():
    if output:     
        handler = logging.FileHandler(output)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
    
    if name:
        logger.info('[*] Trying to resolve name: '+ name)
        actions.resolve(name)
        
    if output: 
        logger.info('[+] File log written: ' + output)
# Program

if __name__ == '__main__':
    actions.header()
    main()
    sys.exit(0)
