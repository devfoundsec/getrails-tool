#!/usr/bin/env python3
from sys import argv
from getrails import go_duck
from getrails import go_gle
from getrails import go_onion
from urllib import error

# vars
use = 'Use: search.py "<seach expression>"'
art = '''
  ________        __                .__.__          
 /  _____/  _____/  |_____________  |__|  |   ______
/   \  ____/ __ \   __\_  __ \__  \ |  |  |  /  ___/
\    \_\  \  ___/|  |  |  | \// __ \|  |  |__\___ \ 
 \______  /\___  >__|  |__|  (____  /__|____/____  >
        \/     \/                 \/             \/'''
enable_dorks = '''\
Dorks Google and Duckduckgo search
----------------------------------
site\t\tFind all urls of domain
intitle\t\tFinds pages that include a specific keyword as part of the indexed title
inurl\t\tFind pages that include a specific keyword as a part
filetype\tSearch for specific file type
intext\t\tSearh for specific text
feed\t\tFind RSS related to search term\
'''
banner = f'''\
{art}
GeTrails are projet for OSINT and Dorks
{use}
\t-d, --dorks\t\tDorks enable in Google and Duckduckgo hacking
\t-t, --tor  <term>\tFor search in hidden services 
Issue: github.com/Vault-Cyber-Security/getrails-tools/issues\
'''

def search_now (query):
    try:
        result = go_gle(query)
        result.extend(go_duck(query))
    except error.HTTPError:
        result = go_duck(query)

    return '\n'.join(result)

def search_onion (query):
    return '\n'.join(go_onion(query))

# Use
try:
    if len(argv) > 2:
        if argv[1] == '-o' or argv[1] == '--onion':
            print(search_onion(argv[2]))
            exit(0)
        else:
            print(use)
            exit(1)
    elif argv[1] == '--help' or argv[1] == '-h':
        print(banner)
        exit(0)
    elif argv[1] == '--dorks' or argv[1] == '-d':
        print(enable_dorks)
        exit(0)
    else:
        print(search_now(argv[1]))
except IndexError:
    print(use)
