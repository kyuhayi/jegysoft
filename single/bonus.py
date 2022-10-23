import datetime
import threading

import worker

jin = 'Bora Jin'

start = datetime.datetime(2022, 10, 23, 19, 28, 0)
play_date = "2022-10-23"  # 2022-08-12
play_time = "10:00"  # 01:00
court_number = 2  # 1-2
player2 = jin

uri = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"
param = "item=" + str(court_number) + "&date=" + play_date + "&time=" + play_time + "%20PM"
book_page_url = uri + param

for interval in range(0, 40, 2):
    time_open_book_page = start - datetime.timedelta(minutes=1, seconds=interval * 4)
    time_hit_it = start + datetime.timedelta(milliseconds=interval * 100)
    thread = threading.Thread(target=worker.book,
                              args=(player2, book_page_url, time_open_book_page, time_hit_it,
                                    'https://www2.tennisclubsoft.com/bubbletennis/home/login.do',
                                    "Ky.oakville@gmail.com", "planet00"))
    thread.start()
