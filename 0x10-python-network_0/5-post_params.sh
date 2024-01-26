#!/bin/bash
# Sends a POST request with specific form data to a URL and displays the response body
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
