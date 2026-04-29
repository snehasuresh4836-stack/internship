accounts=[]
def create_accounts():
    payee=input("Enter payee")
    amount=input("Enter amount")
    date=input("Enter date")
    accounts.append((payee,amount,date))
def display_accounts():
    print(accounts)
def delete_accounts():
    i=int(input("Enter the index you want to remove"))
    accounts.pop(i)
def update_accounts():
    i=int(input("Enter the index you want to update"))
    name=input("Enter payee")
    email=input("Enter amount")
    mobile=input("Enter date")
    accounts[i]=(payee,amount,date)
def menu():
    print("Menu")
    print("1->For insert new accounts")
    print("2->For Display accounts")
    print("3->For Delete accounts")
    print("4->For Update")
    op=int(input("Enter Your Option"))
    return op