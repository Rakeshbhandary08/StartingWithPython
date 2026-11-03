age=10
authorized="Yes" if age >= 18 and age <= 60 else "No"

print(authorized)

#Question
a = 5
b = 0 #Falsy value
c = 15

if a > 2 and b or c < 10:
    x = "Hello"
else:
    x = "World"

y = "Python" if x == "Hello" else "JavaScript" if not b else "C++"

print(x) #"World"
print(y)


#Question
a = 0
b = 10
c = 20

result = "A" if a else "B" if b > 5 and not c else "C" if c else "D"

if a:
    result="A"
else:
    if b>5 and not c:
     result="B"
    else:
       if c:
          result="C"
       else:
          result="D"

print(result)