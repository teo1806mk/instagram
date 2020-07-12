import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Firefox()
url = (f"https://www.instagram.com/p/CCGUOA_HFe_/?utm_source=ig_web_copy_link")
driver.get(url)
time.sleep(2)
singin = driver.find_element_by_css_selector("button.L3NKy").click()
time.sleep(2)
usename = driver.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
usepass= driver.find_element_by_css_selector('div.-MzZI:nth-child(3) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
usename.send_keys('6983811496')
usepass.send_keys('18062001.karip')
singin = driver.find_element_by_css_selector("div.Igw0E:nth-child(4)").click()
time.sleep(3)
notbutton = driver.find_element_by_css_selector("button.sqdOP:nth-child(1)").click()
time.sleep(2)
comment = lambda: driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
time.sleep(1)
comment().click()
time.sleep(4)
#messages = ['good luck', 'kalh thxh', 'makari kerdiso', 'hi', 'hello', 'its me mario']
mes ="good luck"
comment().send_keys(mes)
comment().send_keys(Keys.ENTER)
