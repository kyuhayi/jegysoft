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

player2 = yoo
player3 = hwang
player4 = choi

for mills in range(0, 3000, 190):  # Every 190 milliseconds for 3 second from 07:00
    threading.Thread(target=egg.book("mon", 8, 1, player2, player3, player4, mills)).start()

for mills in range(2000, 5000, 290):
    threading.Thread(target=egg.book("mon", 6, 1, player2, player3, player4, mills)).start()

