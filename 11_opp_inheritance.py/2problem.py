# Create a class 'pets' from a class 'Animals' and further create class 'Dog' from 'pets'.Add method 'bark' to class 'Dog'.


class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):
    @staticmethod

    def bark():
      print("Bow Bow!")


d = Dog()

d.bark()
