#!/usr/bin/python3
"""
This module contain a script that takes your 
"""
import sys
import requests

url = 'https://api.github.com/user'

username = sys.argv[1]
password = sys.argv[2]

response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    print(response.json().get('id'))
else:
    print("None")
