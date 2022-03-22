import datetime
import threading

import worker

jin = 'Bora Jin'

start = datetime.datetime(2022, 3, 21, 17, 0, 0)
playDate = "2022-03-21"
playTime = "07:00"  # 01:00
courtNumber = 2  # 1-2
player2 = jin

for interval in range(0, 20, 2):
    open_book_page = start - datetime.timedelta(minutes=1, seconds=interval * 4)
    hit_it = start + datetime.timedelta(milliseconds=interval * 100)
    thread = threading.Thread(target=worker.book,
                              args=(jin, playTime, playDate, courtNumber, open_book_page, hit_it))
    thread.start()

