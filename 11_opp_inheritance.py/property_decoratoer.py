class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

        @property
        def name(self):
            return f"{self.fname} {self.fname}"
        
        @name.setter
        def name(self,value):
            parts = value.split(" ")
            self.fname = parts[0]
            self.lname = parts[1]
        

e = Employee()
e.a = 46


e.name = "Abhishek kumar"

e.show()