import datetime
import pause
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

start = datetime.datetime(2022, 3, 26, 16, 0, 0)

for interval in range(0, 40, 2):
    hit_it = start + datetime.timedelta(milliseconds=interval * 100)
    print(hit_it.strftime("%H:%M:%S.%f"))
