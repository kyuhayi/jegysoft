import datetime

import pause
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium


def book(book_page_url, time_open_book_page, time_hit_it, login_url, login_id, login_pw, player2):
    browser = get_chrome_headless()
    pause.until(time_open_book_page - datetime.timedelta(seconds=30))
    browser.get(login_url)  # retry this
    browser.find_element(By.ID, 'userid').send_keys(login_id)
    browser.find_element(By.ID, 'password').send_keys(login_pw)
    browser.find_element(By.ID, 'submit').click()
    ts = time_open_book_page.strftime("%H:%M:%S")
    pause.until(time_open_book_page)
    browser.get(book_page_url)
    browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
    browser.find_element(By.ID, 'Booking Duration').send_keys('60')
    print("It will run at " + time_hit_it.strftime("%H:%M:%S"))
    pause.until(time_hit_it)
    browser.find_element(By.ID, 'final').click()
    print(datetime.datetime.now().strftime("%H:%M:%S.%f") + " - clicked BOOK button by " + ts)
    try:
        print(browser.find_element(By.CSS_SELECTOR, "h1.error").text
              + " by " + ts
              + " at " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
    except NoSuchElementException:
        try:
            print(browser.find_element(By.CSS_SELECTOR, "div.caltablesec strong").text
                  + " by " + ts
                  + " at " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        except NoSuchElementException:
            pass


def get_chrome_headless():
    options = selenium.webdriver.chrome.options.Options()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    chrome = selenium.webdriver.Chrome(options=options)
    chrome.implicitly_wait(5)  # seconds
    return chrome
