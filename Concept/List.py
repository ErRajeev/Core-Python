class Bank:
 
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to Len Den bank")
    def account(self,name,amount,acno,phno,pin,lists):
        self.name=name
        self.amount=amount
        self.acno=acno
        diction={}
        diction['name']=name
        diction['amount']=amount
        diction['account_number']=acno
        diction['phn no']=phno
        diction['pin']=pin
        lists.append(diction)
        print(diction)
    def deposit(self):
        acc=int(input("enter the acc no:"))
        pin=int(input("enter the pin"))
        for i in range(len(lists)):
            if(acc==lists[i]['account_number'] and pin==lists[i]['pin']):
                amount=float(input("Enter amount to be Deposited: "))
                lists[i]['amount']+=amount
                print("\n Amount Deposited:",amount)
                print(lists)
    def withdraw(self):
        acc=int(input("enter the acc no:"))
        pin=int(input("enter the pin"))
        for i in range(len(lists)):
            if(acc==lists[i]['account_number'] and pin==lists[i]['pin']):
                amount=float(input("Enter amount to be withdrawn: "))
                if(lists[i]['amount']>amount):
                    lists[i]['amount']-=amount
                    print("\n Amount withdraw:",amount)
                    print(lists)
            else:
                print("\n Insufficient balance")
    def display(self):
        acc=int(input("enter the acc no:"))
        pin=int(input("enter the pin"))
        for i in range(len(lists)):
            if(acc==lists[i]['account_number'] and pin==lists[i]['pin']):
                print("\n Amount in account:",lists[i]['amount'])
                print(lists)
    def displayall(self):
        print("helo")
        for i in range(len(lists)):
            print("\n account holder name:",lists[i]['name'])
            print("\n account holder phnno:",lists[i]['phn no'])
            print("\n Amount in account:",lists[i]['amount'])
    def close(self):
        acc=int(input("enter the acc no:"))
        pin=int(input("enter the pin"))
        c=input("are u sure ,u want to close the account(yes ore no)")
        if c=="yes":
            for i in range(len(lists)):
                if(acc==lists[i]['account_number']):
                    lists.remove(lists[i])
                    print("account closed")
    def modify(self):
        acc=int(input("enter the acc no:"))
        pin=int(input("enter the pin"))
        c=input("are u sure ,u want to modify the account(yes ore no)")
        for i in range(len(lists)):
            if(acc==lists[i]['account_number'] and pin==lists[i]['pin']):
                if c=="yes":
                    print(''' 1-edit name \n 2-phone no''')
                    cho=int(input("enter the choice"))
                    for i in range(len(lists)):
                        if(acc==lists[i]['account_number']):
                            if(cho==1):
                                name=input("enter the name to be updated:")
                                lists[i]['name']=name
                            elif cho==2:
                                phnno=input("enter the name to be updated:")
                                lists[i]['phn no']=phnno
s = Bank()
lists=[]
print('''
1-create account
2-deposit
3-withdraw
4-balance Enquiry
5-all account holders list
6-close an account
7-modify account
''')
while(1):
    choice=int(input("enter the choice:"))
    if choice==1:        
        name=input("enter the name:")
        amount=float(input("enter the amount:"))
        acno=int(input("enter the account no:"))
        phno=int(input("enter the phnno:"))
        pin=int(input("enter the pin no:"))
        s.account(name,amount,acno,phno,pin,lists)
    elif choice==2:
        s.deposit()
    elif choice==3:
        s.withdraw()
    elif choice==4:
        s.display()
    elif choice==5:
        s.displayall()
    elif choice==6:
        s.close()
    elif choice==7:
        s.modify()
    else:
        print("EXIT")
        break

