import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.print_page_options import PrintOptions

options = ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
#options.page_load_strategy = "normal"
with webdriver.Chrome(options=options) as driver:

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
    """driver.get("https://www.example.com")
    
    driver.add_cookie({"name":"name_key","value":"value_key"})
    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})
    
    print(driver.get_cookie("name_key")) # {'domain': 'www.example.com', 'httpOnly': False, 'name': 'name_key', 'path': '/', 'secure': True, 'value': 'value_key'}
    print(driver.get_cookie("test1")) # {'domain': 'www.example.com', 'httpOnly': False, 'name': 'test1', 'path': '/', 'secure': True, 'value': 'cookie1'}
    print(driver.get_cookies()) # [{'domain': 'www.example.com', 'httpOnly': False, 'name': 'test2', 'path': '/', 'secure': True, 'value': 'cookie2'}, {'domain': 'www.example.com', 'httpOnly': False, 'name': 'test1', 'path': '/', 'secure': True, 'value': 'cookie1'}, {'domain': 'www.example.com', 'httpOnly': False, 'name': 'name_key', 'path': '/', 'secure': True, 'value': 'value_key'}]
    
    driver.delete_all_cookies()
    print(driver.get_cookies()) # []""" # cookies
    """driver.get("https://www.selenium.dev/documentation/webdriver/browser/windows/")
    wait = WebDriverWait(driver, 10)

    original_window = driver.current_window_handle

    assert len(driver.window_handles) == 1

    #print(driver.title) # Working with windows and tabs | Selenium
    #driver.switch_to.new_window("tab")
    #driver.get("https://www.google.com")
    #print(driver.title) # Google

    driver.find_element(By.LINK_TEXT, "new window").click()
    time.sleep(3)
    wait.until(EC.number_of_windows_to_be(2))

    print(driver.title) # Working with windows and tabs | Selenium

    for w_handle in driver.window_handles:
        if w_handle != original_window:
            driver.switch_to.window(w_handle)
            break

    print(driver.title) # Selenium

    driver.close()
    driver.switch_to.window(original_window)

    width = driver.get_window_size().get("width") # 1050
    height = driver.get_window_size().get("height") # 718

    driver.set_window_size(1024, 768)

    # top left coordinate
    x = driver.get_window_position().get("x") # 10
    y = driver.get_window_position().get("y") # 10

    driver.set_window_position(0, 0)

    # driver.minimize_window(), driver.maximize_window(), driver.fullscreen_window()

    driver.save_screenshot("./deneme.png")

    # driver.find_element(By.LINK_TEXT, "new window").screenshot("C:\\Users\\Fox\\Desktop\\deneme.png")

""" # windows

