print('21.06.2024')
current_year = input('Какой сейчас год? ') # «input» у нас запрашивает ввод переменной с клавиатуры
print(type(current_year))
name = input('Введите ваше имя: ')
print(type(name))
print('Здравствуйте,',name)
date_of_birth = input('В каком году Вы родились: ')
print('В этом году Вам',int(current_year) - int(date_of_birth)) # но дучше сразу в переменных задать int, см. ниже
confirm = input('Правильно? ')
next_year_age = int(current_year) - int(date_of_birth) + 1 # пример, son_date_bith = int(input())
print('В следующем году вам будет',next_year_age,'лет.')
son_date_birth = int(input('В каком году родился ваш сын? ')) # но если int то далее в скобках должен стоять иной тип
# son_date_birth = int(input()) будет ошибкой
# C командой «input» всегда будет тип данных «str»
print('Но если напишем после строки точку, и, например, «upper» и запустим'.upper()) # получим перевод в верхний регистр
# НО ЕСЛИ НАПИШЕМ ПОСЛЕ СТРОКИ ТОЧКУ, И, НАПРИМЕР, «UPPER» И ЗАПУСТИМ
print('НО ЕСЛИ НАПИШЕМ ПОСЛЕ СТРОКИ ТОЧКУ, И, НАПРИМЕР, «lower» И ЗАПУСТИМ'.lower()) # получим перевод в нижний регистр
# но если напишем после строки точку, и, например, «lower» и запустим
# Напишем в кавычках «привет», поставим запятую, снова откроем кавычки и напишем «пока»
print('Привет от Никиты'.replace('Привет','Пока')) # Пока от Никиты - замена Привет на Пока
print('Привет от Никиты'.replace(' ','')) # ПриветотНикиты - удаление пробела
# система не понимала __old и __new, но с удалением конвертировала в них же, но меньшего размера
# Дополнительно о всех методах строк можно узнать по ссылке ниже:
# https://docs.python.org/3/library/stdtypes.html#string-methods