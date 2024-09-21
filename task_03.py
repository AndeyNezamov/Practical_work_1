numbers = int(input('Введите число: '))
count = 0
while numbers > 0:
    numbers //= 10
    count += 1
print(f'Количество цифр в числе - {count}')