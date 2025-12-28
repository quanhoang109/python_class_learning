# Bank Account System Project

A complete banking system demonstrating all major OOP concepts.

## Features

### Account Types
- **Checking Account**: No interest, overdraft allowed up to $500, $10 monthly fee (waived if balance ≥ $1000)
- **Savings Account**: 2% annual interest, limited to 6 withdrawals per month
- **Business Account**: 1% annual interest, $0.50 transaction fee per withdrawal

### Operations
- Deposit money
- Withdraw money
- Transfer between accounts
- Apply interest
- View transaction history
- Monthly maintenance

## OOP Concepts Demonstrated

### 1. Encapsulation
- Private attributes: `_account_number`, `_balance`, `_owner`
- Read-only properties: `account_number`, `owner`, `balance`
- Internal methods: `_add_transaction()`, `_check_withdrawal_limit()`

### 2. Inheritance
```
Account (abstract base)
├── CheckingAccount
├── SavingsAccount
└── BusinessAccount
```

### 3. Polymorphism
- Each account type implements `calculate_interest()` differently
- Each account type has different withdrawal rules
- Same interface, different behavior

### 4. Abstraction
- Abstract base class `Account` defines interface
- Child classes must implement `calculate_interest()` and `_check_withdrawal_limit()`
- Implementation details hidden from user

## Running the Project

```bash
python projects/bank_system/main.py
```

## Usage Example

```python
# Create bank
bank = Bank("My Bank")

# Create accounts
checking = bank.create_account('checking', 'Alice', 500)
savings = bank.create_account('savings', 'Bob', 2000)

# Perform operations
checking.deposit(300)
checking.withdraw(100)
savings.transfer(500, checking)

# Apply interest
savings.apply_interest()

# View history
checking.get_transaction_history()
```

## Class Diagram

```
┌─────────────────────┐
│   Transaction       │
├─────────────────────┤
│ - timestamp         │
│ - type             │
│ - amount           │
│ - balance_after    │
└─────────────────────┘

┌─────────────────────┐
│   Account (ABC)     │
├─────────────────────┤
│ - _account_number   │
│ - _owner           │
│ - _balance         │
│ - _transactions[]  │
├─────────────────────┤
│ + deposit()        │
│ + withdraw()       │
│ + transfer()       │
│ + apply_interest() │
│ # calculate_interest()│ (abstract)
└─────────────────────┘
         △
         │
    ┌────┴────────────┐
    │                 │
┌───────────┐   ┌─────────────┐   ┌──────────────┐
│ Checking  │   │  Savings    │   │  Business    │
│ Account   │   │  Account    │   │  Account     │
└───────────┘   └─────────────┘   └──────────────┘
```

## Extension Ideas

1. Add account PIN/password authentication
2. Implement daily withdrawal limits
3. Add loan accounts
4. Create account statements (PDF export)
5. Add multi-currency support
6. Implement interest compounding options
7. Add joint account support
8. Create mobile banking interface
