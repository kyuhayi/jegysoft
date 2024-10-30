import datetime

import pause
from pygame import mixer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

login_id = "Ky.oakville@gmail.com"
login_pw = ""
timeout = 10  # seconds

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.google.com")
actions = ActionChains(browser)


browser.get('https://ts2.clubinterconnect.com/cvt/home/login.do')
browser.get('https://ts2.clubinterconnect.com/cvt/home/login.do')

WebDriverWait(browser, timeout).until(expected_conditions.element_to_be_clickable((By.ID, 'submit')))

username = browser.find_element(By.ID, 'userid')
username.send_keys(login_id)
pw = browser.find_element(By.ID, 'password')
pw.send_keys(login_pw)
browser.find_element(By.ID, 'submit').click()

courtString = '1 - 6'
browser.find_element(By.XPATH, "//a[contains(text(), '%s') and contains(text(), 'Book Court')]" % courtString).click()
date = 'Jun 8'
browser.find_element(By.XPATH, "//*[contains(text(), '%s')]" % date).click()

while True:
    book_link = browser.find_element(By.XPATH, ("//a[contains(@href, '8:30 PM')]"))
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
