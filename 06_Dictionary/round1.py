#Dictionary is a datatype named dict.
car = {"brand": "Maruti", "model": "Swift", "year": 2022}

#Methods keys,values and items
carKeys=car.items()
for cars in carKeys:
    print(cars[1])

# print(car)


# #Access
# print(car["brand"])
# print(car.get("name","Not Found"))

# #Update
# car["year"]=2026;
# car.update({"year":"2026","brand":"Royals Roise"})
# print(car)

# #Add
# car["color"]="white"
# print(car)

# #Delete
# del car["color"]
# car.pop('brand')
# print(car)