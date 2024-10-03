student_grades  = { }

def add_student(name,grade):
    student_grades[name] = grade
    print(f"added {name} with a {grade}")

def update(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marta are  updated {grade}")
    else:
        print(f"{name} is no found!")

def delete_stu(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has benn successfully deleted")  

    else:
        print(f"{name} is no found!")

def display_stu():
    for name,grade in student_grades.items():
        print(f"{name}: {grade}")

    else:
        print(f"no fount students ")    




def main():
    while True:
        print("\n students grade management system")
        print("1: add students")
        print("2: update students")
        print("3: delete students")
        print("4: view students")
        print("5: exit students")

        choice = int(input("enter your choice = "))
        if choice == 1:
            name = input("enter student name =  ")
            grade = int(input("enter the studen grade = "))
            add_student(name,grade)

        elif choice ==2 :
            name = input("enter student name =  ")
            grade = int(input("enter the studen grade = "))
            update(name,grade)

        elif choice == 3 :
            name = input("enter student name =  ")
            delete_stu(name)

        elif choice == 4 :
            display_stu()

        elif choice == 5 :
            print("closing  the program,,,")
            break 

        else:
            print("invalid input ")      
               

main()
        

