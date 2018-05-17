from html.parser import HTMLParser
import re
from bs4 import BeautifulSoup
"""TODO: fix rmb??? why rmb??? or just convert to usd"""
"""TODO: run the same thing on all pages"""

class MyHTMLParser(HTMLParser):
    title_flag = 0
    price_flag = 0
    print_flag = 0 # print_flag is changed only when "razer core" keyword is found in the title
    return_list = []
    title_price_tuple = [None, None]
    def handle_starttag(self, tag, attrs):
        if (attrs!=[]):
            # class attribute in the tag
            cls = attrs[0][1]
            if cls == "s-item__title" or cls == "vip":# encountered a title of item
                self.title_flag = 1
                print("title")
            elif (cls == "s-item__price") or cls == "lvprice":# encounter a price
                self.price_flag = 1

# s-item__detail--primary
    def handle_data(self, data):
        if self.title_flag and self.is_core(data):# when we found keyword "razer core" in the title
            print(data)
            self.title_price_tuple = self.title_price_tuple.copy()
            self.title_price_tuple[0] = data # set the title_price tuple
            self.print_flag = 1
        elif self.price_flag and self.print_flag == 1:# we found the price of the found keyword
            # print(data)
            self.title_price_tuple[1] = data # set the price in title_price_tuple
            # store the title price tuple in the return list
            self.return_list.append(self.title_price_tuple)
            self.print_flag = 0 # resets the print flag
        # elif data == "New Listing":
        #     return
        self.price_flag = 0
        self.title_flag = 0

    def is_core(self, string):
        pat = re.compile('[Rr]azer [Cc]ore')
        li = pat.findall(string)
        return len(li) != 0

    def feed(self, data):
        HTMLParser.feed(self, data)
        return self.return_list

    def initialize(self):
        self.title_price_tuple = [None, None]
        self.return_list = []

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        pass

"""
Returns a list of title-price pair of razer core from the given html page
"""
def extract_rc_info_with_page(page):
    return_list = []
    soup = BeautifulSoup(page, "html.parser")
    # number of pages
    result_txt = soup.find(string=re.compile("results")).string
    print(result_txt[:-8])
    num_page = (int(result_txt[:-8]) // 50 ) + 1
    # first we need to know which version of the html did we get.
    # is it using class "vip" or "s-items" for the items on sale
    for info in soup.findAll("a", string=re.compile('[Rr]azer [Cc]ore')):
        link = info.get("href")
        title = info.string
        item = info.parent.parent
        price = item.find(class_="s-item__price").string
        return_list.append((title, price))

    return return_list, num_page

def extract_rc_info(page):
    return_list = []
    soup = BeautifulSoup(page, "html.parser")
    # first we need to know which version of the html did we get.
    # is it using class "vip" or "s-items" for the items on sale
    for info in soup.findAll("a", string=re.compile('[Rr]azer [Cc]ore')):
        link = info.get("href")
        title = info.string
        item = info.parent.parent
        price = item.find(class_="s-item__price").string
        return_list.append((title, price))

    return return_list