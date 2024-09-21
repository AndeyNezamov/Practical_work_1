import random
count = 0
number = random.randint(0, 10)
while True:
    count += 1
    user = int(input('Введите число: '))
    if user > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif user < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print(f'Вы угадали! Число попыток: {count}')
        break