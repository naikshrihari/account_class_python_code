import function as fun

class Account:
    count=0
    def __init__(self,name="",mobile=""):
        Account.count=Account.count+1
        self.__accId=Account.count
        self.__name=name
        self.__mobile=mobile

    def __str__(self):
        return '\nAccount Id: '+str(self.__accId)+'\nname: '+str(self.__name)+'\nMobile No: '+str(self.__mobile)

    def getAccId(self):
        return self.__accId

    def getName(self):
        return self.__name

    def getMobile(self):
        return self.__mobile

    def setMobile(self, mobile):
        self.__mobile=mobile

    def setMobile(self, name):
        self.__name=name

    def deposit(self, amount):
        self.__balance+=amount

    
    
class SavingAccount(Account):
    interestRate = 6.0
    maxWithdrawAmt = 25000
    minBalance = 5000
    
    def __init__(self,name="",mobile="",chequeBookNo="",balance=0.0):
        super().__init__(name,mobile)
        self.__balance=balance
        self.__chequeBookNo=chequeBookNo


    def __str__(self):
        return super().__str__()+'\nChequeBookNo: '+str(self.__chequeBookNo)+'\nBalance: '+str(self.__balance)

    def setBalance(self, balance):
        self.__balance=balance

    def setChequeBookNo(self, chequeBookNo):
        self.__chequeBookNo=chequeBookNo

    def getBalance(self):
        return self.__balance

    def getChequeBookNo(self):
        return self.__chequeBookNo

    def withdraw(self, amount):
        self.__Balance-=amount


    
class CurrentAccount(Account):
    interestRate = 6.0
    maxWithdrawAmt = 25000
    minBalance = 5000
    
    def __init__(self,name="",mobile="",chequeBookNo="",balance=0.0):
        super().__init__(name,mobile)
        self.__balance=balance
        self.__chequeBookNo=chequeBookNo


    def __str__(self):
        return super().__str__()+'\nChequeBookNo: '+str(self.__chequeBookNo)+'\nBalance: '+str(self.__balance)


    def setBalance(self, balance):
        self.__balance=balance

    def setChequeBookNo(self, chequeBookNo):
        self.__chequeBookNo=chequeBookNo
        
    def getBalance(self):
        return self.__balance

    def getChequeBookNo(self):
        return self.__chequeBookNo

    def withdraw(self, amount):
        self.__balance -= amount
        
##    def withdraw(account, acc):
##        amount=float(input("Enter the amount to withdraw: "))
##        remainBalance=acc.getBalance()-amount
##        try:
##            if remainBalance >0:
##                acc.setBalance(remainBalance)
##                count=searchAcc(account, acc)
##                if count!=-1:
##                    account.pop(count)
##                    account.insert(count, acc)
##                    return account
##                else:
##                    print("Account not found.")
##
##            else:
##                raise RemainBalanceException("Amount is less than zero i.e thansaction not possible.")
##        except :
##            print("Amount is less than zero i.e thansaction is not possible.")
##        

    


    
if __name__=='__main__':
    p = SavingAccount('shrihari','12345','122123',1234)
    print(p)

    p = SavingAccount('shrihari','12345','122123',1234)
    print(p)

    a = Account("shrihari", "99999")
    print(a)
