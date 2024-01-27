#!/usr/bin/python3
"""
This module contain a script takes in a URL and an email a
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

response = requests.post(url, data=data)
print(response.text)
