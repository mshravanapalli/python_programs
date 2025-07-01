#1. User Input Validation System:
'''(Build a script that takes user inputs (name, age, email).
Handle empty input
Raise ValueError for invalid age (<0)
Raise custom exception for invalid email (no ‘@’))'''
import sys
from fileinput import close


def user():
    try:
        name = input("Enter your name: ")
        age =  input("Enter your age: ")
        email = input("Enter your email: ")

        if name == "" or age == "" or email == "":
            raise ValueError("enter name cannot be empty")
        age = int(input(age))

        if age<0:
           raise ValueError("age must be between 0 and 100")

        if '@' not in email:
            raise ValueError("Invalid email",'<EMAIL>@')
        print("Your name is :",name)
        print("Your age is :",age)
        print("Your email is :",email)
    except ValueError as e:
        print(e)
    else:
        print("success")
    finally:
        print("data inserted")
user()

# 2.2. File Reader Tool
# Build a function that opens a file and reads its content.
# — Handle FileNotFoundError if the file doesn’t exist
# — Handle PermissionError for restricted files
# — Use finally to always close the file

def file_read():
    try:
        file=open("textfile.txt",'r')
        data=file.read()
        print(f"Error: The file was not found.")
    except FileNotFoundError:
        print("file not exists")

    except PermissionError:
        print(f"Error: You do not have permission to read.")
    finally:
        print("file closed")

file_read()

# 3. Safe Division Function

'''(Write a safe_divide(a, b) function that:
— Catches ZeroDivisionError
— Catches TypeError if a or b are not numbers
— Logs errors and returns meaningful messages'''

def safe_divide():
    try:
        a=int(input("enter first number: "))
        b=int(input("enter second number: "))
        result = a/b
    except ZeroDivisionError :
        print("Error: division by zero")
    except ValueError:
        print("Error: valid a number")
    else:
        print(result)
    finally:
        print("execution completed")
safe_divide()

# 4. API Request Handler (Mock Project):
# Simulate an API call using a function.
# — Raise exception for invalid endpoint
# — Handle timeout with a custom TimeoutError
# — Use try-except-finally to manage connection lifecycle

def api_call():
    try:
        endpoint = input("Enter the api endpoint: ")
        endpoint = endpoint.rstrip('/menu')
        print("Connecting to API")
        if endpoint not in endpoint:
            raise ValueError("Invalid endpoint.")
        raise TimeoutError("Request timed out.")
    except ValueError as ve:
        print("Error:",ve)
    except TimeoutError as te:
        print("Error:", te)
    finally:
        print("closing connection.")

api_call()

#5. Dictionary Data Fetcher:
#Fetch a value from a dictionary by key.
#— Handle KeyError and return a default message
#— Log access errors for missing keys
#— Raise exception if dictionary is empty

def data_fetcher():
    try:
        data={"id":111,"name":'vishu'}
        key=input("Enter key to fetch (id or name):")
        if not data:
          raise ValueError("dictionary is empty")
        print("value",data[key])
    except KeyError:
         print("key not found")
    finally:
        print("finished fetching")
data_fetcher()

#6. Student Grade Calculator:
#Read marks from user, compute grade.
# Handle non-integer input (ValueError)
# Handle marks outside valid range (0–100)
#Raise custom exceptions for invalid scores

class InvalidScoreError(Exception):
    pass

def stu_grade_calculator():
    try:
        marks=float(input("enter marks(0-100): "))
        marks=int(marks)
        if marks < 0 or marks > 100:
            raise ValueError("marks must be between 0 and 100")
        if marks > 90:
            grade='A'
        elif marks > 80:
            grade='B'
        elif marks > 70:
            grade='C'
        elif marks > 60:
            grade='D'
        else:
            grade='F'
            print(f"Grade: {grade}")

    except ValueError:
         print("enter valid number")
    except InvalidScoreError as e:
         print("score error:",e)
    finally:
         print("finished calculating")

stu_grade_calculator()

# 7.File Upload Validator:
# Validate file format and size.
# — Raise ValueError for unsupported formats (e.g., .exe)
# — Raise custom FileTooLargeException if size > 5MB
# — Catch both and return meaningful feedback
class FileTooLargeException(Exception):
    pass
def upload_validator():
    try:
        filename = input("Enter file name: ")
        size_mb = float(input("Enter file size in MB: "))
        size_bytes = size_mb * 1024 * 1024  # Convert MB to bytes

        if filename.endswith(".exe"):
            raise ValueError("Execute (.exe) files are not allowed.")
        if size_bytes > 5 * 1024 * 1024:
            raise FileTooLargeException(f"File size exceeds 5MB limit.")

        print("File is valid and accepted.")
    except ValueError as ve:
        print("Format Error:", ve)
    except FileTooLargeException as fe:
        print("Size Error:", fe)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("File validation process completed.")

upload_validator()

# 8.Database Connection Simulator
# Simulate a DB connection (no real DB needed).
# — If credentials are wrong, raise PermissionError
# — If DB not found, raise ConnectionError
# — Use finally block to ‘close’ the connection

def database_connection():
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("connecting")
        if username != "admin" and password != "password2228":
          raise PermissionError("please enter correct username and password")
        raise ConnectionError("connection failed")
    except PermissionError as pe:
       print("Error:", pe)
    except ConnectionError as ce:
       print("Error:", ce)
    finally:
       print(" connection closed.")

database_connection()

# 9. E-Commerce Cart Price Calculator
# Calculate total from cart list (item name, price, quantity).
# — Handle missing price or quantity with KeyError
# — Handle type errors (e.g., string instead of int)
# — Use try-except to process the cart smoothly

def cart_price_cal():
    try:
        cart = []
        x = int(input("Enter number of items: "))
        for i in range(x):
            name = input(f"Item {i + 1} name: ")
            price = float(input(f"Item {i + 1} price: "))
            quantity = int(input(f"Item {i + 1} quantity: "))
            cart.append({"name": name, "price": price, "quantity": quantity})

        total = 0
        for item in cart:
            total += item["price"] * item["quantity"]
        print("Total Cart Price:", total)
    except KeyError as ke:
        print("Missing data:", ke)
    except ValueError:
        print("Invalid number entered.")
    finally:
        print("Cart calculation complete.\n")

cart_price_cal()

# 10. Exception Logger Utility:
# Create a utility function log_exception(e) that:
# — Accepts an exception object
# — Logs error type, message, and timestamp to a file
# — Can be reused in any except block

import datetime

def log_exception(e):
    try:
        with open("log.txt", "a") as file:
            time = datetime.datetime.now()
            file.write(f"{time} - {type(e).__name__}: {e}\n")
    except Exception as err:
        print("Logging failed:",err)
    finally:
        print("Exception logging finished.\n")

# Example usage:
    try:
     number = int(input("Enter a number to divide 100 by: "))
     result = 100 / number
     print("Result:", result)
    except Exception as e:
       print("An error occurred:", e)
log_exception(e)




