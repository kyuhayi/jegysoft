import datetime

import pause
import selenium.webdriver.support
from pygame import mixer
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

login_id = "Ky.oakville@gmail.com"
login_pw = "planet00"
timeout = 10  # seconds

browser = webdriver.Chrome("/home/kyuu/opt/chromedriver99")
actions = ActionChains(browser)


browser.get('https://www2.tennisclubsoft.com/bubbletennis/home/login.do')
browser.get('https://www2.tennisclubsoft.com/bubbletennis/home/login.do')

WebDriverWait(browser, timeout).until(expected_conditions.element_to_be_clickable((By.ID, 'submit')))

username = browser.find_element_by_id('userid')
username.send_keys(login_id)
pw = browser.find_element_by_id('password')
pw.send_keys(login_pw)

browser.find_element_by_id('submit').click()

browser.find_element_by_link_text('Book a Court').click()

while True:
    book_link = browser.find_elements_by_xpath("//*[contains(text(), 'Bonus')]")
    print("Current Time =", datetime.datetime.now().strftime("%H:%M:%S"))
    if len(book_link) > 1:
        print('Found Bonus')
        while True:
            mixer.init()  # you must initialize the mixer
            alert = mixer.Sound('/home/kyuu/opt/file_example.wav')
            alert.play()
            pause.seconds(10)
        # break
    pause.seconds(10)
    browser.refresh()
