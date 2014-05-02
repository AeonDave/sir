#!/usr/bin/python

"""
Copyright (c) 2014 tilt (https://github.com/AeonDave/sir)
See the file 'LICENSE' for copying permission
"""

import socket, sys, urllib2, urllib, source
from lib.logger import logger


    
def get_ip_by_name(name):
    
    ip = source.get_reverse_from_resolvethem(name)
    return ip

def get_html_from_url(url, name):
    
    values = {'username' : name, 'submit' : ''}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Connection', 'keep-alive')
    
    try:
        response = urllib2.urlopen(req)
        return response.read()
    except:
        logger.error('[-] Error')

