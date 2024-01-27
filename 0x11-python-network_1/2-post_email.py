#!/usr/bin/python3
"""
This module contain a  script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse
url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
data = urllib.parse.urlencode(data)
data = data.encode('ascii')

request = urllib.request.Request(url, data)

with urllib.request.urlopen(request) as response:
    content = response.read().decode('utf-8')
    print(content)
