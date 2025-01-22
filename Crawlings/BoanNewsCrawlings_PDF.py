from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
import pdfkit
import os
import time

# HTML을 PDF로 변환하기 위한 pdfkit 설정
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='C:/Program Files (x86)/wkhtmltopdf/bin/wkhtmltopdf.exe')

def scrape_and_save_news_as_pdf():
    browser = webdriver.Chrome()
    browser.get("https://m.boannews.com/html/index.html")
    browser.implicitly_wait(3)

    base_url = "https://m.boannews.com"
    wait = WebDriverWait(browser, 20)
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "headline4_title")))

    time.sleep(5)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    ref_list = []
    title_list = []
    for headline4_title in soup.find_all(class_="headline4_title"):
        title = headline4_title.text.strip()
        title_list.append(title)
        href = headline4_title.a.get('href')
        if href:
            ref_list.append(base_url + href)

    today_date = datetime.now().strftime("%Y%m%d")
    output_dir = "C:/boanNews/"
    os.makedirs(output_dir, exist_ok=True)

    pdf_filename = os.path.join(output_dir, f"{today_date}_boanNews.pdf")
    combined_html = "<html><head><meta charset='utf-8'><style>body { font-family: Arial, sans-serif; } table { width: 100%; border-collapse: collapse; margin-bottom: 20px; } table, th, td { border: 1px solid black; padding: 8px; text-align: center; } img { margin: 10px 0; }</style></head><body>"

    for title, ref in zip(title_list, ref_list):
        try:
            browser.execute_script("window.open('{}', '_blank');".format(ref))
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[-1])

            combined_html += f"<div style='page-break-after: always;'>"
            combined_html += f"<h1>{title}</h1>"

            # 이미지 먼저 출력
            try:
                article_body = browser.find_element(By.CSS_SELECTOR, "div[itemprop='articleBody']")
                article_html = article_body.get_attribute("innerHTML")
                soup_content = BeautifulSoup(article_html, 'html.parser')

                for img_element in soup_content.find_all('img'):
                    img_url = img_element['src']
                    combined_html += f"<img src='{img_url}' width='600'><br>"

                # 텍스트 추가
                article_text = soup_content.get_text(separator="\n").strip()
                combined_html += f"<p>{article_text}</p>"

            except Exception as e:
                print(f"본문 로드 실패: {e}")

            combined_html += "</div>"

            browser.close()
            browser.switch_to.window(browser.window_handles[0])

        except Exception as e:
            print(f"기사 로드 실패: {e}")

    combined_html += "</body></html>"

    # HTML을 PDF로 변환
    try:
        pdfkit.from_string(combined_html, pdf_filename, configuration=PDFKIT_CONFIG)
        print(f"PDF 파일이 성공적으로 생성되었습니다: {pdf_filename}")
    except Exception as e:
        print(f"PDF 생성 실패: {e}")

    browser.quit()

# 실행
scrape_and_save_news_as_pdf()
