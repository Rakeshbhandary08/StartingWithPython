#Because calling a generator function doesn't execute its body immediately. It creates a generator object.
#To retrieve its values, we can use next().

# def calling_num():
#     for num in range(1,6):
#         yield num


# print(next(calling_num()))
# print(next(calling_num()))
# print(next(calling_num()))


def demo():
    yield 100
    yield 200
    yield 300

gen = demo()

print(next(gen)) #100

gen = demo() #gen ko new copy

print(next(gen)) #100
print(next(gen)) #200