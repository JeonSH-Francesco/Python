from selenium import webdriver
from user_agents import parse
import random
def make_user_agent(ua, is_mobile):
    user_agent = parse(ua)
    model = user_agent.device.model    
    platform = user_agent.os.family
    platform_version = user_agent.os.version_string + ".0.0"
    version = user_agent.browser.version[0]
    ua_full_version = user_agent.browser.version_string    
    print(user_agent, model, platform, platform_version, version, ua_full_version)
    if is_mobile:
        ### Android
        platform_info = "Linux armv8l"
        architecture = ""        
    else:
        ### Windows
        platform_info = "Win32"
        architecture = "x86"
        mobile = ""
    return_user_agent = {
        "appVersion" : ua.replace("Mozilla/", ""),
        "userAgent" : ua,
        "platform" : f"{platform_info}",
        "acceptLanguage" : "ko-KR, kr, en-US, en",
        "userAgentMetadata" : {
            "brands" : [
                {"brand" : " Not A;Brand", "version" : "20099"},{"brand" : "Google Chrome", "version" : f"{version}"},{"brand" : "Chromium", "version" : f"{version}"},
            ],
            "fullVersion" : f"{ua_full_version}",
            "fullVersionList": [
                {"brand" : " Not A;Brand", "version" : "20099"},{"brand" : "Google Chrome", "version" : f"{version}"},{"brand" : "Chromium", "version" : f"{version}"},                
            ],          
            "platform" : platform,
            "platformVersion" : platform_version,
            "architecture" : architecture,
            "model" : model,
            "mobile" : False
        }        
    }       
    return return_user_agent
ua = "Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]"
ua_data = make_user_agent(ua, True)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
mobile_data = {"enabled" : True, "maxTouchPoints": random.choice([1,5])}
#driver.execute_cdp_cmd("Emulation.setTouchEmulationEnabled",mobile_data)
#driver.execute_cdp_cmd("Network.setUserAgentOverride", ua_data)
driver.get("http://m.naver.com")
input()








