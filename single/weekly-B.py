import datetime
import threading

import worker

jin = 'Bora Jin'
kwak = 'Dongho Kwak'

start = datetime.datetime(2023, 2, 5, 7, 0, 0)
play_date = "2023-02-09"  # 2022-08-12
play_time = "09:00"  # 01:00
court_number = 1  # 1-2
player2 = jin

uri = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"
param = "item=" + str(court_number) + "&date=" + play_date + "&time=" + play_time + "%20PM"
book_page_url = uri + param
login_url = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
login = "Ky.oakville@gmail.com"
passwd = "planet00"

for interval in range(0, 100, 5):
    time_open_book_page = start
    time_hit_it = start + datetime.timedelta(seconds=interval)
    thread = threading.Thread(target=worker.book,
                              args=(book_page_url, time_open_book_page, time_hit_it, login_url, login, passwd,
                                    player2))
    thread.start()
