from ClassLibrary.Department import Department 
from ClassLibrary.Employee import Employee

depa = Department("aaa")
depa.PrintName()

depIt = Department("It")

empl1 = Employee("First", "aaa", "10", "aAa")
empl2 = Employee("First", "Last", "1000", "IT")
empl3 = Employee("Fulano", "bla bla","2344","xyz")

depa.AddEmployee(empl1)
depa.AddEmployee(empl2)
depa.AddEmployee(empl3)

x=1