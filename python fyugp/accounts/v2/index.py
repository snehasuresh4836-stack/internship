from helper import *
y=0
while y==0:
    opt=menu()
    if(opt==1):
       create_accounts() 
    if(opt==2):
       display_accounts() 
    if(opt==3):
       delete_accounts() 
    if(opt==4):
       update_accounts() 
    y=int(input("Do you want to continue?Press 0 for yes"))
