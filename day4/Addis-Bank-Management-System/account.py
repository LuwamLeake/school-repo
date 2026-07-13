# account.py

class Account:
    def __init__(self, owner, account_number, initial_balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute

    @property
    def balance(self):
        """Read-only access to the account balance."""
        return self.__balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit failed: Amount must be greater than zero.")
            return

        self.__balance += amount
        print(f"Deposit successful! {amount:.2f} ETB added.")
        print(f"Current Balance: {self.__balance:.2f} ETB")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal failed: Amount must be greater than zero.")
            return

        if amount > self.__balance:
            print("Withdrawal failed: Insufficient funds.")
            return

        self.__balance -= amount
        print(f"Withdrawal successful! {amount:.2f} ETB withdrawn.")
        print(f"Current Balance: {self.__balance:.2f} ETB")


# ----------------------------
# Test the Account class
# ----------------------------

account1 = Account("Binyam", "100001", 5000)
account2 = Account("Sara", "100002", 2500)

print(f"\nAccount Owner: {account1.owner}")
print(f"Balance: {account1.balance:.2f} ETB")

account1.deposit(1500)
account1.withdraw(2000)
account1.withdraw(10000)
account1.deposit(-500)

print("\n--------------------------\n")

print(f"Account Owner: {account2.owner}")
print(f"Balance: {account2.balance:.2f} ETB")

account2.deposit(500)
account2.withdraw(1000)
account2.withdraw(-50)