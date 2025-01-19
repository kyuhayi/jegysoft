# import datetime
import datetime
import pause
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from bubble_sun_7am.egg import date_next_weekday_by, str_date_next_weekday_by, date_7am_sunday, sunday_3min_to_7am

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


# Example usage:
print(str_date_next_weekday_by("mon"))  # Output example: "2023-11-22"
print(date_7am_sunday())  # Output example: "2023-11-22"
print(sunday_3min_to_7am())  # Output example: "2023-11-22"
print(date_next_weekday_by("thu"))  # Output example: "2023-11-22"
print(date_next_weekday_by("fri"))  # Output example: "2023-11-22"
print(date_next_weekday_by("sat"))  # Output example: "2023-11-22"
print(date_next_weekday_by("sun"))  # Output example: "2023-11-22"
print(date_next_weekday_by("mon"))  # Output example: "2023-11-22"
