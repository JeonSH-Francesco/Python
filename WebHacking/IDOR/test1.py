import requests
from bs4 import BeautifulSoup

def test():
    for i in range(0,30):
        url = "http://192.168.0.19:22223/practice.php?userid={}".format(i)
        headers = {
            "Host":"192.168.0.19:22223",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        }
        data=""
        res = requests.get(url=url, data=data, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        res1 = soup.find_all('h3')
        print(res1)
if __name__=="__main__":
    test()
