from ClassLibrary.Department import Department 
from ClassLibrary.Employee import Employee




CONST_EXIT="EXIT"
CONST_SECTION_SEPARATOR="/////////////////////////////////////////////////////////////////"

CONST_ANSWER_YES="YES"
CONST_ANSWER_NO="NO"

# DEPARTMENT DATA
CONST_MSG_DEPARTMENT = "Please enter the department name or EXIT when yhou finish: "

#EMPLOYEE DATA
CONST_MSG_FIRST_NAME = "Please enter the employee first name: "
CONST_MSG_LAST_NAME = "Please enter the employee last name: "
CONST_MSG_SALARY = "Please enter the employee salary:  "
CONST_MSG_DEPT = "Please enter department Name: "

##### Department loop
newDept = None
while True:
    deptName = input(CONST_MSG_DEPARTMENT)
    
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
    empFirstName = input(CONST_MSG_FIRST_NAME)
    empLastName = input(CONST_MSG_LAST_NAME)
    empSalary = input(CONST_MSG_SALARY)
    empDept = input(CONST_MSG_DEPT)
    
    newEmpl = Employee(empFirstName, empLastName, empSalary, empDept)
    
    if (newEmpl.IsEmployeeValid()):
        Department.AddEmployee(newEmpl)

    while True:
        answer = input("Do you want to enter another employee yes/no? ")
        if answer.upper() == CONST_ANSWER_NO:
            answer_continue=False
            break
        elif answer.upper() == CONST_ANSWER_YES:            
            break
    
print(CONST_SECTION_SEPARATOR)
Department.PrintAllDepartments()  
