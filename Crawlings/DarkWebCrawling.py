import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

depth = 3

proxies = {
    "http": "socks5h://127.0.0.1:9150",
    "https": "socks5h://127.0.0.1:9150"
}

def get_page_content(url):
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        return response.content
    except RequestException as e:
        print(f"Failed to fetch content for {url}: {e}")
        return None

def extract_text(soup):
    # <body> 태그 내부의 텍스트를 추출
    body = soup.find("body")
    if body:
        text = body.get_text()
        return text.strip()
    else:
        return ""

def explore_links_recursive(url, current_depth):
    if current_depth > depth:
        return

    content = get_page_content(url)
    if content is None:
        return

    soup = BeautifulSoup(content, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and (href.startswith("http://") or href.startswith("https://")) and href.endswith(".onion"):
            print(f"Depth: {current_depth} Link: {href}")
            sub_content = get_page_content(href)
            if sub_content is not None:
                sub_soup = BeautifulSoup(sub_content, "html.parser")
                title = sub_soup.title.string if sub_soup.title else "No Title"
                content_text = extract_text(sub_soup)  # <body> 태그 내부의 텍스트 추출
                data = {
                    "Depth": current_depth,
                    "url": href,
                    "title": title,
                    "content": content_text
                }
                try:
                    response = requests.post("http://172.30.1.80:8000/kisia", json=data)
                    response.raise_for_status()
                except RequestException as e:
                    print(f"Failed to post data for {href}: {e}")
                explore_links_recursive(href, current_depth + 1)

for index in range(0, 19):
    url = f"http://donionsixbjtiohce24abfgsffo2l4tk26qx464zylumgejukfq2vead.onion/?cat={index}&pg=0"
    data = {"Depth": 0, "url": url}
    explore_links_recursive(url, 1)
