x = 10
y = 20
z = 0

if x < y and z or not (x == 10 and y > 15):
    result = "A"
elif x == 10 or y < 15 and z == 0:
    result = "B"
else:
    result = "C"

final = result if x > 5 and not z else "D"
              

print(result)#B
print(final)#B