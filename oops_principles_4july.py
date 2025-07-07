# Task 1.Design a class hierarchy for a Library System.
#Base class: Item (with title, author, ID)
#Subclasses: Book, Magazine, DVD
#Implement methods like check_out() and return_item()
#Use inheritance and polymorphism.
class Item:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.available = True

    def check_out(self):
        if self.available:
            self.available = False

            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is currently not available.")

    def return_item(self):
        self.available = True
        print(f"{self.title} has been returned.")

class Book(Item):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def check_out(self):
        print("Checking out a book...")
        super().check_out()

class Magazine(Item):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.issue_number = issue_number

    def check_out(self):
        print("Checking out a magazine...")
        super().check_out()
class DVD(Item):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.duration = duration

    def check_out(self):
        print("Checking out a DVD...")
        super().check_out()

library_items = [
    Book("1984", "George Orwell", "B001", "Dystopian"),
    Magazine("National Geographic", "Various", "M101", "July 2025"),
    DVD("Inception", "Christopher Nolan", "D202", "2h 28m")
]

for item in library_items:
    item.check_out()

print()

for item in library_items:
    item.return_item()
    print("------------------------")

# Task 2.Create a Billing System for an Online Store.
# Class Product: name, price
# Class Cart: list of products, add/remove item, calculate total
# Apply encapsulation for price calculation logic.

# Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  # Encapsulated

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.name} - {self.__price}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added: {product}")

    def remove_item(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print(f"{product_name} not found in cart.")

    def calculate_total(self):
        total = sum(item.get_price() for item in self.items)
        return total

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Cart items:")
            for item in self.items:
                print(f" {item}")
            print(f"Total: {self.calculate_total()}")
# Create products
p1 = Product("Laptop", 23000)
p2 = Product("Mouse", 700)
p3 = Product("Keyboard", 1200)

# Create cart and add items
cart = Cart()
cart.add_item(p1)
cart.add_item(p2)
cart.add_item(p3)

# Show cart and total
cart.show_cart()

# Remove an item
cart.remove_item("Mouse")
cart.show_cart()
print("-------------------")

# Task 3.Build a Vehicle Inheritance Model.
# Base class: Vehicle
# Subclasses: Car, Bike, Truck
# Each subclass should override a method move() with its own behavior.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print(f"{self.brand} vehicle is moving.")
class Car(Vehicle):
    def move(self):
        print(f"{self.brand} car is driving .")
class Bike(Vehicle):
    def move(self):
        print(f"{self.brand} bike on traffic.")
class Truck(Vehicle):
    def move(self):
        print(f"{self.brand} driving the truck.")
vehicles = [ Car("Toyota"), Bike("Yamaha"), Truck("Volvo")]

for v in vehicles:
    v.move()
print("----------------")

# Task 4.Implement a simple ATM System using OOP.
# Class: Account (balance, pin)
# Methods: check_balance(), withdraw(), deposit()
# Use encapsulation to protect sensitive data.

class Account:
    def __init__(self, pin, balance=0):
        self.__pin = pin          # Encapsulated
        self.__balance = balance  # Encapsulated

    def __verify_pin(self, input_pin):
        return self.__pin == input_pin

    def check_balance(self, input_pin):
        if self.__verify_pin(input_pin):
            print(f"Your balance is ₹{self.__balance}")
        else:
            print("Incorrect PIN.")

    def deposit(self, amount, input_pin):
        if self.__verify_pin(input_pin):
            if amount > 0:
                self.__balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Incorrect PIN.")

    def withdraw(self, amount, input_pin):
        if self.__verify_pin(input_pin):
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Incorrect PIN.")

my_account = Account(pin=1234, balance=5000)
my_account.check_balance(1234)
my_account.deposit(1000, 1234)
my_account.withdraw(2000, 1234)
my_account.check_balance(1234)
print("--------------------------")

#5. Design a Student Management System.
#Class Person with attributes: name, age
#Class Student inherits from Person and adds: student_id, courses
#Add method to display full student details using abstraction.

def abstractmethod(args):
    pass


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display(self):
     pass

class Student(Person):
    def __init__(self, name, age,student_id=None,course=None):
        super().__init__(name,age)
        self.student_id = student_id
        self.courses = course

    def display_details(self):
        print(f"Name: {self.name}")
        print(f" Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Courses: {self.courses}")

if __name__ == "__main__":
    student1=Student("vismaya",18,3131,"cse")
    student1.display_details()
    student2 = Student("mishika", 20, 2323, "eee")
    student2.display_details()
    student3 = Student("virah", 19, 3232, "ece")
    student3.display_details()
    print("---------------------------")

#6. Create an Animal Sound Simulation.
#Use polymorphism: each animal class (Dog, Cat, Cow) should implement make_sound()
#Write a function play_sound(animal) that works for all.
from abc import abstractmethod

class Animal:
    def make_sound(self):
        raise NotImplementedError

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Cow(Animal):
    def make_sound(self):
        return "Moo"

# Polymorphic function
def play_sound(animal: Animal):
    print(animal.make_sound())

if __name__ == "__main__":
    animals = [Dog(), Cat(), Cow()]
    for animal in animals:
        play_sound(animal)
    print("-------------------------------")

#Task 7. Build a Company Employee Hierarchy.
#Class Employee with salary, name
#Subclasses: Manager, Developer, Intern
#Add bonus logic using method overriding.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.03

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary}")
        print(f"Employee Bonus: {self.calculate_bonus()}")

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.30

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

class Intern(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05

emp1 = Manager("Meena", 50000)
emp2 = Developer("vishu", 40000)
emp3 = Intern("vismaya", 20000)

employees = [emp1, emp2, emp3]
for employee in employees:
    employee.display_info()

print('..........................................')

#Task 8.Develop a Movie Ticket Booking System.
#Class Movie (name, seats, time)
#Class Ticket to book or cancel tickets
#Use encapsulation for seat management and price.

class Movie:
    def __init__(self, name, time, seats, price):
        self.name = name
        self.time = time
        self.__seats = seats
        self.__price = price

    def get_details(self):
        print(f"Movie Name: {self.name}")
        print(f"Movie Time: {self.time}")
        print(f"Available Seats: {self.__seats}")
        print(f"Ticket Price: {self.__price}")

    def get_available_seats(self):
        return self.__seats

    def get_price(self):
        return self.__price

    def _reduce_seats(self,quantity):
        if quantity <= self.__seats:
            self.__seats -= quantity
            return True
        return False

    def _increase_seats(self,quantity):
        self.__seats += quantity

class Ticket:
    def book_ticket(self, movie, quantity):
        if movie._reduce_seats(quantity):
            total = quantity * movie.get_price()
            print(f"Booked:{quantity} tickets for {movie.name} at {total}")
        else:
            print(f"Not enough seats for {movie.name}.Only {movie.get_available_seats()} available.")

    def cancel_ticket(self, movie, quantity):
        movie._increase_seats(quantity)
        refund = quantity * movie.get_price()
        print(f"Cancelled {quantity} tickets for {movie.name} refund amount {refund}")

m1 = Movie("Coolie", "11:00 AM", 100, 250)

m1.get_details()
t = Ticket()
t.book_ticket(m1, 5)
t.cancel_ticket(m1, 1)
m1.get_details()
print("-----------------------------")

#9. Create a Shape Drawing App using Abstraction.
#Abstract class: Shape
#Subclasses: Circle, Rectangle, Triangle with method draw()
#Call them in a loop to simulate drawing.

# Abstract class
class Shape():
    @abstractmethod
    def draw(self):
        pass

# Subclass: Circle
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

# Subclass: Rectangle
class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

# Subclass: Triangle
class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")


shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.draw()
print("------------------")


#10. Design a Food Delivery App Backend Classes.
#Class Restaurant with menu
#Class Order with cart, delivery address
#Use multiple inheritance for Customer and DeliveryAgent

class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu  # menu is a dictionary {item_name: price}

    def show_menu(self):
        return self.menu

# Order class with cart and delivery address
class Order:
    def __init__(self, customer, restaurant, delivery_address):
        self.customer = customer
        self.restaurant = restaurant
        self.delivery_address = delivery_address
        self.cart = []

    def add_to_cart(self, item):
        if item in self.restaurant.menu:
            self.cart.append(item)
        else:
            print(f"{item} is not available in the menu.")

    def get_total(self):
        return sum(self.restaurant.menu[item] for item in self.cart)

# Customer class using multiple inheritance
class Customer(Person, Order):
    def __init__(self, name, phone, restaurant, delivery_address):
        Person.__init__(self, name, phone)
        Order.__init__(self, self, restaurant, delivery_address)

# DeliveryAgent class using multiple inheritance
class DeliveryAgent(Person):
    def __init__(self, name, phone, agent_id):
        super().__init__(name, phone)
        self.agent_id = agent_id

    def deliver_order(self, order):
        print(f"Delivering order to {order.delivery_address}")

menu = {'Pizza': 250, 'Burger': 150, 'Pasta': 200}
restaurant = Restaurant("sitara", menu)
customer = Customer("Vishwanath", "9876543210", restaurant, "Lb.nagar")

customer.add_to_cart('Pizza')
customer.add_to_cart('Burger')
print("Total:", customer.get_total())

agent = DeliveryAgent("Rahul", "9123456780", "AG123")
agent.deliver_order(customer)
