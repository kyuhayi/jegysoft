import threading
import egg

kwak = 'Dongho Kwak'
yoo = 'Matthew Yoo'
jung = 'Jaeyong Jung'
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
player4 = jung

day = "mon"

threading.Thread(target=egg.book, args=(1, 8, 2, day, player2, player3, player4, USER, PW)).start()
threading.Thread(target=egg.book, args=(3, 8, 1, day, player2, player3, player4, USER, PW)).start()
threading.Thread(target=egg.book, args=(5, 6, 2, day, player2, player3, player4, USER, PW)).start()
threading.Thread(target=egg.book, args=(7, 6, 1, day, player2, player3, player4, USER, PW)).start()
