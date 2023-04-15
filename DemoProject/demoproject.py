from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

#initialize chrome
driver=webdriver.Chrome("C:\Drivers\chromedriver.exe",options=ops)



#open url
driver.get("https://www.saucedemo.com/")

#maximize the window
driver.maximize_window()

username=driver.find_element_by_id("user-name").send_keys("standard_user")
time.sleep(2)
password=driver.find_element_by_id("password").send_keys("secret_sauce")
time.sleep(2)
login=driver.find_element_by_id("login-button").click()
time.sleep(2)

backpack=driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
time.sleep(2)

#scroll the page
driver.execute_script("window.scrollBy(0,500)"," ")
value=driver.execute_script("return window.pageYOffset;")
time.sleep(2)


tshirt=driver.find_element_by_id("add-to-cart-sauce-labs-onesie").click()
time.sleep(2)

#scroll to top of the page
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
time.sleep(2)

cart=driver.find_element(By.XPATH,'//a[@class="shopping_cart_link"]').click()

checkout=driver.find_element_by_id("checkout").click()
time.sleep(2)

name=driver.find_element_by_name("firstName").send_keys("test")
time.sleep(2)
lastname=driver.find_element_by_name("lastName").send_keys("user")
time.sleep(2)
postalcode=driver.find_element_by_id("postal-code").send_keys("090")
time.sleep(2)

driver.execute_script("window.scrollBy(0,500)"," ")
value=driver.execute_script("return window.pageYOffset;")
time.sleep(2)

continuebutton=driver.find_element_by_id("continue").click()
time.sleep(2)

finish=driver.find_element_by_id("finish").click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
time.sleep(2)

driver.find_element_by_id("back-to-products").click()
time.sleep(3)

#close the window
driver.close()