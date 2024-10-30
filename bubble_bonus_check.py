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

# browser = webdriver.Chrome("/home/kyuu/opt/chromedriver99")
# browser = webdriver.Chrome("C:/Users/YiKyuha/scratch/jegysoft/chromedriver99.exe")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.google.com")

actions = ActionChains(browser)

browser.get('https://www2.tennisclubsoft.com/bubbletennis/home/login.do')
WebDriverWait(browser, timeout).until(expected_conditions.element_to_be_clickable((By.ID, 'submit')))

username = browser.find_element(By.ID, 'userid')
username.send_keys(login_id)
pw = browser.find_element(By.ID, 'password')
pw.send_keys(login_pw)

browser.find_element(By.ID, 'submit').click()

browser.find_element(By.LINK_TEXT, 'Book a Court').click()

while True:
    book_link = browser.find_elements(By.XPATH, ("//*[contains(text(), 'Bonus')]"))
    print("Current Time =", datetime.datetime.now().strftime("%H:%M:%S"))
    print(len(book_link))
    if len(book_link) > 1:
        print('Found Bonus')
        while True:
            mixer.init()  # you must initialize the mixer
            alert = mixer.Sound('sampling.wav')
            alert.play()
            pause.seconds(10)
        # break
    pause.seconds(10)
    browser.refresh()
