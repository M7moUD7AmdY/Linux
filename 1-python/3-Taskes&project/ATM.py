# Sample ATM accounts
accounts = [
    {'name': 'Mahmoud', 'pin': '123', 'balance': 1000},
    {'name': 'Hamdi', 'pin': '456', 'balance': 500},
    {'name': 'Rashed', 'pin': '789', 'balance': 1500}
]



# Function to validate account PIN
def validate_pin(pin):
    for account in accounts:
        if account['pin'] == pin:
            return account
    return None

# Function to withdraw money from an account
def withdraw(account, amount):
    if amount > account['balance']:
        print('Insufficient funds')
    else:
        account['balance'] -= amount
        print(f'Withdrawal successful. New balance: {account["balance"]}')

# Function to deposit money to an account
def deposit(account, amount):
    account['balance'] += amount
    print(f'Deposit successful. New balance: {account["balance"]}')

# Prompt user for PIN
pin = input('Enter your PIN: ')

# Validate the PIN
account = validate_pin(pin)
if account is None:
    print('Invalid PIN')
else:
    # Display account balance
    print(f'Welcome, {account["name"]}. Your balance is {account["balance"]}')

    # Prompt user for transaction type
    transaction_type = input('Enter "W" for withdrawal or "D" for deposit: ')

    # Process transaction
    if transaction_type == 'W':
        amount = int(input('Enter withdrawal amount: '))
        withdraw(account, amount)
    elif transaction_type == 'D':
        amount = int(input('Enter deposit amount: '))
        deposit(account, amount)
    else:
        print('Invalid transaction type')
