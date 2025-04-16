class Employee:
#creating get and set for name.
    def __init__(self,name: str):
        self._name = name 

    def getname(self):
        return self._name
    
    def setname(self,newname:str):
        self._name = newname
#creating the pay method to be got and set.

    def pay(self,hoursworked):
        return 0
    
    def __str__(self):
        return "Employee " + self._name

    
#creating other classes that will inherit from Employee.
class HourlyEmployee(Employee):

    def __init__(self, name: str, hourlyrate:int):
        super().__init__(name)
        self._hourlyrate = hourlyrate

    def gethourlyrate(self):
        return self._hourlyrate

    def sethourlyrate(self,hourlyrate:int):
        self._hourlyrate = hourlyrate

    def pay(self,hoursworked:int):
        return hoursworked * self._hourlyrate


class SalariedEmployee(Employee):

    def __init__(self, name:str,annualsalary:int):
        super().__init__(name)
        self._annualsalary = annualsalary

    def getannualsalary(self):
        return self._annualsalary
    
    def setannualsalary(self,annualsalary:int):
        self._annualsalary = annualsalary

    def pay(self, hoursworked:int):
        return self._annualsalary / 12
    

class Manager(SalariedEmployee):
    
    def __init__(self, name:str, annualsalary:int , bonus:int):
        super().__init__(name, annualsalary)
        self._bonus = bonus

    def get_bonus(self):
        return self._bonus
    
    def set_bonus(self,bonus):
        self._bonus = bonus

    def pay(self, hoursworked: int):
        return super().pay(hoursworked) + self._bonus
    
    def __str__(self):
        return "Manager " + self._name


#creation of objects from all the classes.
obj1 = Employee("John")
obj2 = HourlyEmployee("Rebbeca",1.5)
obj3 = SalariedEmployee("Jo",12000)
obj4 = Manager("Jenne",15,100)

print(obj1, "is paid", obj1.pay(6000))
print(obj2, "is paid", obj2.pay(6500))
print(obj3, "is paid", obj3.pay(500))
print(obj4, "is paid", obj4.pay(90000))

