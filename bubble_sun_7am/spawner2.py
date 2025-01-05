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

player2 = hwang
player3 = keum
player4 = jung

for mills in range(1000, 2000, 900):  # Every 190 milliseconds for 3 second from 07:00
    threading.Thread(target=egg.book, args=("tue", 8, 2, player2, player3, player4, mills)).start()

for mills in range(3000, 4000, 900):  # Every 190 milliseconds for 3 second from 07:00
    threading.Thread(target=egg.book, args=("tue", 8, 1, player2, player3, player4, mills)).start()

