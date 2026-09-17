class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

# Deposit Money
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ৳{amount}")
        else:
            print("Invalid amount!")

    # Withdraw Money
    def withdraw(self, amount):

        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ৳ {amount}")
        else:
            print("Invalid amount or insufficient balance!")

    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ৳{self.__balance}")
# -------------------                ------------------

