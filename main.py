from ClassLibrary.Department import Department 
from ClassLibrary.Employee import Employee




# depMkt = Department("mkt")
# depIt = Department("It")
# depEmpty = Department("NobodyWorksHere")



# empl_it_1 = Employee("First", "aaa", 4200, "it")
# empl_it_2 = Employee("First", "Last", 2700, "IT")
# empl_it_3 = Employee("First", "Last Name", 3000, "iT")

# empl_mkt_1 = Employee("John", "Bull",2544,"mkt")
# empl_mkt_2 = Employee("Jim", "Carey",2644,"mKt")
# empl_mkt_3 = Employee("Jack", "Naldson",2844,"mkT")
# empl_mkt_4 = Employee("Zz", "Jellerson",0,"mkT")

# depIt.AddEmployee(empl_it_1)
# depIt.AddEmployee(empl_it_2)
# depIt.AddEmployee(empl_it_3)

# depMkt.AddEmployee(empl_mkt_1)
# depMkt.AddEmployee(empl_mkt_2)
# depMkt.AddEmployee(empl_mkt_3)

# #should not add
# empl_xxx_1 = Employee("JackXXX", "Naldson",2844,"xxx")
# depMkt.AddEmployee(empl_mkt_4)

#instance
# depMkt.PrintAllDepartments()

#class
# Department.PrintAllDepartments()

##########


CONST_EXIT="EXIT"
CONST_SECTION_SEPARATOR="/////////////////////////////////////////////////////////////////"

CONST_ANSWER_YES="YES"
CONST_ANSWER_NO="NO"


##### Department loop
newDept = None
while True:
    deptName = input("Please enter the department name or EXIT when yhou finish: ")
    #print("You typed: " + deptName)
    if deptName.upper() == CONST_EXIT:
        break
    
    newDept = Department(deptName)
    
#Department.PrintAllDepartments()
print(CONST_SECTION_SEPARATOR)


#########Employee section
newEmpl = None
answer_continue=True
##### Employee Loop
while answer_continue:
    empFirstName = input("Please enter the employee first name: ")
    empLastName = input("Please enter the employee last name: ")
    empSalary = float(input("Please enter the employee salary:  "))
    empDept = input("Please enter department Name: ")
    
    newEmpl = Employee(empFirstName, empLastName, empSalary, empDept)
    if (not newEmpl == None ):
        Department.AddEmployee(newEmpl)

    while True:
        answer = input("Do you want to enter another employee yes/no? ")
        if answer.upper() == CONST_ANSWER_NO:
            answer_continue=False
            break
        elif answer.upper() == CONST_ANSWER_YES:            
            break
    
Department.PrintAllDepartments()  
    
x=1