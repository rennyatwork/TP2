# Classe qui contient les donnés et logique associés à un employé
import numbers
class Employee:
    def __init__(self, FirstName, LastName, Salary, Department):
      

        self.FirstName = FirstName
        self.LastName = LastName
        
        try:
            self.Salary = float(Salary)
        except:
            self.Salary = None

        
        self.Department = Department

        # retourne true si la string est vide
    def __IsEmptyString(self, strToCheck):
        return (strToCheck is None or strToCheck.isspace() or strToCheck.strip() =='')
        
    def IsEmployeeValid(self):
        isValid = False
        isValidFirstName = False
        isValidLastName = False
        
        ## !!! La vérification de nom et prénom vides ne sont pas dans l'enoncé
        ## mais on suppose qu'ils doivent etre renseignés
        ## En tout cas, c'est de l'apprentissage python
        if (self.__IsEmptyString(self.LastName)):
            print("Last Name cannot be empty") 
        else:
            isValidLastName = True
        
        if (self.__IsEmptyString(self.FirstName)):
            print ("First Name cannot be empty")
        else:
            isValidFirstName=True
        
        isValidSalary = False
        try:
            if(self.Salary > 0):
                isValidSalary = True
            else:
                isValidSalary = False
                print("Salary must be greater than 0")
        except:            
            isValidSalary=False
            print("Salary must be be a number greater than 0")


        isValid = isValidFirstName and isValidLastName and isValidSalary
   
        return isValid
        