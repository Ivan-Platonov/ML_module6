print('Задача 1. Кубы чисел')

# В один из вечеров к Васе домой пришёл племянник и пожаловался на сложности с уроками математики: у него никак не получалось разобраться со степенями чисел. Вася решил помочь племяннику и написать программу, которая позволит наглядно увидеть возведение чисел в третью степень.

# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.

number = ''
digit = 1
while number == '':
  try:
    number = int(input('Введите число: '))
  except ValueError:
    print('Необходимо ввсести число!!!')
print()

if number > 0:
  while digit <= number:
    print(digit ** 3)
    digit += 1
else:
  while digit >= number:
    print(digit ** 3)
    digit -= 1