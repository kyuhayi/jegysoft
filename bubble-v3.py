import datetime

import pause
import selenium.webdriver.common.action_chains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

kwak = 'Dongho Kwak'
keum = 'Jongho Keum'
park = 'Sean Park'
seong = 'Marcus Seong'
yoo = 'Matthew Yoo'
daewoong = 'Dae Jung'
jung = 'Jaeyong Jung'
choi = 'John Choi'
hwang = 'Dy Hwang'


booking_start = datetime.datetime(2023, 12, 10, 7, 0, 1, microsecond=500)
playDate = "2023-12-12"
playTime = "08:00"  # 01:00
courtNumber = 1  # 1-2
player2 = yoo
player3 = hwang
player4 = choi


print("==================================================")
print("Booking is running at " + booking_start.strftime("%b %d %a, %H:%M:%S"))
print("==================================================")
pause.until(booking_start - datetime.timedelta(minutes=1))
loginUrl = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
login_id = "Ky.oakville@gmail.com"
login_pw = ""
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.google.com")
actions = selenium.webdriver.common.action_chains.ActionChains(browser)
browser.get(loginUrl)
browser.get(loginUrl)
username = browser.find_element(By.ID, 'userid')
username.send_keys(login_id)
pw = browser.find_element(By.ID, 'password')
pw.send_keys(login_pw)

browser.find_element(By.ID, 'submit').click()  # login one min before
pause.until(booking_start)  # because we are too fast

uri = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"

param = "item={court}&date={date}&time={time}%20PM".format(court=courtNumber, date=playDate, time=playTime)

browser.get(uri + param)

browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
browser.find_element(By.ID, 'Player_three_Auto').send_keys(player3)
browser.find_element(By.ID, 'Player_Four_Auto').send_keys(player4)
browser.find_element(By.ID, 'Booking Duration').send_keys('120')
final_btn = "//*[contains(@onclick, 'final')]"
WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, final_btn)))
browser.find_element(By.XPATH, final_btn).click()

