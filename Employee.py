# Trisha Kabir 817173
class Employee:
    def __init__(self,Name):
        self._name = Name
    
    def getName(self):
        return self._name
    def setName(self,Name):
        self._name = Name 

    def Pay(self,HoursWorked):
        return 0
    
#HourlyEmployee
class hourlyEmployee(Employee):
    def __init__(self, Name,hourlyRate):
        super().__init__(Name)
        self._hourlyRate = hourlyRate

    def gethourlyRate(self):
        return self._hourlyRate
    def sethourlyRate(self,hourlyRate):
        self._hourlyRate = hourlyRate 

    def Pay(self,HoursWorked):
        return HoursWorked * self._hourlyRate

class salariedEmployee(Employee):
    def __init__(self, Name,annualSalary):
        super().__init__(Name)
        self._annualSalary = annualSalary

    def getannualSalary(self):
        return self._annualSalary
    def setannualSalary(self,annualSalary):
        self._annualSalary  =  annualSalary

    def Pay(self,HoursWorked):
        return self._annualSalary / 12
    
class Manager(salariedEmployee):
    def __init__(self, Name, annualSalary,Bonuspay):
        super().__init__(Name, annualSalary)
        self._bonuspay = Bonuspay

    def getbonuspay(self):
        return self._bonuspay
    def setbonuspay(self,Bonuspay):
        self._bonuspay = Bonuspay

    def Pay(self,HoursWorked):
        return super().Pay(HoursWorked) + self._bonuspay
    

#Objects of the classes 
Parentclass = Employee("Trisha")
Subclass1 = hourlyEmployee("Jane",15)
Subclass2 = salariedEmployee("Simran",15000)
Manager1 = Manager("Anne",6000,12)

#print the data 
print(Parentclass.getName(), "gets $",Parentclass.Pay(0))
print(Subclass1.getName(), "gets $",Subclass1.Pay(8000))
print(Subclass2.getName(),"gets $",Subclass2.Pay(30000))
print(Manager1.getName(), "Manager", "gets $",Manager1.Pay(20))