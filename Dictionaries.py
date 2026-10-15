# Key Value pairs

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
# Key should exist and case sensitive

print(customer.get("age"))
print(customer.get("DOB","Jan 1 1970"))