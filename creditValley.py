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
jung = 'Andrew Jung'
yoo = 'Matthew Yoo'
hwang = 'Douglas Hwang'
keum = 'Jongho Keum'
guest = 'Guest Player'

booking_start = datetime.datetime(2021, 8, 25, 7, 0, 1)
date = 'Aug 26'
time = '09:00'  # 01:00
amPm = 'PM'
court = 3  # 1-8
player2 = jung
player3 = kwak
player4 = yoo

print("==================================================")
print("Booking is running at " + booking_start.strftime("%b %d %a, %H:%M:%S"))
print("==================================================")
pause.until(booking_start - datetime.timedelta(minutes=1))
loginUrl = 'https://ts2.clubinterconnect.com/cvt/home/login.do'
login_id = "Ky.oakville@gmail.com"
login_pw = "planet00"
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

#  Book Court 1 - 6
if 1 <= court <= 6:
    courtString = '1 - 6'
else:
    courtString = '7 - 8'
browser.find_element(By.XPATH, "//a[contains(text(), '%s') and contains(text(), 'Book Court')]" % courtString).click()
browser.find_element(By.XPATH, "//*[contains(text(), '%s')]" % date).click()

playTime = time + ' ' + amPm
threesome = browser.find_element(By.XPATH, ("//*[contains(text(), '%s')]" % playTime))

if court == 1:
    shouldClick = threesome[0]
elif court == 2:
    shouldClick = threesome[1]
elif court == 3:
    shouldClick = threesome[2]
elif court == 4:
    shouldClick = threesome[3]
elif court == 5:
    shouldClick = threesome[4]
elif court == 6:
    shouldClick = threesome[5]
elif court == 7:
    shouldClick = threesome[0]
elif court == 8:
    shouldClick = threesome[1]
else:
    shouldClick = threesome[0]

shouldClick.click()
browser.find_element(By.ID, 'Team_Two_Auto').send_keys(player2)
browser.find_element(By.ID, 'Player_three_Auto').send_keys(player3)
browser.find_element(By.ID, 'Player_Four_Auto').send_keys(player4)
browser.find_element(By.ID, 'Booking Duration').send_keys('90')
final_btn = "//*[contains(@onclick, 'final')]"
WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, final_btn)))
browser.find_element(By.XPATH, final_btn).click()

# actions.move_to_element(browser.find_element(By.XPATH, "//*[contains(@onclick, 'final')]")).click().perform()
