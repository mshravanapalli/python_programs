import calc
print(calc.add(22,12))
print(calc.sub(10,2))
print(calc.mul(10,2))
print(calc.div(100,20))

import geometry
print(geometry.perimeter_rectangle(21,32))
print(geometry.perimeter_circle(2*3.14))
print(geometry.area_rectangle(22,12))
print(geometry.area_circle(2*3.14))


# Task 3.Use Built-in Modules
#Use the following modules:
#math – to find square roots and factorials.
#random – to generate random passwords.
#datetime – to calculate age from date of birth.

import math
print(math.sqrt(8))
import math
print(math.factorial(5))

#random – to generate random passwords.

import random
import string

length = int(input("enter the length of password:"))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
numbers=string.digits
symbols=string.punctuation

all = lower + upper + numbers + symbols

temp =random.sample(all,length)
password="".join(temp)
print(password)

#datetime – to calculate age from date of birth.

import _datetime

date_of_birth=int(input("enter the date of birth:"))
today_date= _datetime.date.today().strftime("%Y")
print("your currect age is:",int(today_date)-date_of_birth)

#Task 4: Directory Analyzer
#Use the os module to:
#List all files in a directory
#Count how many .py files are present
#Create a new folder named backup

#Use the os module to:
import os
DIR = "C:/Users/meena"
filenames=os.listdir(DIR)
for filename in filenames:
   file_path = os.path.join(DIR,filename)
   print("file",file_path)

#List all files in a directory
import os
dir="C:/Users/meena"
for li in os.listdir(dir):
    if li.endswith("meena.txt"):
        print(li)

# Count how many .py files are present

import os

def count_py_files(directory_path):

    count = 0
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".py") and os.path.isfile(os.path.join(directory_path, filename)):
                count += 1
    except FileNotFoundError:
        print(f"Error: Directory not found at '{directory_path}'")
        return -1  # Indicate an error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return -1
    return count


directory_to_check = "."
num_py_files = count_py_files(directory_to_check)

if num_py_files != -1:
    print(f"Number of .py files in '{directory_to_check}': {num_py_files}")

#Create a new folder named backup

#import os
#os.makedirs(r"Desktop\backup")
#print(os.makedirs(r"Desktop\backup"))


#Task 5: Reload Module During Development
#Create a module temp.py with a simple function.
#Import and use it in another script.
#Change the function in temp.py, then reload the module using importlib.

import temp
print(temp.month_name(8))


#Import and use it in another script.



#Change the function in temp.py, then reload the module using importlib.
import temp
import importlib
importlib.reload(temp)
print(temp.month_name(2))