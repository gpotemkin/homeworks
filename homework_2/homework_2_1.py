# пользователь вводит слово. Для простоты будем считать,
# что слово не меньше 3 символов

# Считайте ввод и распечатайте:

# длину слова
# слово без первой буквы
# последний символ слова
# слово без последних двух букв
# слово в uppercase

print('Введите слово, состоящее из трех или большего количества букв')
user_word = str(input())
print('Длина слова: ', len(user_word), 'символа(ов)')
print('Слово без первой буквы: ', user_word[1:])
print('Последний символ слова: ', user_word[-1])
print('Слово без двух последних букв: ', user_word[0:-2])
print('Слово в верхнем регистре: ', user_word.upper())