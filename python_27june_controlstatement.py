#conditionalstatement:used to execute certain blocks of code based on specific conditions
#if:used to check a condition, and execute it if the condition holds true.
a=input("enter your value:")
b=input("enter your value:")
if a==b:
    print("a is equal to b")

#if else statement:Incase of if or else statements are not execute else stamente code block will execute.
a=10
b=20
if a>b:
    print("a bigger than  b")
else :
    print("a is smaller than  b")

#elif statement:check multiple code blocks. if anyone of elif stmt execute the remaning will not execute.
a = input("enter your value:")
b = input("enter your value:")
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#nested if: one condition inside another.
#example
i = 0
if i != 0:
    # condition 1
    if i > 0:
        print("Positive")

    # condition 2
    if i < 0:
        print("Negative")
else:
    print("Zero")

x = 10
y = 5
if x > 5:
    if y > 5:
        print("x is greater than 5")
    elif y==5:
         print("x is greater than 5 and y is 5")
    else:
        print("x is greater than 5 and y is less than 5")

#match:match statement is used to perform different actions based on different conditions.

value=2
match value:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case x:
        print("default case")

#Ternary operator:if else statement shorthand code
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
value=900
print(value) if(value in list) else print("value not in list")

#Iterative statement:(for,while,break ,continue,pass):
#for:
fruits = ["aaaa", "bbbb", "cccc"]
for x in fruits:
    print(x)

list = ["meena", "vishu", "vismaya"]
name="meena"
for i in list:
    if i.upper()==name.upper():
        print("name exits in the list")
    else:
        print("name not exits")
else:
    print("loop is finished")
# Iterative a numbers
for i in range(10):
    print(i)

#while:The while loop keeps executing the block of code as long as the given condition is True.
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#nested :A nested loop is a loop inside a loop.
col = ["red", "yellow", "orange"]
fruits = ["apple", "banana", "orange"]
for x in col:
  for y in fruits:
    print(x, y)

#break:break statement is immediately terminated the loop
#1example
A={'a','b','c','d'}
val=A
for i in A:
    if i == val:
        print("print of val:A")
        break
    else:
        print("val not exits")
#2example
studentsList = ["ved", "charvy", "maha"]
for student in studentsList:
  print(student)
  if student == "ved":
    break
#continue statement:continue skips the current iteration and moves to the next one.
#1example
i = 0
while i < 5:
  i += 1
  if i == 2:
    continue
  print(i)

#2example
dept = ["hr", "manager", "developer"]
for x in dept:
  if x == "hr":
    continue
  print(x)

#pass: pass statement is a null statement; it does nothing when executed.
n = 10
if n > 10:
    pass
print('Hello')
