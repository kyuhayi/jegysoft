from selenium import webdriver
import datetime

start = datetime.datetime(2022, 3, 26, 16, 0, 0)

for interval in range(0, 40, 2):
    hit_it = start + datetime.timedelta(milliseconds=interval * 100)
    print(hit_it.strftime("%H:%M:%S.%f"))
