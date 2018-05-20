class Department:
    # on garde chaque departement ajouté dans la liste
    __lstNameDept = []
    
    __lstDept = []

    __dictDeptNameEmployees = {}

    # def __init__(self, Name, ListEmployee=[]):
    #     self.Name = Name.upper()
    #     self.ListEmployee = ListEmployee
        
    #     Department.__lstNameDept.append(self.Name)
        
    #     self.__lstDept=[]
    #     Department.__lstDept.append(self)
        

    #     x=1
    
    def __init__(self, Name):
        self.Name = Name.upper()
        self.ListEmployee = []
        
        Department.__lstNameDept.append(self.Name)        

        self.__lstDept=[]
        Department.__lstDept.append(self)
    
    def AddEmployee(self, employee):
        #ajoute seulement si le departement existe
        if employee.Department.upper() in Department.__lstNameDept:
            self.ListEmployee.append(employee)
        else:
            print("Error: deparment %s does not exist! ", employee.Department)
        # print("Employee: [" + employee.LastName.capitalize() +" "+ employee.FirstName+"]  added to the list" )
    
    def PrintName(self):
        print(self.Name)
    
    def CalculateAverage(self):
        print("=========ClaculateAverage=========")
        print(self.Name)
        sumSal =0
        for emp in self.ListEmployee:
            print("Name: " +emp.LastName +" "+ emp.FirstName)            
            sumSal= sumSal+emp.Salary

        # sumSal = sum(emp.Salary in self.ListEmployee)
        x=1
        # print("Sum salaries: " + sumSal)

#parcourit la liste, appele la fonction de moyenne
    def PrintAllDepartments():
        # for dept in Department.__lstDept:
        #     print(dept.Name)
        
        for name in Department.__lstNameDept:
            print(name)
        
        for dept in Department.__lstDept:
            print("-- in department loop")
            print (dept.Name)
            
            dept.CalculateAverage()