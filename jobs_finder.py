from usp.tree import sitemap_tree_for_homepage
from urllib.request import urlopen
import re
import sys

def get_urls(url):
    tree = sitemap_tree_for_homepage(url)

    urls = []
    for page in tree.all_pages():
        urls.append(page.url)

    return urls

def look_for_jobs(urls):
    # Initially just try to find job related words in the url
    # Try to visit each page and find out containing job related words.

    for url in urls:
        if re.search(r"jobs.*|careers.*|apply.*|opportunities.*", url):
            return url

    for url in urls:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        if re.search(r"\s|jobs.*careers.*internship.*hiring.*apply", html):
            return url

def main():
    try:
        url = sys.argv[1]
    except IndexError:
        print("Please enter a url")
        exit(1)
    urls = get_urls(url)
    
    print(look_for_jobs(urls))


if __name__ == "__main__":
    main()
