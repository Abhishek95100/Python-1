class Employee:
    company = "ITC"
    name = "Default name"
    def show (self):
        print(f"the name of the Employee is {self.company}and the salary is {self.company}")
class coder:
    languages = "python"
    def pribtlanguages(self):
        print(f"out of all languages hera is your language:{self.languages}")


class programmer(Employee,coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"the name of the Employee is {self.company}and the salary is {self.company}")

        
a = Employee()
b = programmer()


b.show()
b.pribtlanguages()
b.showlanguage()

print(a.company, b.company)