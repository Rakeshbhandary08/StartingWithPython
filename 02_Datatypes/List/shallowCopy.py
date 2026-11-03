a=[10,20,30]

b=a;
b.append(100)


print(a)

#SHallow copy
c=a.copy()

c.append(200)

print(a)
print(c)