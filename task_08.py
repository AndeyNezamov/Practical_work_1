start = 1
finish = 101
count = 1

while True:
    number = (start + finish) // 2
    print(f'Загаданное число равно, больше или меньше? {number}')
    user = int(input('1 — равно, 2 — больше, 3 — меньше: '))
    if user == 1:
        print(f'Угадал с {count} попытки')
        break
    elif user == 2:
        start = number
    elif user == 3:
        finish = number
    count += 1