from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://vinothqaacademy.com/demo-site/")

wait=WebDriverWait(driver,10)

first_name=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//input[@id="vfb-5"]')
))
first_name.send_keys("Test User")

last_name=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-7"]')
))
last_name.send_keys("Example")

female=wait.until(EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="vfb-31-2"]')
))
female.click()

selenium_course=wait.until(EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="vfb-20-0"]')
))
selenium_course.click()

address=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-13-address"]')
))
address.send_keys("Example Engineering College")

street=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-13-address-2"]')
))
street.send_keys("Example Street")

city=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-13-city"]')
))
city.send_keys("Example City")

country=wait.until(EC.presence_of_element_located(
    (By.XPATH,'//*[@id="vfb-13-country"]')
))
select=Select(country)
select.select_by_visible_text("India")

email=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-14"]')
))
email.send_keys("test@example.com")

date=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-18"]')
))
date.send_keys("10/06/26")

time=wait.until(EC.presence_of_element_located(
    (By.XPATH,'//*[@id="vfb-16-hour"]')
))
select=Select(time)
select.select_by_visible_text("05")

time2=wait.until(EC.presence_of_element_located(
    (By.XPATH,'//*[@id="vfb-16-min"]')
))
select=Select(time2)
select.select_by_visible_text("25")

mobile=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-19"]')
))
mobile.send_keys("0000000000")

query=wait.until(EC.visibility_of_element_located(
    (By.XPATH,'//*[@id="vfb-23"]')
))
query.send_keys("This is an automation testing process")

input("press enter to close")
print("Test executed successfully...")
driver.quit()