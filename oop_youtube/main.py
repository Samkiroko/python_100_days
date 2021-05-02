# position, name, age, level, salary

se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 5000]


def code(se):
    print(f"{se[1]} is writting code ...")


class SoftwareEngineer:

    # class attribute
    alias = "keyboard magician"

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writting code ...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # def information(self):
    #     information = f"name = {self.name}, age = {self.age}, level = {self.level}"
    #     return information

    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self,  other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


se1 = SoftwareEngineer("Sam", 20, "Junior", 5000)
se3 = SoftwareEngineer("Sam", 20, "Junior", 5000)
se2 = SoftwareEngineer("lisa", 25, "Senior", 7000)

se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("C++")
# print(se1.information())
print(se2)
print(se1 == se3)

print(se1.entry_salary(24))
