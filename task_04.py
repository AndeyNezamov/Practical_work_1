positive_ratings = negative_ratings = 0

while True:
    rating = int(input('Введите число: '))
    if rating > 0:
        positive_ratings += 1
    elif rating < 0:
        negative_ratings += 1
    else:
        break
print(f'Кол-во положительных чисел: {positive_ratings}\n'
      f'Кол-во отрицательных чисел: {negative_ratings}')