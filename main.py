import sys
import function as fun
import classes as cs

account=[]


while True:
    print("1. Create account")
    print("2. Close Account")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Deposit")
    print("6. Transfer fund")
    print("7. Show all account")
    print("8. Exit")

    choice=int(input("Enter the choice: "))

    if choice==1:
        account=fun.createAccount(account)
        
    elif choice==2:
        account=fun.removeAccount(account)
    
    elif choice==3:
        id1=int(input("Enter the id to withdraw: "))
        amount=float(input("Enter the amount: "))
        acc=fun.searchById(account, id1)
        account=fun.withdrawAmount(account, acc, amount)
        
    
    elif choice==4:
        id1=int(input("Enter the id for check balance: "))
        acc=fun.searchById(account, id1)
        showBalance(acc)
    
    elif choice==5:
        id1=int(input("Enter the id to deposit : "))
        amount=float(input("Enter the amount: "))
        acc=fun.searchById(account, id1)
        account=fun.depositAmount(account, acc, amount)
    
    elif choice==6:
        account=fun.transferFund(account)
    
    elif choice==7:
        fun.showAll(account)
    
    elif choice==8:
        sys.exit(0)
    
    
