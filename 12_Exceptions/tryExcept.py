# student={"name":"Rakesh","year":2027}

# try:
#  print(student["course"]) #sensitive call
# except KeyError:
#  print("Key is missing")

# print("Hello world")

def calling(a):

    try:
        if a=="unknown":
         raise NameError("This is not valid value")
    except NameError as e:
        print("Error",e)
    else:
        print(f"This is {a}")
    finally:
        print("Function Execution is done")

calling("unknown")