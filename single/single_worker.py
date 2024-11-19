import datetime

import pause
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def book(book_page_url, time_open_book_page, time_hit_it, login_url, login_id, login_pw, player2):
    browser = get_browser()
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
    browser.find_element(By.ID, 'Booking Duration').send_keys('60')
    final_btn = "//*[contains(@onclick, 'final')]"
    pause.until(time_hit_it)
    browser.find_element(By.XPATH, final_btn).click()
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
    finally:
        browser.close()


def get_browser():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("headless")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(1)
    return browser