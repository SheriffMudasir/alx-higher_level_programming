#!/usr/bin/python3
"""
This module contain a script that fetches url using request package
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

print("Body response:")
print("\t - type:", type(response.text))
print("\t - content:", response.text)
