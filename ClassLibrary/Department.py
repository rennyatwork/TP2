class Department:
    def __init__(self, Name, ListEmployee=[]):
        self.Name = Name
        self.ListEmployee = ListEmployee
    def AddEmployee(self, employee):        
        self.ListEmployee.append(employee)
        # print("Employee: [" + employee.LastName.capitalize() +" "+ employee.FirstName+"]  added to the list" )
    def PrintName(self):
        print(self.Name)