nums = [1, 2, 3, 4, 5]

#Using lambda
answer=map(lambda num:num*2,nums)
print(list(answer))

result=[]

for num in nums:
    result.append(num*2)

print(result)


#Filter even numbers
arr = [1, 2, 3, 4, 5, 6, 7, 8]

store=filter(lambda num:True if num%2 == 0 else False,arr)

print(list(store))



numbers = [-8, 3, -2, 5, -1] #Sort according to the absolute difference
# 8,3,2,5,1 = -1,-2,3,5,-8

numbers.sort()
print("Soring according to Ascending order",numbers)
numbers.sort(reverse=True)
print("Soring according to Descending order",numbers)

#sorted(iterable, key=function, reverse=False)

ans=sorted(numbers,key=lambda num:abs(num),reverse=False)
print(ans)
