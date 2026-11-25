#Menu-Driven Student Infromation System
student={}
def add_student():
    roll=input("Enter Roll No. : ")
    name=input("Enter Name : ")
    dept=input("Enter department : ")
    student[roll]={"Name":name, "Department":dept}
    print("Student added succesfully.")

def view_student():
    if not student:
        print("No student records found. ")
        return
    print("\n---Student Records---")
for roll, data in student.items():
    print("Roll No:", roll,
          "|Name : ",data["Name"],"|Department : ",data["Department"])
    
def search_student():
    roll=input("Enter Roll No to Search : ")
    if roll in student:
        print(student[roll])
    else:
        print("Student not found.")
        
def delete_student():
    roll=input("Enter No to delete : ")
    if roll in student:
        del student[roll]
        print("Student deleted succesfully.")
    else:
        print("Student not found.")
        while True:
            print("\n.Add Student")
            print("\n.View student")
            print("\n.Search Student")
            print("\n.Delete Student")
            print("\n.Exit")
            choice =input("Enter Your Choice : ")
            if choice == "1":
                add_student()
            elif choice == "2":
                view_student()
            elif choice == "3":
                search_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice")
