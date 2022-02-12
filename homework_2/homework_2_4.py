# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой
print('Введите три числа через пробел')
user_input = input().split(' ')
num1 = int(user_input[0])
num2 = int(user_input[1])
num3 = int(user_input[2])

user_input_set = {num1, num2, num3}
if len(user_input_set) < 3:
    sum_num = 0
else:
    sum_num = sum(user_input_set)

print('Сумма числе равна: ', sum_num)





#input_to_set = set(user_input)
#print(input_to_set)