class Account:
    # Starts the parameters.
    def __init__(self, client, number_account, account_balance, account_limit=1000.0):
        print(f'Initializing an account.\n'
              f'Client {client}')
        self.client = client
        self.number_account = number_account
        self.account_balance = account_balance
        self.account_limit = account_limit
    # Creates the deposit method
    def deposit(self, value):
        self.account_balance += value
    # Create the withdram method
    def withdrawMoney(self, value):
        # Checks whether the account has a withdrawal balance
        if self.account_balance < value:
            print('You do not have money enough to withdraw.')
            return False
        else:
            self.account_balance -= value
            return True
    # Create the account statement method.
    def accountStatement(self):
        print(f'Number Account: {self.number_account}\n'
              f'Balance: {self.account_balance}.')
    # Create the method transfer
    def transfer(self, destine, value):
        withdraw = self.withdrawMoney(value)
        # Checks whether the account has a transfer balance.
        if withdraw == False:
            print(f'You do not have money enough to do a transfer, your account balance is {self.account_balance}')
            return False
        else:
            destine.deposit(value)
            return True
