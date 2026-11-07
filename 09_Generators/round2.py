# #Iterator object
# nums=[10,20,30]

# gen=iter(nums) #Iterator object
# print(gen)

# print(next(gen))
# print(next(gen))
# print(next(gen))

# #Generator object
# def genObj():
#     yield 10;
#     yield 20;
#     yield 30;

# store=genObj() #store will get the generator object
# print(next(store))
# print(next(store))
# print(next(store))


# def demo():
#     yield 10
#     yield 20

# gen = demo()

# print(next(gen))
# print(next(gen))
# print(next(gen))


#Output
numbers = (x * 2 for x in range(1, 5)) #Generator expression ()->Generator object


print(next(numbers)) #new generator object created and first value that is 2 will be printed
print(next(numbers)) #again new generator object created and first value that is 2 will be printed

for num in numbers:
    print(num)