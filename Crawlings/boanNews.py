from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    title_list.append(headline4_title.a.text)
    href = headline4_title.a.get('href')
    if href:
        ref_list.append(base_url + href)

print("Title List:")
for title in title_list:
    print(title)

print('\n')

print("Ref List:")
for ref in ref_list:
    print(ref)
    # Open the link in a new tab
    browser.execute_script("window.open('{}', '_blank');".format(ref))
    time.sleep(random.randint(3, 5))  # You can adjust the wait time as needed

    # Switch to the new tab
    browser.switch_to.window(browser.window_handles[-1])

    # Find the content
    article_body = browser.find_element(By.CSS_SELECTOR, "div[itemprop='articleBody']")
    content = article_body.text

    print(content)

    # Close the new tab
    browser.close()

    # Switch back to the original tab
    browser.switch_to.window(browser.window_handles[0])

browser.quit()

'''

pip install python-docx reportlab

'''
