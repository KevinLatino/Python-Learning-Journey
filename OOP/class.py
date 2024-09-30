class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print(f"Hi, mi name is {self.name} and my age is {self.age}")

person1 = Person("Kevin", 30)
person1.print_info()

class BankAccount:
    
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount
        self.total_balance = initial_amount
    
    def deposit(self, deposit_amount):
        self.total_balance = self.initial_amount + deposit_amount
        print(self.total_balance)
        
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.total_balance:
            print("Error")
        else: 
            new_balance = self.total_balance - withdraw_amount
            print("Completed, now your balance is: ", new_balance)
    
    
account1 = BankAccount(1000)
account1.deposit(2000)
account1.withdraw(1000)