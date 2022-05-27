import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

options = Options()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

with webdriver.Chrome(options=options) as driver:
    driver.get("https://twitter.com/")
    signUp_btn = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/a/div/span/span")
    signUp_btn.click()

    username = driver.find_element(By.CLASS_NAME, 'css-1dbjc4n r-16y2uox r-1wbh5a2')
    tel = driver.find_element(locate_with(By.TAG_NAME, "input").below(username))
    time.sleep(3)
    username.send_keys("deneme")
    tel.send_keys("055545")

    time.sleep(10)
    driver.quit()