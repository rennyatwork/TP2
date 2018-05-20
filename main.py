from ClassLibrary.Department import Department 
from ClassLibrary.Employee import Employee

lstDept = []


depMkt = Department("mkt")
depIt = Department("It")

# lstDept.append(depMkt)
# lstDept.append(depIt)


empl_it_1 = Employee("First", "aaa", 4200, "it")
empl_it_2 = Employee("First", "Last", 2700, "IT")
empl_it_3 = Employee("First", "Last Name", 3000, "iT")

empl_mkt_1 = Employee("John", "Bull",2544,"mkt")
empl_mkt_2 = Employee("Jim", "Carey",2644,"mKt")
empl_mkt_3 = Employee("Jack", "Naldson",2844,"mkT")

depIt.AddEmployee(empl_it_1)
depIt.AddEmployee(empl_it_2)
depIt.AddEmployee(empl_it_3)

depMkt.AddEmployee(empl_mkt_1)
depMkt.AddEmployee(empl_mkt_2)
depMkt.AddEmployee(empl_mkt_3)

#should not add
empl_mkt_4 = Employee("JackXXX", "Naldson","2844","xxx")
depMkt.AddEmployee(empl_mkt_4)

#instance
# depMkt.PrintAllDepartments()

#class
Department.PrintAllDepartments()


x=1