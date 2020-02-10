import classes as cs
from exception import *

def createAccount(account):
    print("a. saving account")
    print("b. current account")

    choice=input("Enter your choice : ")

    if choice=="a":
        name=input("Enter the name: ")
        mobile=input("Enter the mobile: ")
        chequeBookNo=input("Enter the chequeBook number: ")
        balance=float(input("Enter the balance: "))
        acc=cs.SavingAccount(name, mobile, chequeBookNo, balance)
        account.append(acc)
        return account
        
    
    elif choice=="b":
        name=input("Enter the name: ")
        mobile=input("Enter the mobile number: ")
        chequeBookNo=input("Enter the chequeBookNo: ")
        balance=float(input("Enter the balance: "))
        acc=cs.CurrentAccount(name, mobile, chequeBookNo, balance)
        account.append(acc)
        return account
    
    else:
        print("Enter the correct choice!!!!!!")

def searchById(account, id):
    for acc in account:
        if acc.getAccId()==id:
            return acc

    else:
        print("Account Not found.")

def searchAcc(account, acc):
    count=0
    for acc1 in account:
        if acc==acc1:
            return count
        count+=1
    else:
        return -1

def removeAccount(account):
    print("@@Remove Account@@")
    id = int(input("Enter the id : "))
    acc=searchById(account, id)
    account.remove(acc)
    return account
    
    

def showAll(account):
    for acc in account:
        print("\n")
        print(acc)
    print("\n")

def transferFund(account):
    id1=int(input("Enter the account number from where : "))
    id2=int(input("Enter the account number to where: "))
    amount=float(input("Enter the amount to transfer: "))
    acc1=searchById(account, id1)
    acc2=searchById(account, id2)
    
    account=withdrawAmount(account, acc1, amount)
    account=depositAmount(account, acc2, amount)
    
    return account

##def depositAmount(account, acc, amount):
##        
##        remainBalance=acc.getBalance()+amount
##        acc.setBalance(remainBalance)
##        count=searchAcc(account, acc)
##        if count!=-1:
##            account.pop(count)
##            account.insert(count, acc)
##            return account
##        else:
##            print("Account not found.")
##
####
def depositAmount(account, acc, amount):
        
        remainBalance=acc.getBalance()+amount
        count=searchAcc(account, acc)
        acc.deposit(amount)
        
        if count!=-1:
            account.pop(count)
            account.insert(count, acc)
            return account
        else:
            print("Account not found.")
            
        
            


##def withdraw(account, acc, amount):
##       
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
def withdrawAmount(account, acc, amount):
       
        remainBalance=acc.getBalance() - amount
        try:
            if remainBalance >0:
                count=searchAcc(account, acc)
                acc.withdraw(amount)
                account.pop(count)
                account.insert(count, acc)
                return account
                    
            

            else:
                raise RemainBalanceException("Amount is less than zero i.e thansaction not possible.")
        except :
            print("Amount is less than zero i.e thansaction is not possible.")

def showBalance(acc):
    print(acc.getBalance())
