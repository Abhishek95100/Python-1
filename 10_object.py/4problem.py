#Add a static method in problem 2 to greet the user with hello

class calculator:
    def __init__(self,n):
        self.n =n

    def square(self):
        print(f"the square is: {self.n*self.n}")

    def cube(self):
        print(f"the cube is :{self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the square root is :{self.n**1/2}")
   
    @staticmethod
    def hello():
     print("hello there!")

a =calculator(16)
a . hello()
a.square()  
a.cube()
a.squareroot()   