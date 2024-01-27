#!/usr/bin/python3
"""
This module contain a that takes in a U
"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)

value = response.headers.get('X-Request-Id')
if value:
    print(value)
