from enum import nonmember
from operator import truediv

Name = input("Enter your Name:")
print("your Name is " +Name)

#operatores
#arthamatic operators:
#Int
print(1+3)
print(2-1)
print(2*10)
print(10/2)
print(10%8)
print(2**3)
print(10//2)

#Assignment operators
firstname="Meena"
firstname+=" shravanapalli"
print(firstname)

a=2
print(a)
a+=2
print(a)
a-=2
print(a)
a*=2
print(a)
b=5
b/=5
print(5)
b%=5
print(b)
b//=5
print(b)
b**=3
print(b)
#comparsion
a=1
b=2
print(a==b)
a=25
b=100
print(a<=b)
print(a>b)
print(a<b)
print(a>=b)
print(a!=b)

#Logical :
a=10
print(a>1 and a<100)
print(a>1 or a<0)
print(not(a>1 and a<0))

#bitwise
print(4&2)#AND
print(4|2)#or
print(4^2)#Xor
print(~4)#not
print(4<<2)#leftshift
print(4>>2)#rightshift

#membership
print("a"in "apple")
email="krishna@gmail.com"
print(("@"in email)and(".com"in email))
print(("x "not in email))
print(("x " in email))

emails=["meena@gmail.com","praneeth@gmail.com","sabees@gmail.com"]
email="meena@gamil.com"
print(email in  emails)
print(email not in emails)

#Identity
a=10
b=a
print(a is b)
print(a is not b)

#Datatypes
#Numbers/numeric
#int
a=1
print(type(a))
print(10+3)

#float
print(1.3+0.2)
a=2.8
print(type(a))
#complex
a=1+2j
b=1+3j
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#srting
#char/str
name="meena"
print(name)
print(type(name))

#Non-nothing
a = None
print(type(a))


















