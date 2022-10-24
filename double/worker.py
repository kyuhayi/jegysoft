import datetime

import pause
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

google_url = "https://www.google.com"

def book(book_page_url, time_open_book_page, time_hit_it, login_url, login_id, login_pw, player2, player3, player4):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(google_url)
    pause.until(time_open_book_page - datetime.timedelta(seconds=30))
    browser.get(login_url)  # retry this
    username = browser.find_element(By.ID, 'userid')
    username.send_keys(login_id)
    pw = browser.find_element(By.ID, 'password')
    pw.send_keys(login_pw)
    browser.find_element(By.ID, 'submit').click()
    ts = time_open_book_page.strftime("%H:%M:%S")
    pause.until(time_open_book_page)
    browser.get(book_page_url)
    browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
    browser.find_element(By.ID, 'Player_three_Auto').send_keys(player3)
    browser.find_element(By.ID, 'Player_Four_Auto').send_keys(player4)
    browser.find_element(By.ID, 'Booking Duration').send_keys('120')
    final_btn = "//*[contains(@onclick, 'final')]"
    pause.until(time_hit_it)
    browser.find_element(By.XPATH, final_btn).click()
    print(datetime.datetime.now().strftime("%H:%M:%S.%f") + " - clicked BOOK button by " + ts)
    try:
        print(browser.find_element(By.CSS_SELECTOR, "body > h1").text + " by " + ts)
    except NoSuchElementException:
        print(datetime.datetime.now().strftime("%H:%M:%S.%f") + " *** Booked successfully by " + ts)
