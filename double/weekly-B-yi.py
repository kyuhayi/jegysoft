import datetime
import threading

import worker

kwak = 'Dongho Kwak'
yoo = 'Matthew Yoo'
jung = 'Jaeyong Jung'
dae_jung = 'Dae Jung'
seong = 'Marcus Seong'
keum = 'Jongho Keum'
choi = 'John Choi'
park = 'Sean Park'
hwang = 'Dy Hwang'
jin = 'Bora Jin'
yi = 'Kyuha Yi'

start = datetime.datetime(2022, 11, 13, 7, 0, 4)
play_date = "2022-11-16"
play_time = "08:00"  # 01:00
court_number = 1  # 1-6
player2 = keum
player3 = park
player4 = jung


uri = "https://www2.tennisclubsoft.com/bubbletennis/home/newView.do?id=304&calendar=7&"
param = "item=" + str(court_number) + "&date=" + play_date + "&time=" + play_time + "%20PM"
book_page_url = uri + param
login_url = 'https://www2.tennisclubsoft.com/bubbletennis/home/login.do'
login = "ky.oakville@gmail.com"
passwd = "planet00"

for interval in range(3, 5, 1):
    open_book_page = start
    hit_it = start + datetime.timedelta(seconds=interval)
    thread = threading.Thread(target=worker.book,
                              args=(book_page_url, open_book_page, hit_it, login_url, login, passwd,
                                    player2, player3, player4))
    thread.start()
