class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def get_role(self):
        return "Employee"
    
class Manager(Employee):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.__bonus = bonus

    def get_role(self):
        return "Manager"
    
    def get_bonus(self):
        return self.__bonus
    
    def get_salary(self):
        return super().get_salary() + self.__bonus

def info(team):
    for i in team:
        print(f"Name: {i.name}; Role: {i.get_role()}; Salary: {i.get_salary()}")
 
sul = Manager('Suleiman', 20, 700, 200)
yel = Employee('Yelinar', 19, 500)
dim = Employee('Dinmukhamed', 21, 650)
team = [sul, yel, dim]
info(team)