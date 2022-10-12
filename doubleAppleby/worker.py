import datetime

import pause
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def book(player2, player3, player4, play_time, play_date, court_number, open_book_page, hit_it):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.google.com")
    login_url = 'https://www.tennisclubsoft.com/appleby/home/login.do'
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
    uri = "https://www.tennisclubsoft.com/appleby/home/newView.do?id=304&calendar=7&"
    court_item = {1: "1", 2: "2", 3: "3", 4: "4", 5: "19", 6: "20"}
    param = "item=" + court_item[court_number] + "&date=" + play_date + "&time=" + play_time + "%20PM"
    browser.get(uri + param)
    browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
    browser.find_element(By.ID, 'Player_three_Auto').send_keys(player3)
    browser.find_element(By.ID, 'Player_Four_Auto').send_keys(player4)
    browser.find_element(By.ID, 'Booking Duration').send_keys('120')
    final_btn = "//*[contains(@onclick, 'final')]"
    pause.until(hit_it)
    browser.find_element(By.XPATH, final_btn).click()
    print(datetime.datetime.now().strftime("%H:%M:%S.%f") + " - clicked BOOK button by " + ts)
    try:
        print(browser.find_element(By.CSS_SELECTOR, "body > h1").text + " by " + ts)
    except NoSuchElementException:
        print(datetime.datetime.now().strftime("%H:%M:%S.%f") + " *** Booked successfully by " + ts)
