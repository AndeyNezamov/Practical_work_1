deposit = int(input('Ваш вклад в банке составляет: '))
percent = int(input('Процентная ставка составляет: '))
result = int(input('Итоговая сумма вклада: '))
year = 0
while True:
    year += 1
    deposit += int(deposit * (percent/100))
    print(f'{year}:{deposit}')
    if deposit >= result:
        print(f'Должно пройти {year} лет до того как на счету будет {result}')
        break
