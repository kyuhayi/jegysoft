import threading
import roe

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
player3 = park
player4 = jung

for mills in range(0, 3000, 200):  # Every 190 milliseconds for 3 second from 07:00
    threading.Thread(target=roe.book, args=("wed", 8, 1, player2, player3, player4, mills)).start()

