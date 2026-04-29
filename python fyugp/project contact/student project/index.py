from helper import *
from fileop import *
y = 0
data = read_student()
set_student(data)

while y == 0:
    opt = menu()
    
    if opt == 1:
        add_student()
        
    elif opt == 2:
        view_student()
        
    elif opt == 3:
        search_student()
        
    elif opt == 4:
        delete_student()
        
    elif opt == 5:
        print("Exiting...")
        break 
    write_student(get_student())  
        
    y = int(input("Do you want to continue? Press 0 for yes: "))

    

