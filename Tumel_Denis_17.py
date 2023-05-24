 # Описать два метода в классе: один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова,
# то выводить все гласные, иначе согласные;
# если передаю число, то вывести произведение суммы чётных цифр на длину числа.

class Str_Namber:
    def transformation(self,obj):
        if type(obj)==str:
            glas=[]
            soglas=[]
            glass=['a','e','i','o','u','y']
            for i in obj:
                if i in glass: glas.append(i)
                else: soglas.append(i)
            if len(glas)*len(soglas)<=self.len_str_namber(obj):
                return str(glas)
            else:
                return str(soglas)
        elif type(obj)==int:
            summa=0
            for i in str(obj):
                if int(i) % 2 == 0:
                    summa += int(i)
            return summa*self.len_str_namber(obj)

    # Длину строки и числа искать во втором методе.
    def len_str_namber(self,obj):
        return len(str(obj))

kuk=Str_Namber()
print(kuk.len_str_namber('knkkjk'))
print(kuk.transformation('kapan'))
print(kuk.transformation(123))