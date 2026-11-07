# def demo():
#     value = yield
#     print("Received:", value)

# gen = demo() #Gen is variable which has Genetor object

# next(gen) #Start the generator

# try:
#  gen.send(100)
# except StopIteration:
#    print("Function Finish")



# def calculator():#Generator function
#     num = yield
#     yield num * 2

# gen = calculator() #Storing Generator object to gen variable

# next(gen) #Start the generator object

# print(gen.send(5)) #Passing 5 to gen varible which points to genetor object


# #Question

def test(): #Generator Function
    x = yield 100
    y = yield x
    yield y

gen = test() #Generator object will be passed to gen variable

print(next(gen)) #Start the generator object, # 100;
print(gen.send(50)) #Here we passed to 50 to our first yield ,x=50,passed 
print(gen.send(200))