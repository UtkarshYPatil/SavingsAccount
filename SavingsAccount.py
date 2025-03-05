class SavingsAccount:
    def __init__(self, account_no, account_holder_name):
        self.account_no = account_no
        self.account_holder_name = account_holder_name
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful. New balance: Rs.", self.balance)
        else:
            print("Invalid deposit amount.")

    def withdrawal(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. New balance: ₹.", self.balance)
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print("Account balance for", self.account_holder_name, "(Account No.", self.account_no, "): Rs.", self.balance)

account_no = int(input("Enter account number: "))
account_holder_name = input("Enter account holder name: ")

account = SavingsAccount(account_no, account_holder_name)

while True:
        print("Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display balance")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            deposit_amount = float(input("Enter deposit amount: Rs. "))
            account.deposit(deposit_amount)
        elif choice == 2:
            withdrawal_amount = float(input("Enter withdrawal amount: Rs. "))
            account.withdrawal(withdrawal_amount)
        elif choice == 3:
            account.display_balance()
        elif choice == 0:
            print("Exiting. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
            