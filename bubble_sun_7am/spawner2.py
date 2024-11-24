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

for mills in range(0, 3000, 200):  # Every 190 milliseconds for 3 second from 07:00
    threading.Thread(target=egg.book, args=("thu", 8, 1, player2, player3, player4, mills)).start()

for mills in range(3000, 6000, 900):  # Every 190 milliseconds for 3 second from 07:00
    threading.Thread(target=egg.book, args=("thu", 8, 2, player2, player3, player4, mills)).start()

