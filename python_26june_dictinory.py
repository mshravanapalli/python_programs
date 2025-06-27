#Dictionary: ordered ,mutable,not allow duplicates
employee={
  id:1,
  "Name" :'Meena',
    "email":'m@gmail.com'
}
print(employee)

#Add item dict
employee["gender"]='female'
print(employee)

#update item dict
employee.update({"country":"India"})
print(employee)
#create employees
employee1={
    id:2,
    "Name":"nikhil",
    "Email":'nkhil@gmail.com',
    "gender":'male',
    "country":'India'
}
employee2={
    id:3,
    "Name":'praneeth',
    "Email":'p@gmail.com',
    "gender":'male',
    "country":'India'
}
employee3={
    id:4,
    "Name":'sabeer',
    "Email":'sa@gmail.com',
    "gender":'male',
    "country":'India'
}
employee=[]
employee.append(employee)
employee.append(employee1)
print(employee)
employee=[]
employee.append(employee)
employee.append(employee2)
print(employee)
employee=[]
employee.append(employee)
employee.append(employee3)
print(employee)

#create product
Products={
    "proId":1,
    "ProName":"smartphone",
    "price":20000,
    "city": "Hyderabad",
    "country":"India"
}
print(Products)
Product2={
    "proId":2,
    "ProName":"smartphone",
    "price":20000,
    "city": "Hyderabad",
    "country":"India"
}
Product3={
    "proId":3,
    "ProName":"smartwatch",
    "price":25000,
    "city":"secunderabad",
    "country":"India"
}
#create Productslist
Product  =[]
Product.append(Products)
Product.append(Product2)
Product.append(Product3)
print(Product)

#create orders
Orders12={
    "Id":1,
    "name":"chocolates",
    "custname":"vishu",
    "brand":"dairymilk",
    "city":"hyderabad"
}
print(Orders12)
Order1={
    "Id":2,
    "name":"laptop",
    "custname":"AAA",
    "brand":"lenovo",
    "city":"hyderabad"
}
print(Order1)
#add
Order1["Email"]="CC@gmail.com"
Order2={
    "Id":3,
    "name":"tv",
    "custname":"BBB",
    "brand":"LG",
    "city":"hyderabad"
}
#update
Order2.update({"email":"cus@gmail.com","mobilenumber":123456})
print(Order2)

#create Orderslist
Orders12=[]
Orders12.append(Orders12)
Orders12.append(Order1)
Orders12.append(Order2)
print(Orders12)


