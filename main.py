#!/usr/bin/env python3
from sys import argv
# Search cons
query=f"site:{argv[1]}"

def get_duckduckgo (query):
    # Import main
    import mechanicalsoup

    # Connect to duckduckgo
    browser = mechanicalsoup.StatefulBrowser()
    browser.set_user_agent('Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')
    browser.open(f"https://duckduckgo.com/html/?q={query}")
    
    # List 
    list1 = []

    # Subfunction
    def change_page():
        browser.select_form(browser.get_current_page().select('form')[-1])
        browser.submit_selected()
        read_urls()


    def check():
        print(f"check: {browser.get_url()}")
        if browser.get_current_page().select('.btn--alt'):
            change_page()

    def read_urls():
        urls = []
        for link in browser.get_current_page().select('a.result__url'):
            list1.append(link.text)
            urls.append(link.text)

        check()
        return '\n'.join(list1)

    return read_urls()


def get_google (query):
    from googlesearch import search, get_random_user_agent
    my_results_list = []
    for i in search(query,        # Expression
                    tld = 'com',  # TL domain
                    lang = 'en',  # Set lang en
                    num = 10,     # Number of results / page
                    start = 0,    # First result to retrieve
                    stop = None,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                    user_agent = get_random_user_agent(),
                   ):
        my_results_list.append(i)

    return '\n'.join(my_results_list)

def search_now (query):
    try:
        result = get_google(query)
    except:
        result = get_duckduckgo(query)
    return result

print(search_now(query))

