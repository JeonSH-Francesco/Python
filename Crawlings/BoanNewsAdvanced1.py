from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import schedule
import sys

def scrape_and_save_news():
    browser = webdriver.Chrome()
    browser.get("https://m.boannews.com/html/index.html")
    browser.implicitly_wait(3)

    base_url = "https://m.boannews.com"
    # Wait for the element with class "headline4_title" to be present
    wait = WebDriverWait(browser, 20)  # Increased the timeout to 20 seconds
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "headline4_title")))

    # Pause for a few seconds to allow more content to load (you can adjust the duration as needed)
    time.sleep(5)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    ref_list = []
    title_list = []
    for headline4_title in soup.find_all(class_="headline4_title"):
        title = headline4_title.text.strip()  # Remove leading and trailing spaces
        title_list.append(title)
        href = headline4_title.a.get('href')
        if href:
            ref_list.append(base_url + href)

    # Get today's date in the format YYYYMMDD
    today_date = datetime.now().strftime("%Y%m%d")

    # Specify the full path for the text file including today's date
    txt_filename = f"C:/boanNews/{today_date}_boanNews.txt"

    with open(txt_filename, 'w', encoding='utf-8') as txt_file:
        for title, ref in zip(title_list, ref_list):
            # Write title
            txt_file.write("제목: " + title + '\n\n')

            # Open the link in a new tab
            browser.execute_script("window.open('{}', '_blank');".format(ref))
            time.sleep(random.randint(3, 5))  # You can adjust the wait time as needed

            # Switch to the new tab
            browser.switch_to.window(browser.window_handles[-1])

            # Find the content
            article_body = browser.find_element(By.CSS_SELECTOR, "div[itemprop='articleBody']")
            content = article_body.text

            # Write content to the text file
            txt_file.write("내용: " + content + '\n\n')  # Add some space between contents

            # Close the new tab
            browser.close()

            # Switch back to the original tab
            browser.switch_to.window(browser.window_handles[0])

    browser.quit()
    print(f"Text file generated successfully at {txt_filename}")
    sys.exit()  # 스크립트 종료

# Schedule the scraping and saving job to run every day at 10:00 AM
schedule.every().day.at("19:00").do(scrape_and_save_news)

while True:
    schedule.run_pending()
    time.sleep(1)
