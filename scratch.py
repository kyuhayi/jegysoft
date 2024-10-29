# import datetime
import datetime
import pause
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# days_ = datetime.datetime.today() + datetime.timedelta(days=1)
# print(days_.replace(hour=7, minute=0, second=0, microsecond=0))

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# browser = webdriver.Chrome(service=s, options=None)

# start = datetime.datetime(2022, 3, 26, 16, 0, 0)
#
# for interval in range(0, 40, 2):
#     hit_it = start + datetime.timedelta(seconds=interval)
#     print(hit_it.strftime("%H:%M:%S.%f"))

# for interval in range(3, 5, 1):
#     print(interval)

def next_weekday_date(day_abbr):
    # Map abbreviations to day numbers (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    try:
        target_day = days.index(day_abbr.lower())
    except ValueError:
        return "Invalid day abbreviation. Use mon, tue, wed, thu, fri, sat, or sun."

    today = datetime.datetime.now()
    days_ahead = (target_day - today.weekday() + 7) % 7
    if days_ahead == 0:
        days_ahead = 7  # Ensures we get the next occurrence, not today if it's the same day
    next_date = today + datetime.timedelta(days=days_ahead)
    return next_date.strftime("%Y-%m-%d")


# Example usage:
print(next_weekday_date("tue"))  # Output example: "2023-11-22"


def format_hour(hour):
    # Convert hour to two-digit string and add ":00" for minutes
    return f"{hour:02}:00"


# Example usage:
print(format_hour(7))  # Output: "06:00"
print(format_hour(8))  # Output: "08:00"
