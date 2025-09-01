class Employee:
    language ="python"
    salary =12000000000

    def getinfo(self):
         print(f"the language is {self.language}.the salary is {self.salary}")

    def greet(self):
         print("good morning bro")


harry = Employee()
harry.language ="javascript"
# print(harry.language,harry.salary,)
harry.getinfo()
harry.greet()
