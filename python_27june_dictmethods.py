#dictionary: ordered,mutable,not allow duplicates
#create customers
from email.policy import default

emp1={
    "id":1,
    "Name":'raju',
    "dept":'ccc',
    "city":'sec',
    "phone":13242354
}
emp2={
    "id":2,
    "Name":'vishu',
    "dept":'aaaa',
    "city":'hyd',
    "phone":63543543
}
emp3={
    "id":3,
    "Name":'mishika',
    "dept":'bbb',
    "city":'hyd',
    "phone":653533
}
emp4={
    'id':4,
    'Name':"meena",
    'dept':"ddd",
    'city':"hyd",
    'phone':"699786"
    }

#empList
emplist=[]
emplist.append(emp1)
emplist.append(emp2)
emplist.append(emp3)
emplist.append(emp4)
print(emplist)

#update item to dict
emp1.update({"gender":"male"})
emp2.update({"gender":"male"})
emp3.update({"gender":"female"})
emp4.update({"gender":"female"})
print(emplist)

#setdefault:adding key is not exists  it will add,if key is exits nothing will happens
emp1.setdefault("email","s@gmail.com")
emp2.setdefault("email","v@gmail.com")
emp3.setdefault("email","a@gmail.com")
emp4.setdefault("email","m@gmail.com")
print(emplist)

#get method:get dict values by using dict key
print(emp1.get("email"))
print(emp2.get("email"))
print(emp3.get("email"))
print(emp4.get("email"))

#get all the key from dict
print(emplist[0])
print(emplist[1])
print(emplist[2])
print(emplist[3])

#key method:it is used to get all the keys from the dict
print(emp1.keys())

#value method:get all the value from dict
print(emp1.values())
print(emp2.values())
print(emp3.values())
print(emp4.values())

#create a dictionary with key and default values
keys=("id","Name","dept","city","phone","email")
value=""
emp1.fromkeys(keys,value)
print(emp1)
emp2.fromkeys(keys,value)
print(emp2)

#get:get the dict value based on key
print(emp2.get('Name'))
print(emp2.get('phone'))

#item:get the key and value as tuple pair
print(emp4.items())

#delete/remove method:
#pop:remove specific key item from the dict
emp1.pop("Name")
print(emplist)

#popitem:remove last inserted key value pair
emp3.popitem()
print(emp3)

#clear:remove all the items from the dict
emp1.clear()
emplist.clear()
print(emplist)





















