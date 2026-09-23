from abc import ABC, abstractmethod
class Employee:
    @abstractmethod
    def calculate_salary():
        pass;
class Intern(Employee):
    def __init__(self,stipend):
        self.stipend=stipend
        
    def calculate_salary(self):
        return self.stipend
    
class FullTimeEmployee(Employee):
    def __init__(self,salary):
        self.salary=salary
    
    def calculate_salary(self):
        return self.salary    
        
class ContractEmployee(Employee):
    def __init__(self,rate,hour):
        self.rate=rate
        self.hour=hour
    
    def calculate_salary(self):
        return self.hour*self.rate

i=Intern(15000)
f=FullTimeEmployee(75000)
c=ContractEmployee(1000,25)

print(i.calculate_salary())
print(f.calculate_salary())
print(c.calculate_salary())
