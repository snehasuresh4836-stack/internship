student = []
def set_student(data):
    global student
    student = data

def get_student():
    return student

def add_student():
    Id = input("Enter Id: ")
    name = input("Enter name: ")
    m1 = int(input("Enter mark1: "))
    m2 = int(input("Enter mark2: "))
    m3 = int(input("Enter mark3: "))
    
    student.append((Id, name, m1, m2, m3))


def view_student():
    print(student)


def search_student():
    Id = input("Enter Id to search: ")
    
    for s in student:
        if s[0] == Id:
            print("Student details")
            print("Id:", s[0])
            print("Name:", s[1])
            print("m1:", s[2])
            print("m2:", s[3])
            print("m3:", s[4])
            
            calculate_grade(s)   
            return
    
    print("Student does not exist")


def calculate_grade(s):   
    total = s[2] + s[3] + s[4]
    avg = total / 3
    
    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    print("Total:", total, "Avg:", avg, "Grade:", grade)


def delete_student():
    i = int(input("Enter index to delete: "))
    
    if i < len(student):
        student.pop(i)
        print("Deleted")
    else:
        print("Invalid index")


def menu():
    print("\nMenu")
    print("1 -> Add student")
    print("2 -> View student")
    print("3 -> Search student")
    print("4 -> Delete student")
    print("5 -> Exit")
    
    op = int(input("Enter your option: "))
    return op
