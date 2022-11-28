"""
CP1404 Practical - Wikipedia API
"""

import wikipedia

page_search = input("Enter your search: ")
while page_search != "":
    try:
        page = wikipedia.page(page_search, auto_suggest=False)
        print(page.title)
        print()
        print("Summary:")
        print(page.summary)
        print()
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("This could refer to multiple pages, please try something more specific")
        print(e.options)
    page_search = input("Enter your search: ")
