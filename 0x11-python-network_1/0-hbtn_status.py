#!/usr/bin/python3
"""
This module contain a python script that fetches a URL
"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
print("Body response:")
print("\t - type:", type(content))
print("\t - content", content)
print("\t - utf8 content:", content.decode('utf-8'))
