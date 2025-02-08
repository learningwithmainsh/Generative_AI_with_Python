#ATM System

class ATM:
    def __init__(self, balance, pin):
        self._balance = balance
        self.__pin = pin  # Storing PIN securely (in a real system, use hashing)

    def __authenticate_user(self, pin):
        """Private method to authenticate user"""
        if pin == self.__pin:
            print("Authentication Success!!")
            return True
        else:
            print("Authentication Failed!")
            return False
    
    def withdraw(self, amount, pin):
        """Withdraws money after authentication"""
        if self.__authenticate_user(pin):  # Fixed function call
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrawn: {amount}. Remaining Balance: {self._balance}")
            else:
                print("Insufficient balance")

# Example Usage
atm = ATM(1000, 1234)  # Initializing ATM with balance and PIN
atm.withdraw(400, 1234)  # Successful withdrawal
atm.withdraw(4000, 1234) # Prints "Insufficient balance"
atm.withdraw(100, 1111)  # Authentication failure
