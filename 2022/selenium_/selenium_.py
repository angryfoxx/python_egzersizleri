from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
browser = webdriver.Chrome(options=option)

browser.get(url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712")

time.sleep(5)

elements = browser.find_elements_by_css_selector(".content")
for element in elements:
    print("*********************************************")
    print(element.text)

browser.close()
