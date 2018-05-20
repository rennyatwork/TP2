class Department:
    # on garde chaque departement ajouté dans la liste
    __lstNameDept = []
    
    __lstDept = []

    __dictDeptNameEmployees = {}

    CONST_NOT_AVAILABLE="Not Available"

    def __init__(self, Name):
        if(Name is None or Name.isspace() or Name.strip() ==''):
            print("Le nom ne peut pas être vide")
            return
        self.Name = Name.upper()
        self.ListEmployee = []
        
        #if department already exists, leave
        if (len([x for x in Department.__lstDept if x.Name.upper() == self.Name]) >0):
            return

        Department.__lstNameDept.append(self.Name)        

        self.__lstDept=[]
        Department.__lstDept.append(self)

        Department.__dictDeptNameEmployees.update({self.Name: self})
    
    # def AddEmployee(self, employee):
    #     #ajoute seulement si le departement existe
    #     if employee.Department.upper() in Department.__lstNameDept:
    #         self.ListEmployee.append(employee)
    #     else:
    #         print("Error: deparment %s does not exist! ", employee.Department)
    #     # print("Employee: [" + employee.LastName.capitalize() +" "+ employee.FirstName+"]  added to the list" )
    

    #static AddEmployee
    def AddEmployee(employee):
        if employee.Department.upper() in Department.__dictDeptNameEmployees:
            dept = Department.__dictDeptNameEmployees[employee.Department.upper()]
            dept.ListEmployee.append(employee)

        else:
            print("Error: deparment "+employee.Department+" does not exist! " )

    def PrintName(self):
        print(self.Name)
    
    def CalculateAverage(self):
        
        # print("=========ClaculateAverage=========")
        # print(self.Name)
        
        if (len(self.ListEmployee) ==0):
            return Department.CONST_NOT_AVAILABLE
        
        sumSal = sum(emp.Salary for emp in self.ListEmployee)
        return sumSal/len(self.ListEmployee)

       

    def CalculateMax(self):
        if (len(self.ListEmployee)==0):
            return Department.CONST_NOT_AVAILABLE
        return max(x.Salary for x in self.ListEmployee)
    
    def CalculateMin(self):
        if (len(self.ListEmployee)==0):
            return Department.CONST_NOT_AVAILABLE
        return min(x.Salary for x in self.ListEmployee)

#parcourit la liste, appele la fonction de moyenne
    def PrintAllDepartments():
       
        # for name in Department.__lstNameDept:
        #     print(name)
        
        for dept in Department.__lstDept:
            # print("-- in department loop")
            # print (dept.Name)
            
          avgSal =  dept.CalculateAverage()
          print("Average salary for " + dept.Name.upper() + " is: " + str(avgSal))

          maxSal = dept.CalculateMax()
          print("Max salary for " + dept.Name.upper() + " is: " + str(maxSal))

          minSal = dept.CalculateMin()
          print("Min salary for " + dept.Name.upper() + " is: " + str(minSal))

          print("\r\n")