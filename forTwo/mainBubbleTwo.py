import datetime
import threading

import bubbleForTwo

jin = 'Bora Jin'

start = datetime.datetime(2022, 3, 2, 0, 0, 0)
playDate = "2022-03-03"
playTime = "10:00"  # 01:00
courtNumber = 2  # 1-2
player2 = jin

for interval in range(1, 2000, 200):
    stagger_book = start + datetime.timedelta(milliseconds=interval)
    thread = threading.Thread(target=bubbleForTwo.book,
                              args=(jin, playTime, playDate, courtNumber, stagger_book))
    thread.start()
    print(stagger_book.strftime("%S.%f") + " - " + datetime.datetime.now().strftime("%H:%M:%S.%f"))
