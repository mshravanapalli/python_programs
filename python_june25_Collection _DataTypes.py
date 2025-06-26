
#Collection Data Types:
#set:unordered,mutable,unique
setlist={1,2,3,4}
print(setlist)

setlist={"meena"," praneeth" , "nikhil"," sabeer"}
print(setlist)

#Add item to set:
setlist={22,33,44,55}
setlist.add(66)
print("setlist add :",setlist)

#remove item
setlist={22,45,34}
setlist.remove(22)
print("setlist remove :",setlist)

#Clear item
setlist={"1,2,3,4,5,2,3"}
setlist.clear()
print("setlist clear:",setlist)

#Pop
setlist={"a","b","c","d"}
setlist.pop()
print("setlist pop item:",setlist)

#union
a={"meena","mishika","vismaya"}
b={"vishu","maha"}
print("print union items:",a.union(b))
#intersection
a={"meena","mishika","vismaya"}
b={"vishu","mishika"}
print("print intersection :",a.intersection(b))
#subset
a={"meena","mishika","vismaya"}
b={"vishu","mishika"}
print("print is subset :",b.issubset(a))

#join/update
a={1,3,4}
b={2,3,5,4}
a.update(b)
print("print update values :",a)

#copy item
a={"meena","mayu","raj","ram"}
b=a
b.add("ragu")
print(a)

a={1,2,3}
b=a.copy()
b.add(4)
print(a)

#Frozenset([]) --unordered,immutable,unique
fst = ['apple', 'banana', 'cherry']
print(fst)
fst1=frozenset([1,2,3,4,5])
print(fst1)
#copy
fst2=frozenset([11,22,44])
fst3=fst2.copy()
print(fst2)
#union
fst1=frozenset([1,2,3])
fst2=frozenset([11,22])
print(fst1.union(fst2))

#list[] ordered,mutable ,allow duplicates
list =[1,"meena","@gmail.com,2.43"]
print("print list :",list)

#1.append:

list1 =[1,2,3]
list1.append(4)
print(list)

#2.extend
list1=["meena","shravanapalli"]
list1.extend("vishu")
print(list)

list1=["meena","shravanapalli"]
list1.extend(["vishu"])
print(list1)

#3.Insert
list1=[1,2,3]
x=list1.insert(0,5)
print(x)

#4.remove
list1=["a","b","c","j"]
list1.remove("j")
print(list1)

#5.pop
list1=["sql","java","python"]
list1.pop(0)
print(list1)

#6.clear
list1=[100,200,300,400,400]
list.clear()
print(list)

#7.index
list = ['a', 'b', 'c','d']
x=list.index("c")
print("print x value :",x)

#8.count
list=['a','b','c','f','e','f','g','f']
x=list.count("f")
print("print x value :", x)

#9.sort
list=[1,4,5,7,9]
list.sort()
print(list)

#10.reverse()
list=['n','b','e','a']
list1.reverse()
print(list)

#11.copy()
list=[1,2,3,4,5,7,1.4]
list.copy()
print(list)

#tuple( immutable ,allows duplicate values)
tuple1=(1,2,3,4)
print(tuple1)
print(type(tuple1))

#count
tuple1=(1,45,2,45,5,45,3,45)
print(tuple1.count(45))

#index

tuple1=(11,22,33)
print(tuple1.index(33))






























