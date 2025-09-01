# create a class with a class Attribute a; create an object from it and set 'a' directly using objecct.a =0.Does this change the class Attribute?

class attribute:
  a=4

o =attribute()
print(o.a)
o.a =0
print(o.a)
print(attribute.a)
      