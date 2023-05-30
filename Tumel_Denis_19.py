# Класс Company:
# Создайте класс Company
class Company:
# Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста:
# 1:junior, 2:middle, 3:senior, 4:lead.
    levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}
# Создайте метод __init__(), внутри которого будут определены два protected свойства:
# 1) _index - передается параметром и 2) _level - принимает из словаря levels значение с ключом _index
    def __init__ (self, index,levels=None):
        self._index = index
        self._level= self.levels[index]

# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def _level_up(self):
        self._index+=1
# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        if self._index==4:
            print('Программист достиг высшей квалификации в нашей компании!')
# Класс Programmer:
# Создайте класс Programmer
class Programmer(Company):
# Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
    def __init__(self,name,age,level):
        super().__init__(level,{1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'})
# 1) name - передается параметром, является публичным,
        self.name=name
# 2)age - возраст
        self.age=age
# 3) level – уровень квалификации на основе словаря из Company
        self.level=self.levels[level]
# Создайте метод work(), который заставляет программиста работать,
# что позволяет ему становиться более квалифицированным с помощью метода _level_up() родительского класса
    def work(self):
        self.level=self._index
        if self.level==4:
            print('У Вас максимальная квалификация в нашей компании')
        else:
            self._level_up()
            self.level=self.levels[self._index]
        # Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
        print( f'Программист:{self.name}, ему {self.age} лет, имеет квалификацию {self.level} ')
        self.is_lead()
# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто любой текст).
    @staticmethod
    def knowledge_base():
        print("ООП сложная, но интересная тема!")

# Вызовите справку по программированию
# Создайте объекты классов Company и Programmer
# Используя объект класса Programmer, повысьте свой уровень квалификации
# Дойдите до уровня lead
Programmer.knowledge_base()
it=Company(4)
TDL=Programmer('Denis',30,1)
TDL.info()
TDL.work()
TDL.info()
TDL.work()
TDL.info()
TDL.work()
TDL.info()
TDL.work()
TDL.info()