import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

options = ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
#options.page_load_strategy = "normal"
driver = webdriver.Chrome(options=options)

"""
driver.implicitly_wait(1)
driver.get("http://www.google.com")

# print(driver.title) --> Google
# print(driver.current_url) --> http://www.google.com
# driver.back() ~~ geri tuşuna basar
# driver.forward() ~~ ileri tuşuna basar
# driver.refresh() ~~ yeniler

search_box = driver.find_element(By.NAME, "q")
search_btn = driver.find_element(By.NAME, "btnK")

search_box.send_keys("selenium")

if search_box.get_attribute("value") == "selenium":
    print("başarılı")
    search_btn.click()

driver.implicitly_wait(5)"""

#driver.get("https://www.selenium.dev/documentation/webdriver/browser/alerts/")
"""driver.find_element(By.LINK_TEXT, "See an example alert").click()
alert = WebDriverWait(driver, 3).until(expected_conditions.alert_is_present()) # uyarı oluşana kadar bekle ve bir değişkene ata

print(alert.text)

alert.accept()""" # alerts
"""driver.find_element(By.LINK_TEXT, "See a sample confirm").click()
WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())

alert = driver.switch_to.alert
print(alert.text)

alert.dismiss() # alert.accept() or dismiss()

""" # confirms
"""driver.find_element(By.LINK_TEXT, "See a sample prompt").click()
WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())

alert = Alert(driver)

alert.send_keys("Selenium")
alert.accept()
""" # prompts
driver.quit()