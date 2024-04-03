import datetime
import threading

import worker

kwak = 'Dongho Kwak'
yoo = 'Matthew Yoo'
jung = 'Andrew Jung'

start = datetime.datetime(2022, 7, 11, 22, 0, 0)
play_date = "2022-07-19"
play_time = "09:00"  # 01:00
court_number = 1  # 1-6
player2 = kwak
player3 = yoo
player4 = jung

court_item = {1: "1", 2: "2", 3: "3", 4: "4", 5: "19", 6: "20"}
uri = "https://www.tennisclubsoft.com/appleby/home/newView.do?id=304&calendar=7&"
param = "item=" + court_item[court_number] + "&date=" + play_date + "&time=" + play_time + "%20PM"
book_page_url = uri + param
login_url = 'https://www.tennisclubsoft.com/appleby/home/login.do'
login = "Ky.oakville@gmail.com"
passwd = ""

for interval in range(3, 5, 1):
    open_book_page = start
    hit_it = start + datetime.timedelta(seconds=interval)
    thread = threading.Thread(target=worker.book,
                              args=(book_page_url, open_book_page, hit_it, login_url, login, passwd,
                                    player2, player3, player4))
    thread.start()
