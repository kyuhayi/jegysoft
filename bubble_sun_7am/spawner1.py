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
player3 = choi
player4 = kwak

threading.Thread(target=egg.book, args=("thu", 8, 2, player2, player3, player4, 1)).start()
threading.Thread(target=egg.book, args=("thu", 8, 1, player2, player3, player4, 3)).start()
threading.Thread(target=egg.book, args=("thu", 6, 2, player2, player3, player4, 5)).start()
threading.Thread(target=egg.book, args=("thu", 6, 1, player2, player3, player4, 7)).start()


# for sec in range(1, 8, 3):  # Every 190 milliseconds for 3 second from 07:00
#     threading.Thread(target=egg.book, args=("thu", 8, 2, player2, player3, player4, sec)).start()


