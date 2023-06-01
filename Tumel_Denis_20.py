import sqlite3
# Вы создаете БД для учета задач в команде разработки.
conn = sqlite3.connect('Tasks.db')
cursor = conn.cursor()
# Вам необходимо создать базу данных для хранения информации о задачах и их статусе.
# Каждая задача должна иметь уникальный идентификатор,
# название,
# описание и
# статус (выполнена или невыполнена).
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Task_execution_control(
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     Name TEXT,
     Description TEXT,
     Status TEXT
     )'''
 )


#
# Напишите программу на языке Python, которая создает базу данных SQLite,
# добавляет в нее несколько задач и позволяет пользователю получать информацию о задачах.
cursor.execute(
    '''INSERT INTO Task_execution_control(
    Name, 
    Description,
    Status) 
    VALUES(
    'Домашнее задание',
    'по математике',
    'не выполненно'
    )'''
)
cursor.execute(
    '''INSERT INTO Task_execution_control(
    Name, 
    Description,
    Status) 
    VALUES(
    'Домашнее задание',
    'по физике',
    'выполненно'
    )'''
)
cursor.execute(
    '''INSERT INTO Task_execution_control(
    Name, 
    Description,
    Status) 
    VALUES(
    'Контрольная работа',
    'по химии',
    'выполненно'
    )'''
)
cursor.execute(
    '''INSERT INTO Task_execution_control(
    Name, 
    Description,
    Status) 
    VALUES(
    'Зачет',
    'по иностранному языку',
    'выполненно'
    )'''
)
conn.commit()

cursor.execute('''SELECT Name, Description, Status FROM Task_execution_control WHERE Status = 'выполненно' ''')
print(*cursor)

Table=cursor.execute('''SELECT * FROM Task_execution_control ORDER BY ID''')
print(*Table)

cursor.execute('''SELECT * FROM Task_execution_control''')
List = cursor.fetchall()

for i in List:
    print(*i)