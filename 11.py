z = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
print(z)
a = {}
a.update([("name", "Kelly"), ("salary", 8000)])
print(a)
z.pop("name")
z.pop("salary")
print(z)

z = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
print(z)
z.pop("city")
z.update([("location", "New York")])
print(z)



























