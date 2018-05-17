"""sources:
html parsing: http://www.boddie.org.uk/python/HTML.html
"""
import urllib.request
import util as util
import socket_util

RETRIEVE_DATA = 0
SOCKET_CONNECTION = 1
if(RETRIEVE_DATA):
    """
    Ebay webpage. pgn indicates the page number. We need to iterate through all its pages
    https://www.ebay.com/sch/i.html?_from=R40&_nkw=razer+core&_sacat=0&_pgn=1
    """
    # myParser = util.MyHTMLParser() # not going to use html parser
    f = open("log.txt", "w", encoding="utf-8")

    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=razer+core&_sacat=0&_pgn=1"#'http://www.infolanka.com/miyuru_gee/art/art.html'
    page = urllib.request.urlopen(url).read().decode("utf-8")
    f.write(page) # loging the page
    # title_price_list = myParser.feed(page)
    title_price_list, num_page = util.extract_rc_info_with_page(page)

    i = 2
    while i <= num_page:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=razer+core&_sacat=0&_pgn={}".format(i)
        page = urllib.request.urlopen(url).read().decode("utf-8")
        title_price_list.append(util.extract_rc_info(page))
        i += 1
    # print(title_price_list)
    # print(len(title_price_list))
    # print(num_page)

    """ TODO: serialize the title_price_list and send to mobile device."""
if (SOCKET_CONNECTION):
    socket_util.server_run();



