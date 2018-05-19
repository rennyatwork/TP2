class Department:
    # on garde chaque departement ajouté dans la liste
    __lstNameDept = []
    
    def __init__(self, Name, ListEmployee=[]):
        self.Name = Name.upper()
        self.ListEmployee = ListEmployee
        self.__lstNameDept.append(self.Name)
    
    def AddEmployee(self, employee):
        #ajoute seulement si le departement existe
        if employee.Department.upper() in self.__lstNameDept:
            self.ListEmployee.append(employee)
        else:
            print("Error: deparment %s does not exist! ", employee.Department)
        # print("Employee: [" + employee.LastName.capitalize() +" "+ employee.FirstName+"]  added to the list" )
    
    def PrintName(self):
        print(self.Name)