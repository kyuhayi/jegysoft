import datetime

import pause
import selenium
import selenium.webdriver.chrome.options
import selenium.webdriver.chrome.service
import webdriver_manager.chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

LOGIN_PW = "rmawhdgh"
LOGIN_ID = "hydrokeum@gmail.com"
LOGIN_URL = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
BOOKING_URI = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"


def book(day, time, court, player2, player3, player4, delay_mill):
    browser = get_chrome_headless()
    pause.until(date_3min_before_7am())

    login(browser)
    book_start_time = date_delayed_7am(delay_mill)
    pause.until(book_start_time)

    try:
        browser.get(str_booking_page_url(day, time, court))
        browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
        browser.find_element(By.ID, 'Player_three_Auto').send_keys(player3)
        browser.find_element(By.ID, 'Player_Four_Auto').send_keys(player4)
        browser.find_element(By.ID, 'Booking Duration').send_keys('120')
        browser.find_element(By.ID, 'final').click()
    except NoSuchElementException:
        pass



    book_start_time_str = book_start_time.strftime("%H:%M:%S.%f")

    try:
        print(browser.find_element(By.CSS_SELECTOR, "h1.error").text
              + " by " + book_start_time_str
              + " at " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
    except NoSuchElementException:
        try:
            print(browser.find_element(By.CSS_SELECTOR, "div.caltablesec strong").text
                  + " by " + book_start_time_str
                  + " at " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
        except NoSuchElementException:
            pass
    finally:
        browser.close()


def date_delayed_7am(delay_mill):
    return date_7am_sunday() + datetime.timedelta(milliseconds=delay_mill)


def date_3min_before_7am():
    return date_7am_sunday() - datetime.timedelta(minutes=3)


def date_7am_sunday():
    return date_next_weekday_by("sun").replace(hour=7, minute=0, second=0, microsecond=0)


def str_date_next_weekday_by(day_abbr):
    return date_next_weekday_by(day_abbr).strftime("%Y-%m-%d")


def login(browser):
    browser.get(LOGIN_URL)  # retry this
    browser.find_element(By.ID, 'userid').send_keys(LOGIN_ID)
    browser.find_element(By.ID, 'password').send_keys(LOGIN_PW)
    browser.find_element(By.ID, 'submit').click()


def str_booking_page_url(day, time, court):
    booking_param = ("item={0}&date={1}&time={2}%20PM"
                     .format(str(court), str_date_next_weekday_by(day), str_formatted_hour(time)))
    return BOOKING_URI + booking_param


def get_chrome_headless():
    options = selenium.webdriver.chrome.options.Options()
    options.add_experimental_option("detach", True)
    options.add_argument("headless")
    chrome = selenium.webdriver.Chrome(options=options)
    chrome.implicitly_wait(5)  # seconds
    return chrome

def get_chrome_old():
    manager = webdriver_manager.chrome.ChromeDriverManager()
    return selenium.webdriver.Chrome(service=selenium.webdriver.chrome.service.Service(manager.install()))

def date_next_weekday_by(day_abbr):
    # Map abbreviations to day numbers (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    try:
        target_day = days.index(day_abbr.lower())
    except ValueError:
        return "Invalid day abbreviation. Use mon, tue, wed, thu, fri, sat, or sun."

    today = datetime.datetime.now()
    days_ahead = (target_day - today.weekday() + 7) % 7
    return today + datetime.timedelta(days=days_ahead)


def str_formatted_hour(hour):
    return f"{hour:02}:00"  # Convert hour to two-digit string and add ":00" for minutes
