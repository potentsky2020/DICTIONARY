class Account:
    def __init__(self):
        self._balance = 0.0
    
    @property
    def balance(self):
        """Get the current balance."""
        return self._balance
    
    def deposit(self, n: float):
        self._balance += n
        """Deposit money into the account."""
    
    def withdraw(self, n: float):
        self._balance -= n
        """Withdraw money from the account."""

def main():
    account = Account()
    print(f"Initial account balance: {account.balance}")
    account.deposit(1000.0)
    print(f"Balance after deposit: {account.balance}")
    account.withdraw(50.0)
    print(f"Balance after withdrawal: {account.balance}")

if __name__ == "__main__":
    main()