# Создайте класс BankAccount, который представляет банковский счет.
class BankAccount:
# У класса есть приватные свойства __account_number (номер счета) и __balance (баланс).
# Инициализатор __init__ используется для инициализации номера счета и начального баланса.
    def __init__(self,number,start_many):
        self.__account_number=number
        self.__balance=start_many
# Методы get_account_number и get_balance предоставляют доступ к приватным свойствам __account_number и __balance соответственно.
    def get_account_number(self):
         print( self.__account_number)

    def get_balance(self):
        print(self.__balance)
# Методы deposit и withdraw позволяют пополнять и снимать деньги со счета,
# при этом проверяя валидность операции (достаточно ли средств, корректно ли введена сумма для снятия).
    def deposit(self,add):
        self.__balance+=add
        print( self.__balance)


    def withdraw(self,summa_snjatija):
        if type(summa_snjatija)==int and summa_snjatija<=self.__balance:
            self.__balance -= summa_snjatija
            print( self.__balance)
        elif summa_snjatija>self.get_balance():
            print ("Недостаточно средств! ")


# В основной части кода мы создаем экземпляр класса BankAccount с номером счета "123456789"  и начальным балансом 1000.
Main=BankAccount(123456789,1000)

# Затем мы используем методы для получения номера счета и баланса, а также для пополнения и снятия средств.

Main.get_account_number()
Main.get_balance()
Main.deposit(2345)
Main.withdraw(1245)
# Выводятся результаты операций.



