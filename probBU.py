from datetime import datetime
print("Hello World")

print('''Welcome to ProbBU,
         For the Bennettians,
         By the Bennettians,
         A Platform for all your University related problems.''')

# Taking Input Student Info
student = ""
room = ""
name = input("Name: \n")
year = input("Year of Study: \n")
course = input("Course Name: \n")
enroll_no = input("Enrollment Number: \n")

# Student is Day Scholar or Hosteller
print('''Enter "H" for Hosteller and "D" for Day Scholar''')
def hosteller_or_day_scholar():
    global student
    student = input()
    if student == "H" or student == "h":
        print("Room Number: ")
        room=input()
    elif student == "D" or student =="d":
        pass
    else:
        print("Enter a valid option.")
        print('''Enter "H" for Hosteller and "D" for Day Scholar''')
        hosteller_or_day_scholar()
hosteller_or_day_scholar()
phone_no = input("Phone Number: \n")


print("---------------------------------------------------------------------------------")


#For Departments
d1 = "IT Department"
d2 = "Finance Department"
d3 = "Maintenance Department"

#if Maintenance Department then following sub departments

sub_d1 = "Furniture"
sub_d2 = "Electrical"
sub_d3 = "Cleaning"


# Asking the department of Query
department_of_query = ""
print("What Department do you want to raise your query in?")
def enter_department():
    global department_of_query
    if student == "H" or student == "h":
        print('''"1" for "IT Department"
"2" for "Finance Department"
"3" for "Maintenance Department"''')
        department_of_query=input()
        if department_of_query == "1":
            return d1
        elif department_of_query == "2":
            return d2
        elif department_of_query == "3":
            return d3
        else:
            print("Please select a valid query department.")
            enter_department()
    else:
        print('''"1" for "IT Department"
"2" for "Finance Department"''')
        department_of_query = input()
        if department_of_query == "1":
            return d1
        elif department_of_query == "2":
            return d2
        else:
            print("Please select a valid query department.")
            enter_department()
print(enter_department())


print("---------------------------------------------------------------------------------")


# Asking for category if the selected department is Maintenance when the student is Hosteller

def category_maintenance():
    if department_of_query == "3":
        print("Under what category of Maintenance do you have your query?")
        print('''"1" for "Furniture"
"2" for "Electrical"
"3" for "Cleaning"''')
        global category_of_maintenance_var
        category_of_maintenance_var = input()
        if category_of_maintenance_var == "1":
            return sub_d1
        elif category_of_maintenance_var == "2":
            return sub_d2
        elif category_of_maintenance_var == "3":
            return sub_d3
        else:
            print("Please select a valid category.")
            category_maintenance()
if department_of_query == "3":
    print(category_maintenance())
    print("---------------------------------------------------------------------------------")
else:
    pass


# Taking query Input from the student
print(f"Enter your query :")
query = input()


now = datetime.now()
today_date=datetime.date(datetime.now()) #Current Date
current_time = now.strftime("%H:%M:%S") #Current Time


# Date and Time of Query
present_date = today_date
present_time = current_time
print("                                 ",present_date)
print("                                 ",present_time)

print("---------------------------------------------------------------------------------")


























