count_tasks = 0
flag = False
hour = 1
while hour <= 3:
    count_tasks += int(input('Сколько задач решит Максим?: '))
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if call == 1:
        flag = True
    hour += 1
else:
    print(f'Рабочий день закончился. Всего выполнено задач: {count_tasks}')
    if flag:
        print('Нужно зайти в магазин.')