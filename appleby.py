import datetime

import pause
import selenium.webdriver.common.action_chains
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

bora = 'BORA JIN'

booking_start = datetime.datetime(2021, 8, 20, 0, 0, 1)
date = 'Aug 27'
time = '07:00'  # 01:00
amPm = 'PM'
court = 3
player2 = bora

print("==================================================")
print("Booking is running at " + booking_start.strftime("%b %d %a, %H:%M:%S"))
print("==================================================")
pause.until(booking_start - datetime.timedelta(minutes=1))
loginUrl = 'https://www.tennisclubsoft.com/appleby/home/login.do'
login_id = "Ky.oakville@gmail.com"
login_pw = ""
browser = webdriver.Chrome("/home/kyuu/opt/chromedriver99")
actions = selenium.webdriver.common.action_chains.ActionChains(browser)
browser.get(loginUrl)
browser.get(loginUrl)
username = browser.find_element(By.ID, 'userid')
username.send_keys(login_id)
pw = browser.find_element(By.ID, 'password')
pw.send_keys(login_pw)

browser.find_element(By.ID, 'submit').click()  # login one min before
pause.until(booking_start)

browser.find_element(By.XPATH, "//a[contains(text(), '%s') and contains(text(), 'Book Court')]" % court).click()
browser.find_element(By.XPATH, "//*[@id='caldaylink']/a[contains(text(), '%s')]" % date).click()
playTime = time + ' ' + amPm
threesome = browser.find_element(By.XPATH, ("//*[contains(text(), '%s')]" % playTime)
if court == 1 or court == 2:
    shouldClick = threesome[0]
elif court == 3 or court == 4:
    shouldClick = threesome[1]
else:
    shouldClick = threesome[2]
shouldClick.click()
browser.find_element_by_name('Team_Two_Auto').send_keys(player2)
final_ = "//*[contains(@onclick, 'final')]"
WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, final_)))
browser.find_element(By.XPATH, final_).click()

# actions.move_to_element(browser.find_element(By.XPATH, "//*[contains(@onclick, 'final')]")).click().perform()
