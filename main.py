#!/usr/bin/env python3
from sys import argv, exit
from duckduckgo.search import go_duck
from google.search import go_gle

# vars
use = 'Use: main.py "<seach expression>"'
banner = f'''
GeTrails are projet for OSINT
{use}
Issue: github.com/Vault-Cyber-Security/getrails/issues
'''

if len(argv) < 2:
    print('Use: main.py "<seach expression>"')
    exit(1)
elif argv[1] == '--help' or argv[1] == '-h':
    print(banner)
    exit(1)

def search_now (query):
    try:
        result = go_gle(query)
        result = go_duck(query)
    except:
        result = go_duck(query)
    return result

print(search_now(argv[1]))

