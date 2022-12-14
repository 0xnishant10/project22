import department
print('''Welcome to ProbBU,
         For the Bennettians,
         By the Bennettians,
         A Place for solutions of all your University Related Problems.''')

#Taking Input Student Info

name = input("Name: \n")
enroll_no = input("Enrollment Number: \n")
print('''Enter "H" for Hosteller and "D" for Day Scholar''')
def hosteller_or_day_scholar():
    global student
    student=input()
    if(student == "H" or student == "h"):
        print("Room Number: ")
        room=input()
    elif (student == "D" or student =="d"):
        pass
    else:
        print("Enter a valid option.")
        print('''Enter "H" for Hosteller and "D" for Day Scholar''')
        hosteller_or_day_scholar()
hosteller_or_day_scholar()
phone_no = input("Phone Number: \n")


print("---------------------------------------------------------------------------------")


#Asking the department of Query

print("What Department do you want to raise your query in?")
def enter_department():
    global department_of_query
    if(student == "H" or student == "h"):
        print('''"1" for "IT Department"
"2" for "Finance Department"
"3" for "Maintenance Department"''')
        department_of_query=input()
        if(department_of_query == "1"):
            print(department.d1)
        elif(department_of_query == "2"):
            print(department.d2)
        elif(department_of_query == "3"):
            print(department.d3)
        else:
            print("Please select a valid query department.")
            enter_department()
    else:
        print('''"1" for "IT Department"
"2" for "Finance Department"''')
        department_of_query = input()
        if (department_of_query == "1"):
            print(department.d1)
        elif (department_of_query == "2"):
            print(department.d2)
        else:
            print("Please select a valid query department.")
            enter_department()
enter_department()


print("---------------------------------------------------------------------------------")


#Asking for category if the selected department is Maintenance when the student is Hosteller

def category_maintenance():
    if(department_of_query == "3"):
        print("Under what category of Maintenance do you have your query?")
        print('''"1" for "Furniture"
"2" for "Electrical"
"3" for "Cleaning"''')
        global category_of_maintenance_var
        category_of_maintenance_var = input()
        if(category_of_maintenance_var == "1"):
            print(department.sub_d1)
        elif(category_of_maintenance_var == "2"):
            print(department.sub_d2)
        elif(category_of_maintenance_var == "3"):
            print(department.sub_d3)
        else:
            print("Please select a valid category.")
            category_maintenance()
category_maintenance()


print("---------------------------------------------------------------------------------")


#Taking query Input from the student
print(f"Enter your query related to {department.d3}")
query = input()





















