import datetime
import threading

import worker

kwak = 'Dongho Kwak'
yoo = 'Matthew Yoo'
jung = 'Andrew Jung'

start = datetime.datetime(2022, 7, 11, 22, 0, 0)
playDate = "2022-07-19"
playTime = "09:00"  # 01:00
courtNumber = 1  # 1-6
player2 = kwak
player3 = yoo
player4 = jung

for interval in range(0, 40, 2):
    open_book_page = start - datetime.timedelta(minutes=1, seconds=interval * 4)
    hit_it = start + datetime.timedelta(milliseconds=interval * 100)
    thread = threading.Thread(target=worker.book,
                              args=(player2, player3, player4, playTime, playDate, courtNumber, open_book_page, hit_it))
    thread.start()
