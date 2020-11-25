import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
ak=0
driver = webdriver.Chrome(executable_path=r"/home/theodork/Desktop/ka/instagram-master/instagram/chromedriver_linux64/chromedriver")
url = (f"https://www.instagram.com/p/CH-MgQOn-7E/?utm_source=ig_web_copy_link")
driver.get(url)
time.sleep(2)
coukis= driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.bIiDR').click()
singin = driver.find_element_by_css_selector("button.L3NKy").click()
time.sleep(2)
usename = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')
usepass= driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')
usename.send_keys('name')
usepass.send_keys('password')
singin = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div").click()
time.sleep(3)
notbutton = driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button").click()
time.sleep(2)
for x in range(1000):
    comment = lambda: driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
    time.sleep(1)
    comment().click()
    time.sleep(4)
    mes ="name for tags"
    comment().send_keys(mes)
    time.sleep(2)
    post= driver.find_element_by_css_selector("#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.sH9wk._JgwE > div.RxpZH > form > button").click()
    ak = ak+1
    print(ak)
    time.sleep(54)
   
    # element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((button, '<button class="sqdOP yWX7d    y3zKF     " type="submit">Post</button>'))
