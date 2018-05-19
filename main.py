from ClassLibrary.Department import Department 
from ClassLibrary.Employee import Employee

depa = Department("aaa")
depa.PrintName()

empl = Employee("First", "Last", "1000", "IT")

depa.AddEmployee(empl)

x=1