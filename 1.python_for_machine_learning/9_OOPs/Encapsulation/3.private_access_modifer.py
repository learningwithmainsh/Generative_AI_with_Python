# private Access mOdifier
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance  #returns the balance

account1 = BankAccount("123456", 1000)
print(account1.get_balance())  

