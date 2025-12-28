"""
Bank Account System - Complete Project
=======================================

A comprehensive banking system demonstrating:
- Encapsulation (private attributes)
- Inheritance (different account types)
- Polymorphism (different interest calculations)
- Abstraction (account interface)

Run: python projects/bank_system/main.py
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class Transaction:
    """Represents a single transaction."""

    def __init__(self, transaction_type: str, amount: float, balance_after: float):
        self.timestamp = datetime.now()
        self.type = transaction_type
        self.amount = amount
        self.balance_after = balance_after

    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.type}: ${self.amount:.2f} | Balance: ${self.balance_after:.2f}"


class Account(ABC):
    """Abstract base class for all account types."""

    account_counter = 1000

    def __init__(self, owner: str, initial_balance: float = 0):
        self._account_number = f"ACC{Account.account_counter:06d}"
        Account.account_counter += 1
        self._owner = owner
        self._balance = initial_balance
        self._transactions: List[Transaction] = []
        self._is_active = True

        if initial_balance > 0:
            self._add_transaction("Initial Deposit", initial_balance)

    @property
    def account_number(self):
        """Read-only account number."""
        return self._account_number

    @property
    def owner(self):
        """Read-only owner name."""
        return self._owner

    @property
    def balance(self):
        """Get current balance."""
        return self._balance

    def _add_transaction(self, trans_type: str, amount: float):
        """Record a transaction."""
        transaction = Transaction(trans_type, amount, self._balance)
        self._transactions.append(transaction)

    def deposit(self, amount: float) -> bool:
        """Deposit money into account."""
        if not self._is_active:
            print("Error: Account is closed")
            return False

        if amount <= 0:
            print("Error: Deposit amount must be positive")
            return False

        self._balance += amount
        self._add_transaction("Deposit", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdraw money from account."""
        if not self._is_active:
            print("Error: Account is closed")
            return False

        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
            return False

        if amount > self._balance:
            print(f"Error: Insufficient funds. Available: ${self._balance:.2f}")
            return False

        # Check withdrawal limit
        if not self._check_withdrawal_limit(amount):
            return False

        self._balance -= amount
        self._add_transaction("Withdrawal", amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
        return True

    def transfer(self, amount: float, target_account: 'Account') -> bool:
        """Transfer money to another account."""
        if self.withdraw(amount):
            if target_account.deposit(amount):
                print(f"Transfer successful: ${amount:.2f} to {target_account.owner}")
                return True
            else:
                # Rollback if deposit fails
                self.deposit(amount)
                print("Transfer failed: Deposit to target account failed")
                return False
        return False

    @abstractmethod
    def _check_withdrawal_limit(self, amount: float) -> bool:
        """Check if withdrawal is within limits."""
        pass

    @abstractmethod
    def calculate_interest(self) -> float:
        """Calculate interest for this account type."""
        pass

    def apply_interest(self):
        """Apply interest to account."""
        if not self._is_active:
            print("Error: Account is closed")
            return

        interest = self.calculate_interest()
        if interest > 0:
            self._balance += interest
            self._add_transaction("Interest", interest)
            print(f"Interest applied: ${interest:.2f}. New balance: ${self._balance:.2f}")

    def get_transaction_history(self):
        """Display transaction history."""
        print(f"\n=== Transaction History for {self._account_number} ===")
        print(f"Owner: {self._owner}")
        print(f"Account Type: {self.__class__.__name__}")
        print(f"-" * 70)
        for transaction in self._transactions:
            print(transaction)
        print(f"-" * 70)
        print(f"Current Balance: ${self._balance:.2f}\n")

    def close_account(self):
        """Close the account."""
        self._is_active = False
        print(f"Account {self._account_number} closed")


class CheckingAccount(Account):
    """Checking account with no interest and unlimited withdrawals."""

    OVERDRAFT_LIMIT = 500  # Can go $500 into negative

    def __init__(self, owner: str, initial_balance: float = 0):
        super().__init__(owner, initial_balance)
        self.monthly_fee = 10.0

    def _check_withdrawal_limit(self, amount: float) -> bool:
        """Checking accounts can overdraft up to limit."""
        if self._balance - amount < -self.OVERDRAFT_LIMIT:
            print(f"Error: Exceeds overdraft limit of ${self.OVERDRAFT_LIMIT:.2f}")
            return False
        return True

    def calculate_interest(self) -> float:
        """No interest on checking accounts."""
        return 0.0

    def charge_monthly_fee(self):
        """Charge monthly maintenance fee."""
        if self._balance >= 1000:
            print("Monthly fee waived (balance >= $1000)")
            return

        self._balance -= self.monthly_fee
        self._add_transaction("Monthly Fee", -self.monthly_fee)
        print(f"Monthly fee charged: ${self.monthly_fee:.2f}")


class SavingsAccount(Account):
    """Savings account with interest and withdrawal limits."""

    INTEREST_RATE = 0.02  # 2% annual interest
    MAX_WITHDRAWALS_PER_MONTH = 6

    def __init__(self, owner: str, initial_balance: float = 0):
        super().__init__(owner, initial_balance)
        self.withdrawals_this_month = 0

    def _check_withdrawal_limit(self, amount: float) -> bool:
        """Savings accounts have withdrawal limits."""
        if self.withdrawals_this_month >= self.MAX_WITHDRAWALS_PER_MONTH:
            print(f"Error: Maximum {self.MAX_WITHDRAWALS_PER_MONTH} withdrawals per month reached")
            return False
        return True

    def withdraw(self, amount: float) -> bool:
        """Override to count withdrawals."""
        if super().withdraw(amount):
            self.withdrawals_this_month += 1
            return True
        return False

    def calculate_interest(self) -> float:
        """Calculate 2% annual interest (monthly)."""
        return self._balance * (self.INTEREST_RATE / 12)

    def reset_withdrawal_count(self):
        """Reset monthly withdrawal counter."""
        self.withdrawals_this_month = 0
        print("Monthly withdrawal counter reset")


class BusinessAccount(Account):
    """Business account with higher limits and fees."""

    INTEREST_RATE = 0.01  # 1% annual interest
    TRANSACTION_FEE = 0.50

    def __init__(self, owner: str, initial_balance: float = 0):
        super().__init__(owner, initial_balance)

    def _check_withdrawal_limit(self, amount: float) -> bool:
        """Business accounts have no special limits."""
        return True

    def withdraw(self, amount: float) -> bool:
        """Charge transaction fee on withdrawals."""
        if super().withdraw(amount):
            self._balance -= self.TRANSACTION_FEE
            self._add_transaction("Transaction Fee", -self.TRANSACTION_FEE)
            return True
        return False

    def calculate_interest(self) -> float:
        """Calculate 1% annual interest (monthly)."""
        return self._balance * (self.INTEREST_RATE / 12)


class Bank:
    """Bank that manages multiple accounts."""

    def __init__(self, name: str):
        self.name = name
        self.accounts: List[Account] = []

    def create_account(self, account_type: str, owner: str, initial_balance: float = 0) -> Account:
        """Create a new account."""
        account_types = {
            'checking': CheckingAccount,
            'savings': SavingsAccount,
            'business': BusinessAccount
        }

        if account_type.lower() not in account_types:
            print(f"Error: Invalid account type '{account_type}'")
            return None

        account_class = account_types[account_type.lower()]
        account = account_class(owner, initial_balance)
        self.accounts.append(account)

        print(f"\n✓ Created {account_type.title()} Account")
        print(f"  Account Number: {account.account_number}")
        print(f"  Owner: {account.owner}")
        print(f"  Initial Balance: ${account.balance:.2f}\n")

        return account

    def find_account(self, account_number: str) -> Account:
        """Find account by account number."""
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def display_all_accounts(self):
        """Display all accounts."""
        print(f"\n{'='*70}")
        print(f"{self.name} - All Accounts")
        print(f"{'='*70}")

        for account in self.accounts:
            print(f"{account.account_number} | {account.owner:20s} | "
                  f"{account.__class__.__name__:20s} | ${account.balance:>10.2f}")

        print(f"{'='*70}")
        print(f"Total Accounts: {len(self.accounts)}\n")


def demo_bank_system():
    """Demonstrate the complete bank system."""
    print("="*70)
    print("BANK ACCOUNT SYSTEM DEMO")
    print("="*70)

    # Create bank
    bank = Bank("Python National Bank")

    # Create different account types
    print("\n--- Creating Accounts ---")
    checking = bank.create_account('checking', 'Alice Johnson', 500)
    savings = bank.create_account('savings', 'Bob Smith', 2000)
    business = bank.create_account('business', 'Tech Startup Inc.', 10000)

    # Perform operations
    print("\n--- Account Operations ---")
    checking.deposit(300)
    checking.withdraw(100)

    savings.deposit(500)
    savings.withdraw(200)

    business.withdraw(1000)

    # Transfer
    print("\n--- Transfers ---")
    savings.transfer(300, checking)

    # Apply interest
    print("\n--- Applying Interest ---")
    checking.apply_interest()
    savings.apply_interest()
    business.apply_interest()

    # Transaction history
    print("\n--- Transaction History ---")
    checking.get_transaction_history()

    # Display all accounts
    bank.display_all_accounts()

    # Monthly operations
    print("\n--- Monthly Operations ---")
    checking.charge_monthly_fee()
    savings.reset_withdrawal_count()

    # Final status
    bank.display_all_accounts()


if __name__ == "__main__":
    demo_bank_system()
