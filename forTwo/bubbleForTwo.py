import datetime

import pause
from selenium import webdriver
from selenium.webdriver.common.by import By


def book(player2, play_time, play_date, court_number, booking_start):
    # browser = webdriver.Chrome("/home/kyuu/opt/chromedriver99")
    browser = webdriver.Chrome("C:/Users/YiKyuha/scratch/jegysoft/chromedriver99.exe")
    login_url = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
    login_id = "Ky.oakville@gmail.com"
    login_pw = "planet00"
    pause.until(booking_start - datetime.timedelta(minutes=2))

    browser.get(login_url)  # retry this
    username = browser.find_element(By.ID, 'userid')
    username.send_keys(login_id)
    pw = browser.find_element(By.ID, 'password')
    pw.send_keys(login_pw)
    browser.find_element(By.ID, 'submit').click()
    ts = booking_start.strftime("%S.%f")
    pause.until(booking_start)
    uri = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"
    param = "item=" + str(court_number) + "&date=" + play_date + "&time=" + play_time + "%20PM"
    browser.get(uri + param)
    browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
    browser.find_element(By.ID, 'Booking Duration').send_keys('60')
    final_btn = "//*[contains(@onclick, 'final')]"
    browser.find_element(By.XPATH, final_btn).click()
    print(ts + " started " + datetime.datetime.now().strftime("%S.%f"))
    result = browser.find_element(By.CSS_SELECTOR, "body > h1")
    if not bool(result.text.strip()):
        print(ts + " Booked successfully")
    print(ts + " " + result.text)
