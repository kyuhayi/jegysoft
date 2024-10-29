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

player2 = kwak
player3 = keum
player4 = park

for mills in range(0, 1000, 90):  # Every 90 milliseconds for 1 second from 07:00
    threading.Thread(target=egg.book("mon", 8, 1, player2, player3, player4, mills)).start()

for mills in range(1000, 2000, 90):  # Every 90 milliseconds for 1 second from 07:01
    threading.Thread(target=egg.book("mon", 6, 1, player2, player3, player4, mills)).start()

