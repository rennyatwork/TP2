class Employee:
    def __init__(self, FirstName, LastName, Salary, Department):
        if (Salary <=0):
            print("Le salaire doit être positif")
            return
        self.FirstName = FirstName
        self.LastName = LastName
        self.Salary = float(Salary)
        self.Department = Department        