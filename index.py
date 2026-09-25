class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

# Deposit Method
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ৳{amount}")
        else:
            print("Invalid amount!")

# Withdraw Method
    def withdraw(self, amount):

        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ৳ {amount}")
        else:
            print("Invalid amount or insufficient balance!")
# Check Balance Method
    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: ৳{self.__balance}")
# Transfer Money Method
    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            other_account.__balance += amount

            print(f"Transferred: ৳{amount}")
            print(f"To: {other_account.name}")
        else:
            print("Invalid amount or insufficient balance!")

print("================================")
print("       🏦 MY BANK")
print("================================")

name = input("Enter your name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(name, initial_balance)

# Create second account
receiver_name = input("Enter receiver name: ")
receiver_balance = float(input("Enter receiver initial balance: "))

receiver = BankAccount(receiver_name, receiver_balance)

while True:

    print("\n================================")
    print("           BANK MENU")
    print("================================")

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transfer Money")
    print("5. Receiver Balance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
        
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        amount = float(input("Enter transfer amount: "))
        account.transfer(receiver, amount)

    elif choice == "5":
        receiver.check_balance()

    elif choice == "6":
        print("\nThank you for using My Bank! 👋")
        break
        
    else:
        print("Invalid choice!")
