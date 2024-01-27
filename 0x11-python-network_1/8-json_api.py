#!/usr/bin/python3
"""
This module contain script that takes in a letter a
"""
import requests
import sys

url = 'http://0.0.0.0:5000/search_user'
q = sys.argv[1] if len(sys.argv) > 1 else ""
data = {'q': q}
response = requests.post(url, data=data)
try:
    json_format = response.json()
    if json_format:
        print(f"[{json_format.get('id')}] {json_format.get('name')}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
