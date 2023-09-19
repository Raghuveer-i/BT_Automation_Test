import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
chrome_driver_path = "C:\\Users\\Raghuveer\\Downloads\\ChromeDriver\\chromedriver-win32\\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.bt.com/")

driver.implicitly_wait(5)
Cookie_Accept = driver.find_element(By.XPATH, "//a[text()='Accept all cookies']")
Cookie_Accept.click()

action = ActionChains(driver)
mobile_tab = driver.find_element(By.XPATH, "(//span[text()='Mobile'])[1]")

action.move_to_element(mobile_tab).perform()

mobile_phones = driver.find_element(By.LINK_TEXT, "Mobile phones")
action.move_to_element(mobile_phones).perform()

# Click on Mobile Phones
click_mobileElement = driver.find_element(By.LINK_TEXT, "Mobile phones")
click_mobileElement.click()

time.sleep(5)

# Page title
title = driver.title
print(title)

#Current URL Assertion
expected_url = "https://www.bt.com/products/mobile/phones/"
actual_url = driver.current_url
assert expected_url == actual_url

# Print number of banners
banners = driver.find_elements(By.XPATH,"//div[@class='flexpay-card_card_wrapper__Antym']")
print(len(banners))

#Scrolling using JavaScript Executer and click on View SIM only deals
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
sim_deals = driver.find_element(By.LINK_TEXT,"View SIM only deals")
sim_deals.click()

#Title Validaton
actual_title = "Mobile phone deals | New mobiles and Pay Monthly | BT Mobile"
expected_title = driver.title
assert actual_title == expected_title
print("Title Validated Successfully")

#Close and quit driver
driver.close()
driver.quit()