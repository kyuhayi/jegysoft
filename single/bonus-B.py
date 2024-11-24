import datetime
import threading

import single_worker

jin = 'Bo Jin'
kwak = 'Dongho Kwak'
court_number = 2  # 1-2
player2 = jin
uri = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"

start = datetime.datetime(2024, 11, 21, 0, 0, 0)
play_date = "2024-11-21"  # 2022-08-12
play_time = "07:00"  # 01:00
param = "item=" + str(court_number) + "&date=" + play_date + "&time=" + play_time + "%20PM"
book_page_url = uri + param
login_url = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
login = "Ky.oakville@gmail.com"
passwd = "planet00"



for interval in range(0, 40, 2):
    time_open_book_page = start - datetime.timedelta(minutes=1, seconds=interval * 4)
    time_hit_it = start + datetime.timedelta(milliseconds=interval * 100)
    thread = threading.Thread(target=single_worker.book,
                              args=(book_page_url, time_open_book_page, time_hit_it, login_url, login, passwd,
                                    player2))
    thread.start()
