num = int(input('Введите трехзначное число   '))
if num > 999 or num < 100:
    print('Вы ввели не трехзначное число')
else:
    n1 = num // 100
    n2 = num // 10 % 10
    n3 = num % 10
    print('Сумма цифр равна', n1 + n2 + n3)