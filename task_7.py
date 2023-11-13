print('Задача 7. Игра «Угадай число»')

# В одной из практических работ мы делали задачу, где папа-программист написал для сына программу, которая просит его угадать число. Недостаток программы был в том, что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного улучшить саму игру.

# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4

goal_number, user_number, count = (0,)*3
goal_number = int(input('Введите целевое число: '))

while user_number != goal_number:
  user_number = int(input('Введите число: '))
  if user_number < goal_number:
    print('Число меньше, чем нужно. Попробуйте ещё раз!')
  elif user_number > goal_number:
    print('Число больше, чем нужно. Попробуйте ещё раз!')
  count += 1
print('Вы угадали! Число попыток: ', count)
