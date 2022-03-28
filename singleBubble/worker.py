import datetime

import pause
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def book(player2, play_time, play_date, court_number, open_book_page, hit_it):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.google.com")
    login_url = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
    login_id = "Ky.oakville@gmail.com"
    login_pw = "planet00"
    pause.until(open_book_page - datetime.timedelta(seconds=30))
    browser.get(login_url)  # retry this
    username = browser.find_element(By.ID, 'userid')
    username.send_keys(login_id)
    pw = browser.find_element(By.ID, 'password')
    pw.send_keys(login_pw)
    browser.find_element(By.ID, 'submit').click()
    ts = open_book_page.strftime("%H:%M:%S")
    pause.until(open_book_page)
    uri = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"
    param = "item=" + str(court_number) + "&date=" + play_date + "&time=" + play_time + "%20PM"
    browser.get(uri + param)
    browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
    browser.find_element(By.ID, 'Booking Duration').send_keys('60')
    final_btn = "//*[contains(@onclick, 'final')]"
    pause.until(hit_it)
    browser.find_element(By.XPATH, final_btn).click()
    print(ts + " clicked BOOK button at " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
    try:
        print(ts + " " + browser.find_element(By.CSS_SELECTOR, "body > h1").text)
    except NoSuchElementException:
        print(ts + " Booked successfully at " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
