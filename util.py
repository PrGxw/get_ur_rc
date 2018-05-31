from html.parser import HTMLParser
import re
from bs4 import BeautifulSoup
import urllib.request

SOUP_NAV_ITER = 5

def extract_info(keyword="razer core", site="ebay"):
    if site == "ebay":
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=razer+core&_sacat=0&_pgn=1"
    else:
        print("No valid url");
        exit(-1)
    page = get_html_from_url(url);
    # initialize beautiful soup
    title_price_list = []
    soup = BeautifulSoup(page, "html.parser")
    # number of pages
    result_txt = soup.find(string=re.compile("results")).string
    num_page = (int(result_txt[:-8]) // 50 ) + 1
    title_price_list = soup_find(soup, title_price_list)
    print(len(title_price_list))
    for i in range(2,num_page):
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=razer+core&_sacat=0&_pgn={}".format(i);
        page = get_html_from_url(url);
        soup = BeautifulSoup(page, "html.parser")
        title_price_list = soup_find(soup, title_price_list)
        print(len(title_price_list))
    return title_price_list

    # return return_list, num_page

def get_html_from_url(url):
    try:
        page = urllib.request.urlopen(url).read().decode("utf-8");
    except Exception:
        print("Unable to read the page");
        exit(-1)
    return page

def soup_find(soup, title_price_list):
    l = soup.findAll("li",class_="s-item"); # list of soup objects that contain keywords razer core
    is_bid = False;
    for item in l:
        # RETURN: title
        title = item.find(string=re.compile("[Rr]azer [Cc]ore"))
        if title == None:
            continue;
        # price = item.findAll(class_="s-item__price")[0].string;
        prices = item.findAll(class_="s-item__price");
        price = prices[0].string
        # RETURN: time-end
        time_end = item.find(class_="s-item__time-end").string;
        if time_end == None:
            is_bid = False;
        else:
            is_bid = True;
        if (is_bid):
            if len(prices) == 2:
                bid_price = prices[0].string
                buy_price = prices[1].string
            else:
                bid_price = prices[0].string
                buy_price = None
        else:
            bid_price = None
            buy_price = prices[0].string

        title_price_list.append((title, price, is_bid, bid_price, buy_price))
    return title_price_list