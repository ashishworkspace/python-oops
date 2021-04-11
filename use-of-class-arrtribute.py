print("---------------------------\nCASE 1\n")

#case 1
class Person:
  no_of_people = 0#class attriburte because it is defined inside class and not inside any method
  def __init__(self, name):
    self.name = name
    print(f"{self.name}")
p1 = Person("harry")
p2 = Person("mosh")
print(Person.no_of_people) 
#or
print(p1.no_of_people)


print("---------------------------\nCASE 2\n")

#case 2
class Person2:
 people = 0
 def __init__(self, name):
  self.name = name
  Person2.people += 1
pi1 = Person2("harry")
print(Person2.people)
pi2 = Person2("mosh")
print(pi2.people)