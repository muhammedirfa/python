# class student:
#     def __init__(self,name,age,subject,place):
#         self.name=name
#         self.age=age
#         self.subject=subject
#         self.place=place
#     def display_info(self):
#         print(f"student:{self.name}{self.age}{self.subject}{self.place}")

# student=student("irfan",21,"dataanaltics","pattambi")
# student.display_info()


# class employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary
#     def display_info(self):
#         print(f"employee:{self.name}{self.__salary}")
#     def add_money(self, new_amount):
#         self.__salary += new_amount

# emp = employee("shadil",200000)
# emp.display_info()

# emp.add_money(10000)
# emp.display_info()


# class Dog:
#     def speak(self):
#         print("Dog : shadil,shadi")

# dog1 = Dog()
# dog1.speak()


# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     pass

# dog = Dog()
# dog.speak()



# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     pass

# dog = Dog()
# dog.speak()


# class Dog:
#     def speak(self):
#         print("Woof")

# class Cat:
#     def speak(self):
#         print("Meow")

# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()

#Abstractmethod

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self,height = height

#     def area(self):
#         print(self.width * self.height)

# r = Rectangle(10,5)
# r.area()


# from abc import ABC, abstractmethod

# class shape(ABC):
    # @abstractmethod
    # def area(self):
    #     pass

#  class rectangle(shape):
#      def _init_(self,width,height):
#          self.width=width
#          self.height=height
# class circle(shape):
#     def __init__(self,radius):
#         self.r=radius
    

#     def area(self):
#         return 3.14 * self.r * self.r

# c=circle(5)
# print(c.area())








