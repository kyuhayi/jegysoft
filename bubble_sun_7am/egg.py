import datetime

import pause
import selenium
import selenium.webdriver.chrome.options
import selenium.webdriver.edge.options
import selenium.webdriver.chrome.service
import webdriver_manager.chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

LOGIN_URL = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
BOOKING_URI = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"


def book(delay_sec, time, court, day, player2, player3, player4, user, pw):
    browser = get_edge()
    three_minute_to_go = sunday_3min_to_7am()
    browser.get(LOGIN_URL)
    print("3 min ahead proceed " + str(three_minute_to_go))
    pause.until(three_minute_to_go.timestamp())
    print("opening... login")
    login(browser, user, pw)
    book_start_time = sunday_7am_plus(delay_sec)
    print("(" + str(delay_sec) + ")" + "booking will proceed " + str(book_start_time))
    pause.until(book_start_time.timestamp())

    browser.get(str_booking_page_url(day, time, court))
    wait = WebDriverWait(browser, 10)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, 'Team_Two_Auto'))).send_keys(player2)
    pause.sleep(1)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, 'Player_three_Auto'))).send_keys(player3)
    pause.sleep(1)
    wait.until(expected_conditions.visibility_of_element_located((By.ID, 'Player_Four_Auto'))).send_keys(player4)
    # wait.until(expected_conditions.visibility_of_element_located((By.ID, 'Booking Duration'))).send_keys('120')
    pause.sleep(1)
    wait.until(expected_conditions.element_to_be_clickable((By.ID, "final"))).click()
    print("now " + datetime.datetime.now().strftime("%H:%M:%S"))
    pause.until(sunday_9pm())


def sunday_7am_plus(delay_sec):
    return date_7am_sunday() + datetime.timedelta(seconds=delay_sec)


def sunday_9pm():
    return date_7am_sunday() + datetime.timedelta(hours=14)


def sunday_3min_to_7am():
    return date_7am_sunday() - datetime.timedelta(minutes=3)


def date_7am_sunday():
    return date_next_weekday_by("sun") + datetime.timedelta(hours=7)


def str_date_next_weekday_by(day_abbr):
    return date_next_weekday_by(day_abbr).strftime("%Y-%m-%d")


def login(browser, user, pw):
    browser.get(LOGIN_URL)  # retry this
    browser.find_element(By.ID, 'userid').send_keys(user)
    browser.find_element(By.ID, 'password').send_keys(pw)
    browser.find_element(By.ID, 'submit').click()


def str_booking_page_url(day, time, court):
    booking_param = ("item={0}&date={1}&time={2}%20PM"
                     .format(str(court), str_date_next_weekday_by(day), str_formatted_hour(time)))
    return BOOKING_URI + booking_param


def get_chrome():
    options = selenium.webdriver.chrome.options.Options()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    chrome = selenium.webdriver.Chrome(options=options)
    return chrome


def get_edge():
    options = selenium.webdriver.edge.options.Options()
    options.add_argument("--inprivate")
    edge = selenium.webdriver.Edge(options)
    return edge


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

    today = datetime.datetime.today()
    days_ahead = (target_day - today.weekday() + 7) % 7
    d = today + datetime.timedelta(days=days_ahead)
    combine = datetime.datetime.combine(d, datetime.datetime.min.time())
    return combine


def str_formatted_hour(hour):
    return f"{hour:02}:00"  # Convert hour to two-digit string and add ":00" for minutes
