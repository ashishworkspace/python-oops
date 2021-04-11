#Inheritance
class Pet:
  def __init__(self, name, age):
    self.name = name
    self.age = age 
  def get_output(self):
    print(f"My name is {self.name}. My age is {self.age}")
  def sound(self):
    print("I don't know how to speak")
class Dog(Pet):
  def sound(self):
   print("Bark")
class Cat(Pet):
  def sound(self):
   print("Meow")
class Fish(Pet):
  pass
class Bird(Pet):
  def __init__(self, name, age, color):
   super().__init__(name, age)
   self.color = color 
  def get_output(self):
   print(f"My name is {self.name}. My age is {self.age}.My color is {self.color}")


obj1 = Fish("Bubble" , 2)
obj2 = Dog("Tommy" , 11)
obj3 = Cat("Kitti" , 23)
obj4 = Bird("titu", 5, "green")
obj4.get_output()
obj1.sound()
obj3.get_output()
