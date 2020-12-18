#!/usr/bin/env python3

#A simple python program to bruteforce api keys made for tryhackme's aoc2020 day 16

# https://pypi.org/project/requests/
# https://github.com/psf/requests
import requests

for api_key in range(1,100,2):
    print(f"api_key {api_key}")
    html = requests.get(f'http://ip/api/{api_key}')
    print(html.text)
