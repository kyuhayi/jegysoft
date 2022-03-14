from selenium import webdriver

driver = webdriver.Chrome("/home/kyuu/opt/chromedriver99")
str1 = driver.capabilities['browserVersion']
str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
print(str1)
print(str2)
print(str1[0:2])
print(str2[0:2])
if str1[0:2] != str2[0:2]: 
  print("please download correct chromedriver version")