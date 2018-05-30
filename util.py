from html.parser import HTMLParser
import re
from bs4 import BeautifulSoup
import urllib.request

def extract_info(keyword="razer core", site="ebay"):
    if site == "ebay":
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=razer+core&_sacat=0&_pgn=1"
    else:
        print("No valid url");
        exit(-1)
    page = get_html_from_url(url);
    # initialize beautiful soup
    return_list = []
    soup = BeautifulSoup(page, "html.parser")
    # number of pages
    result_txt = soup.find(string=re.compile("results")).string
    num_page = (int(result_txt[:-8]) // 50 ) + 1
    # extract core information
    l = soup.findAll(string=re.compile('[Rr]azer [Cc]ore'));
    print(l)
    # for info in soup.findAll("a", string=re.compile('[Rr]azer [Cc]ore')):
    #     link = info.get("href")
    #     title = info.string
    #     item = info.parent.parent
    #     price = item.find(class_="s-item__price").string
    #     return_list.append((title, price))

    return return_list, num_page

def get_html_from_url(url):
#    try:
    page = urllib.request.urlopen(url).read().decode("utf-8");
    # except Exception:
    #     print("Unable to read the page");
    #     exit(-1)
 #   return page

extract_info("razer core", "ebay");
