import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import random, time

options = uc.ChromeOptions()
options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 1  
})

driver_exec_path = ChromeDriverManager().install()
driver = uc.Chrome(driver_executable_path=driver_exec_path,options=options)

#lat= random.uniform(33.57443236768635, 37.557571487999648)
#long = random.uniform(126.95883972338915 , 127.01824406323593)
lat=37.490869
long=127.125467
lat_long  = {"latitude" : lat, "longitude" : long, "accuracy" : 100}
print(lat_long)

### navigator.getLocation
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", lat_long)
driver.get("https://www.gps-coordinates.net/")

driver.implicitly_wait(5)

time.sleep(5)

driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, 'map_canvas'))
driver.implicitly_wait(5)
time.sleep(5)
print(driver.find_element(By.ID, "iwtitle").text)
input()
