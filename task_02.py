name = input('Введите ваше имя: ')
debt = int(input('Сумма долга: '))
flag = True
while flag:
    print(f'Ваша задолжность составляет: {debt}')
    money = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? :'))
    debt -= money
    if debt > 0:
        print(f'Маловато, {name}. Давайте ещё раз.')
    else:
        flag = False
        print(f'Отлично, {name}! Вы погасили долг. Спасибо!')