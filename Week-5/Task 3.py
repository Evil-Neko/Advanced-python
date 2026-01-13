class Person:
    def __init__(self, name, age, fear):
        self.name = name
        self.age = age
        self.__fear = fear
    
    def info(self):
        print(f"Name: {self.name}\n Age: {self.age}")

    def greeting(self):
        print(f"Welcome, {self.name}!")

class Student(Person):
    def greeting(self):
        print(f"Welcome to the university, {self.name}!")

    def grade_sum(self, a=0, b=0, bonus=0):
        res = a + b
        if bonus:
            res += bonus
        return res

me = Student("Suleiman", 20, "Spiders")
wd = Person("Gaster", 66, "Green")
me.info()
me.greeting()
wd.greeting()
print(me.grade_sum(4, 3))
print(me.grade_sum(3, 4, 1))
print(wd.__fear)