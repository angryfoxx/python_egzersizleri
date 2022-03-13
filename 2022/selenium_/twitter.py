from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

op = Options()
op.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
browser = webdriver.Chrome(options=op)

browser.get(url="https://twitter.com/i/flow/login")

usern = "the_foxing"
passw = "12491811asd"
tel = "5464149975"

time.sleep(2)
username = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
first_login = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]")

username.send_keys(usern)
time.sleep(2)
first_login.click()
time.sleep(2)

"""telephone = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
next_btn = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div")
telephone.send_keys(tel)
time.sleep(2)
next_btn.click()
time.sleep(2)
"""

password = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")
second_login = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div")

password.send_keys(passw)
time.sleep(2)
second_login.click()
time.sleep(2)
browser.close()