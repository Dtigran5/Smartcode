class bank_account:
    def __init__(self, account_number, balance = 0, transactions = []):
        self.__account_number = account_number
        self.__balance = balance
        self.transactions = transactions

    def deposit(self,amount):
        self.__balance += amount
        self.transactions.append(f" Deposit: +${amount}")
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.transactions.append(f" Withdrawal: -${amount}")
        else:
            print("Error")
    def transfer(self,other_account, amount):
        if self.__balance >=  amount:
            self.__balance -= amount
            other_account.__balance += amount
            self.transactions.append(f'Transfer to {other_account.__account_number}: -${amount}')
            other_account.transactions.append(f'Transfer from {self.__account_number}: +${amount}')
    def generate_statement(self):
        return self.__balance, self.transactions
    def get_balance(self):
        return self.__account_number
    def clear_transactions(self):
        self.transactions.clear()
        return self.transactions

