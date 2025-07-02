# Task 1. Write a Python class named Employee with instance variables name and salary.
#Add a constructor to initialize them and a method display() to print details.

class Employee:
    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee Name:", {self.name}, {self.salary})
# Example usage:
if __name__ == "__main__":
    employee1 = Employee("vishu", 63000)
    employee2 = Employee("vismaya", 75000)

    print("Employee Details:")
    employee1.display()
    employee2.display()

# Task 2. What will be the output of the following code?

class Test:
  def __init__(self, x):
   self.x = x
   a = Test(10)
   b = Test(20)
   print(a.x)
   print(b.x)

# Task 3. Explain the role of self in a Python class. Can a method work without it? Give an example.

class Number:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)
obj1 = Number(10)
obj1.print_value()

# Task 4. Write a class Circle with a class variable pi = 3.14 and an
# instance variable radius. Add a method to calculate area.

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):

        return self.pi* self.radius**2

obj_circle = Circle(5)
circle_area = obj_circle.area()
print(f"The circle is: {circle_area}")

# Task 5. Differentiate between instance method,
# class method, and static method. Create a class that uses all three.

class Student:

     student ="Vismaya"

     def __init__(self, Id, age):

         self.Id = Id
         self.age = age

     def display(self):
         print(f"Student Id: {self.Id}, Age: {self.age}")

     @classmethod
     def change_student(cls,new_name):
          cls.student = new_name

     @staticmethod

     def static_method():
          print("This is the a Static Method")

Student.change_student(Student("34", 12))
stu1 = Student("34", 12)

Student.static_method()
stu1.static_method()

# Task 6. What is the output of the following code?

x = 5
def outer():
 x=10
def inner():
    x=15

    print("Inner:",x)
    inner()
    print("Outer:",x)
    outer()
    print("Global:",x)
print("Inner:",x)
print("Outer:",x)
print("Global:",x)


# Task 7. What will the output be? Explain why.
    x=100
      def modify():
       global x
        x=x+50
       modify()
    print(x)


# Task 8. Create a nested function where a variable in the outer
#function is modified by the inner function using nonlocal.

def outer():

     name =("vishu")

     def inner():
         nonlocal name
         name = "Meena"
         print(name)

     inner()
     print(name)
     outer()

#Task 9. What does the dir(__builtins__) function return?

# Task 10.10. Identify the scope of each x in the following code and explain the output.

x="global"
def fun1():
     x="enclosing"
def fun2():
     x="local"
     print("fun2:",x)
     fun2()
     print("fun2:",x)
     fun1()
     print("global:",x)


