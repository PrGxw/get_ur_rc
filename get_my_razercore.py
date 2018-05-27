"""sources:
html parsing: http://www.boddie.org.uk/python/HTML.html
"""
import urllib.request
import util as util
import socket_util
import socket
import json


RETRIEVE_DATA = 0
SOCKET_CONNECTION = 1
def retrieve_data():
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
    return title_price_list

    """ TODO: serialize the title_price_list and send to mobile device."""

HOST = "149.28.44.30"  # '114.246.73.95'
PORT = 10101

if (SOCKET_CONNECTION):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # 定义socket类型，网络通信，TCP
        s.bind((HOST, PORT))  # 套接字绑定的IP与端口
        s.listen(1)  # 开始TCP监听,监听1个请求
        
        print("Server is running")
        while True:
            conn, addr = s.accept();
            print("connected by", addr);
            #print(repr(conn.recv(1024)));
            with conn:

                msg = conn.recv(1024);
                if msg.decode('utf-8') == "request":
                    list = retrieve_data();
                    json_str = json.dumps(list);
                    conn.sendall(json_str.encode());
                else:
                    conn.sendall(b"bye");
                





