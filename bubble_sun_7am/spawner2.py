import threading
import egg

kwak = 'Dongho Kwak'
yoo = 'Matthew Yoo'
jung = 'Jaeyong Andrew Jung'
keum = 'Jongho Keum'
choi = 'John Choi'
park = 'Sean Park'
hwang = 'Dy Hwang'
jin = 'Bora Jin'
yi = 'Kyuha Yi'

USER = "ky.oakville@gmail.com"
PW = "planet00"

player2 = kwak
player3 = park
player4 = keum
day = "wed"

threading.Thread(target=egg.book, args=(1, 8, 2, day, player2, player3, player4, USER, PW)).start()
threading.Thread(target=egg.book, args=(3, 8, 1, day, player2, player3, player4, USER, PW)).start()
threading.Thread(target=egg.book, args=(5, 6, 2, day, player2, player3, player4, USER, PW)).start()
threading.Thread(target=egg.book, args=(7, 6, 1, day, player2, player3, player4, USER, PW)).start()



# for sec in range(1, 8, 3):  # Every 190 milliseconds for 3 second from 07:00
#     threading.Thread(target=egg.book, args=("thu", 8, 2, player2, player3, player4, sec)).start()


