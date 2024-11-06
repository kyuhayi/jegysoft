import datetime

import pause
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

LOGIN_PW = "planet00"
LOGIN_ID = "ky.oakville@gmail.com"
LOGIN_URL = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
BOOKING_URI = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"


def book(day, time, court, player2, player3, player4, delay_mill):
    browser = get_browser()
    pause.until(get_sunday_3min_before_7am())

    login(browser)
    book_start_time = book_for7_with_delay(delay_mill)
    pause.until(book_start_time)

    browser.get(get_booking_page_url(day, time, court))
    browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
    browser.find_element(By.ID, 'Player_three_Auto').send_keys(player3)
    browser.find_element(By.ID, 'Player_Four_Auto').send_keys(player4)
    browser.find_element(By.ID, 'Booking Duration').send_keys('120')
    final_btn_e = "//*[contains(@onclick, 'final')]"
    browser.find_element(By.XPATH, final_btn_e).click()

    ts = book_start_time.strftime("%H:%M:%S.%f")
    print(datetime.datetime.now().strftime("%H:%M:%S.%f") + " - clicked BOOK button by " + ts)
    try:
        print(browser.find_element(By.CSS_SELECTOR, "body > h1").text + " by " + ts)
    except NoSuchElementException:
        print(datetime.datetime.now().strftime("%H:%M:%S.%f") + " *** Booked successfully by " + ts)
    finally:
        browser.close()


def book_for7_with_delay(delay_mill):
    return get_sunday_7am() + datetime.timedelta(milliseconds=delay_mill)


def get_sunday_3min_before_7am():
    return get_sunday_7am() - datetime.timedelta(minutes=3)


def get_sunday_7am():
    return next_weekday_date("sun").replace(hour=7, minute=0, second=0, microsecond=0)


def next_weekday_date_str(day_abbr):
    return next_weekday_date(day_abbr).strftime("%Y-%m-%d")


def login(browser):
    browser.get(LOGIN_URL)  # retry this
    browser.find_element(By.ID, 'userid').send_keys(LOGIN_ID)
    browser.find_element(By.ID, 'password').send_keys(LOGIN_PW)
    browser.find_element(By.ID, 'submit').click()


def get_booking_page_url(day, time, court):
    booking_param = ("item={0}&date={1}&time={2}%20PM"
                     .format(str(court), next_weekday_date_str(day), format_hour(time)))
    return BOOKING_URI + booking_param


def get_browser():
    options = Options()
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(options=options)


def next_weekday_date(day_abbr):
    # Map abbreviations to day numbers (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    try:
        target_day = days.index(day_abbr.lower())
    except ValueError:
        return "Invalid day abbreviation. Use mon, tue, wed, thu, fri, sat, or sun."

    today = datetime.datetime.now()
    days_ahead = (target_day - today.weekday() + 7) % 7
    return today + datetime.timedelta(days=days_ahead)


def format_hour(hour):
    return f"{hour:02}:00"  # Convert hour to two-digit string and add ":00" for minutes
