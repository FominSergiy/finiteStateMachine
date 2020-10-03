
# class to hold & process transaction
class Account:
    def __init__(self):
        self.balance = 1000
        self.transactions = []

    def process_debit(self, num:int, name:str):
        self.balance = self.balance + num
        self.transactions.append(name + ' :' + str(num))

    def process_credit(self,num:int, name:str):
        self.balance = self.balance - num
        self.transactions.append(name + ' :' + str(num))

    def print_balance(self):
        print('you current balance is : ' + str(self.balance))

    def get_balance(self):
        return self.balance

    def print_transactions(self):
        for i in self.transactions:
            print(i)
