from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver = webdriver.Chrome(options=options)

driver.quit()
