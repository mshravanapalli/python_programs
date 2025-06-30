#Task 1.Create a Calculator by using function for operations
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return 'error! division by zero'
    return a/b
print('select operation:+,-,*,/')
operators=input("enter operator:")
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if operators == "+":
    print(num1+num2)
elif operators == "-":
    print(num1-num2)
elif operators == "*":
    print(num1*num2)
elif operators == "/":
    print(num1/num2)


#Task 2.Student Management System-Use keyword and default arguments to input student data.

def stu_management(name,registrationno,course,city):
    print(f"Student Name:{name}, ID:{registrationno}, Course:{course}, City:{city}")
stu_management("Vismaya",101,"EEE","Sec")
stu_management("Mishika",201,"CSe","HYD")

#Task 3.Invoice Generator — Use return functions and lambda to apply discounts and calculate totals.
def dis_calculate(total_amount):
   dis = (lambda x: x * 0.10)(total_amount)
   return dis
def generate_invoice(itemname,price,quantity):
    total = price * quantity
    discount = dis_calculate(total)
    final_amount = total - discount

    print("----- Invoice -----")
    print("Item:", itemname)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Amount:", total)
    print("Discount (10%):", discount)
    print("Amount to Pay:", final_amount)
generate_invoice("tv", 20000, 3)

#Task 4.Dynamic Greetings System — Use arbitrary arguments to greet multiple users.
def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")
greet_all("Hello", "Meena", "Vishu", "Praneeth", "Nikhil", "Sabeer")

#Task 5.Recursive Task — Write a function to compute Fibonacci numbers recursively
def fib(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 1:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Example usage
for i in range(6):
    print(f"Fib(i) = {fib(i)}")

#Task 6.Data Processor — Use *args and **kwargs to handle dynamic data fields.
def data_processor(*args, **kwargs):
    for key ,value in kwargs.items():
        print(key,value)
        print(args,kwargs)
data_processor(1,2,name="meena",email="m@gmail.com")

#Task 7.Lambda Sorting — Use lambda to sort a list of dictionaries by a specific key.

employee=[{"name":"ccccc","age":34},
          {"name":"bbbb","age":5},
          {"name":"aaaaa","age":28},
          {"name":"dddd","age":50}
          ]
employee.sort(key=lambda x:x["name"],reverse=True)
print(employee)

#Task 8.String Analyzer — Function that counts vowels, consonants, spaces, and symbols.
def analyze_string(text):
    vowels =0
    consonants =0
    spaces =0
    symbols = 0
    for ch in text:
        if ch.lower() in 'aeiou':
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isspace():
            spaces += 1
        else:
            symbols += 1
    print(f"Vowels: {vowels}, Consonants: {consonants}, Spaces: {spaces}, Symbols: {symbols}")

analyze_string("Meena shravanapalli")

#Task 9.Quiz Application — Functions to ask questions, validate answers, and keep score.
def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("correct!")
        return 1
    else:
        print("wrong!")
        return 0
def quiz():        
    score = 0
    score+= ask_question("how many days are there in july", "31")
    score += ask_question("What is the national flower of India?","Lotus")
    score+=ask_question("Which festival is known as the Festival of Lights?", "Diwali")
print(f"Your score is: ",score)
quiz()

#Task 10.Bank Transaction System — Simulate deposits and withdrawals using functions and return values.
balance = 25000
pin = "2228"
def checkPin():
    entered = input('enter your pin :')
    return entered == pin

def deposit(amount):
    if checkPin():
        global balance
        balance = balance + amount
        print('Deposited amount is :',amount)
        print('Your total balance is :',balance)
    else:
        print('You entered wrong PIN,Try again')
        
def withdraw(amount):
    if checkPin():
        global balance
        if amount <= balance:
            balance = balance - amount
            print('Withdrawn amount is :',amount)
            print('Your total balance is :', balance)
        else:
            print('Not enough balance')

    else:
         print('You entered wrong PIN,Try again')

def checkBalance():
    if checkPin():
        print('Your balance is :',balance)
    else:
        print('You entered wrong PIN,Try again')
withdraw(1000)












