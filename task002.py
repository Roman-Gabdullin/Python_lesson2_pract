number = int(input('Введите трехзначное число: '))
if number < 999 or number > 100:
    sum = number % 10 + number // 10 % 10 + number // 100 % 10
    print(f'Сумма цифр числа = {sum}')
else: print('Ошибка ввода')