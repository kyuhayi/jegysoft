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

for mills in range(0, 2000, 90):  # 0, 100, 200, 300, 400 ... 2000
    threading.Thread(target=egg.book, args=("sat", 8, 1, player2, player3, player4, mills)).start()
