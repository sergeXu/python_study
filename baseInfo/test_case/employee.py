class Employee:
    def __init__(self, name:str,gender:str,salary:int):
        self.name = name
        self.gender = gender
        self.salary = salary

    def give_raise(self, bonus:int = 5000):
        self.salary = self.salary + bonus