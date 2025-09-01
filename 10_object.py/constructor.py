class Employee:
    language ="python"
    salary =12000000000
    def __init__(self): #dunder method which is automatically called
        # self.name = harry
        # self.salary =1233
        
        print("i am creating an object")

    def getinfo(self):
         print(f"the language is {self.language}.the salary is {self.salary}")

    def greet(self):
         print("good morning bro")


harry = Employee("harry",13000000,"javascript")
harry.name ="Harry"
print(harry.name,harry.salary)

