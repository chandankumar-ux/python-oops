class BankAccount:
    def __init__(self,Acc_no,Owner_name,Balance):
        self.Acc_no=Acc_no
        self.Owner_name=Owner_name
        self.Balance=Balance
    
    def deposit(self,deposit):
        self.Balance+=deposit
        print(f"your deposit amount is {deposit} now your current balance is {self.Balance}")
    
    def withdraw(self,amount):
        self.Balance-=amount
        print(f"your withdrawal amount is {amount} now your current balance is {self.Balance}")
        
    def check_balance(self):
        print("Your Available amount is",self.Balance)
    
b1=BankAccount(1234564,"Chandan Kumar",25000)
b1.deposit(65000)
b1.withdraw(20000)
b1.check_balance()