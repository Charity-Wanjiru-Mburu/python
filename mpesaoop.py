from abc import ABC, abstractmethod
# encapsulation
class Account:
    def __init__(self,account_id,holder_name,balance):
        self.account_id=account_id
        self.holder_name=holder_name
        self.balance=balance
    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited {amount}.New balance:{self.balance}")
    def withdraw(self,amount):
        print(f"Attempting to with {amount} from account with balance {self.balance}")
        if amount <=self.balance:
            self.balance-=amount
            print(f"Withdraw {amount} from account with balance {self.balance}")
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.balance
    def get_holder_name(self):
        return self.holder_name
# inheritance
class customer(Account):
    def __init__(self,account_id,holder_name,balance,phone_number):
        super().__init__(account_id,holder_name, balance)
        self.phone_number=phone_number

# polymorphism
class transaction:
    def __init__(self,amount):
        self.amount=amount
    def execute(self,account):
        pass
class deposittransaction(transaction):
    def execute(self,account):
        account.deposit(self.amount)
class withdrawtransaction(transaction):
    def execute(self,account):
        account.withdraw(self.amount)

# Abstraction
class paymentsystem(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
class mpesapaymentsystem(paymentsystem):
    def process_payment(self,amount):
        print(f"Processing Mpesa payment of {amount}")

# example usage
mpesa=mpesapaymentsystem()
account1=customer(1,"Charity",1000,786443232)
deposit=deposittransaction(500)
withdraw=withdrawtransaction(2000)

deposit.execute(account1)
withdraw.execute(account1)
print(f"The balance of {account1.get_holder_name()} is :{account1.get_balance()}")

mpesa=mpesapaymentsystem()
account2=customer(2,"Alice",3000,738290836)
deposit=deposittransaction(500)
withdraw=withdrawtransaction(5879)

deposit.execute(account2)
withdraw.execute(account2)