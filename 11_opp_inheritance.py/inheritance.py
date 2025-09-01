class Employee:
    company = "ITC"
    def show (self):
        print(f"the name of the Employee is {self.name}and the salary is {self.salary}")

# class programmer:
#     company = "ITC company "

#     def show (self):
#         print(f"the name of the Employee is {self.name}and the salary is {self.salary}")

class programmer(Employee):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"the name of the Employee is {self.name}and the salary is {self.salary}")

        
a = Employee()
b = programmer()

print(a.company, b.company)