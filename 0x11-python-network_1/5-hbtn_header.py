#!/usr/bin/python3
"""
This module contain a that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)

value = response.header.get('X-Request-Id')
if value:
    print(value)
