import sqlite3 #импортируем модуль sqlite3
conn=sqlite3.connect('Tasks.db') #обращаюсь к существуещей БД, через переменную указатель
cursor=conn.cursor() #создаю объект для взаимодействия с таблицами

# 1. Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# cursor.execute(
#                '''CREATE TABLE IF NOT EXISTS TASK_1(
#                ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                col_2 TEXT,
#                col_3 TEXT
#                )'''
# )# создал таблицу (если такой еще нет) с тремея колонками, ID индивидуальное для каждой строки, второй и третий столбец текст
# conn.commit()
# Заполнить её с помощью INSERT данными (3 записи).
# cursor.execute(
#                 '''INSERT INTO TASK_1(
#                 col_2,
#                 col_3
#                 )
#                 VALUES(
#                 'кирпич',
#                 'твердый'
#                 )'''
# )
# conn.commit()
# cursor.execute(
#                 '''INSERT INTO TASK_1(
#                 col_2,
#                 col_3
#                 )
#                 VALUES(
#                 'вата',
#                 'мягкая'
#                 )'''
# )
# conn.commit()
# cursor.execute(
#                 '''INSERT INTO TASK_1(
#                 col_2,
#                 col_3
#                 )
#                 VALUES(
#                 'вода',
#                 'жидкая'
#                 )'''
# ) #заполнил таблицу тремя записями
# conn.commit() #сохранил изменения

# Удалить с помощью DELETE 2 запись.

# cursor.execute('''DELETE FROM TASK_1 WHERE ID=2''')# удалил из таблицы запись с ID=2
# conn.commit()#Сохранил

# Обновить значения 3-ей записи на: hello world с помощью UPDATE

# cursor.execute('''UPDATE TASK_1 SET col_2='hello',col_3='world' WHERE ID=3''') #изменение 3-й записи
# conn.commit() # сохраненние

# *Записать данные с таблицы в текстовый файл в три колонки. Первая – id, вторая и третья с данными
# cursor.execute('''SELECT*FROM TASK_1''')#делаем запрос из нашей таблицы по всем столбцам и строкам
# k=cursor.fetchall() #используем переменную для вугрузки информации из БД в питон в виде списка кортежей
# with open('task_1.txt','a',encoding='utf-8') as f: #создаем текстовый файл и открываем его
#
# for i in k:
#     f.write(str(i[0]))
#     f.write(str('   '))
#     f.write(str(i[1]))
#     f.write(str('   '))
#     f.write(str(i[2]))
#     f.write("\n")# проходим по нашему списку и поэлементно записываем в файл, для красоты между элементами используем табуляцию,
#     #в конце кортежа переходим на новую строку

#
#
# # 2. В БД из первого задания удалить первую ПОЛОВИНУ записей,
# a=int(len(k)/2)
# cursor.execute('''DELETE FROM TASK_1 WHERE ID<=(SELECT MAX(ID) FROM TASK_1) / 2.''')# удаляем первую  половину списка
# conn.commit()# сохроняем таблицу
# cursor.execute('''UPDATE TASK_1 SET col_2='goodbye' WHERE ID>(SELECT MAX(ID) FROM TASK_1) / 2.''')
# conn.commit()# сохроняем таблицу
# # а вторую обновить на любые значения.
#
# cursor.execute('''UPDATE TASK_1 SET col_2='goodbye' WHERE ID>?''',(a,))# изменяем значение в колонке col_2 в строках второй половины таблицы
# conn.commit()# сохроняем таблицу
# # ВРучную удалять нельзя!
# # Если строк нечетное количество, то округляем в меньшую сторону!

#3. Создать 2 таблицы в Базе Данных

# cursor.execute('''CREATE TABLE IF NOT EXISTS TEXT_1(col_1 TEXT)''') # создал таблицу с одним столбцом с даннами текст
# conn.commit()
# cursor.execute('''CREATE TABLE IF NOT EXISTS INT_1(col_1 INTEGER)''')# создал таблицу с одним столбцом с даннами число
#conn.commit()
# # Одна будет хранить текстовые данные(1 колонка)
# # Другая числовые(1 колонка)
# # Есть список, состоящий из чисел и слов.
# my_list = ['Home','Work',29, 9, 2022]
# # Если элемент списка слово, записать его в соответствующую таблицу,
# for i in my_list:
#     if type(i)==str: # усли элемент слово
#         cursor.execute('''INSERT INTO TEXT_1(col_1) VALUES (?)''',(i,)) # то делаем инсерт в первую таблицу
#         conn.commit()
#
# # затем посчитать длину слова и записать её в числовую таблицу
#         cursor.execute('''INSERT INTO INT_1(col_1) VALUES (?)''',(len(i),)) # добавляю длинну слова во вторую таблицу
#         conn.commit()
# # Если элемент списка число: проверить, если число чётное записать его в таблицу чисел,
#     elif type(i)==int: # если элемент число
#         if i%2==0: # проверяю на четность
#             cursor.execute('''INSERT INTO INT_1(col_1) VALUES (?)''', (i,)) # добавляю это число в список с числами
#             conn.commit()
#
# # если нечётное, то записать во вторую таблицу слово: «нечётное»
#         else:
#             cursor.execute('''INSERT INTO TEXT_1(col_1) VALUES ('нечётное')''') # записываем слово во текстовую таблицу
#             conn.commit()
# # Если число записей во второй таблице больше 5, то удалить первую запись в первой таблице.
# cursor.execute('''SELECT*FROM INT_1''')
# k=cursor.fetchall()# вытаскиваю данные из таблиц в переменные
#
#
# if len(k)>5: #если в второй таблице число строк больше 5
#     cursor.execute('''DELETE FROM TEXT_1 WHERE ID=1''') # удаляем первую запись из первой таблицы
#     conn.commit()
# # Если меньше, то обновить первую запись в первой таблице на «hello»
# else:
#     cursor.execute('''UPDATE TEXT_1 SET col_1='hello' WHERE ID=1 ''') #редактирую первую запись в текстовой таблице
#     conn.commit()
# conn.close()