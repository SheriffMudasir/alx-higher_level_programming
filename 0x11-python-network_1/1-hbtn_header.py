#!/usr/bin/python3
"""
This module contain a script that send
"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    value = response.getheader('X-Request-Id')
    if value:
        print(value)
