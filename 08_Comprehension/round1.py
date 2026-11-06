#Comprehension is a concise way of creating list,tuple ,dictonaries,etc..

#List Comprehension

#Synax =[variable_name,loop,condition]

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#Find out the even numbers

#Normal Way 
even_no=[]
for num in numbers:
    if num%2 == 0:
        even_no.append(num)
print(even_no)

#Comprehension way
even_num=[numm for numm in numbers if numm % 2 == 0]
print(even_num)


names=['rakesh kumar','suResh jhA','Mahek siNGH','Ritu TIWAri']

capitilized=[name.capitalize() for name in names]
print(capitilized)

#List with If else
numberss = [1, 2, 3, 4, 5, 6]

print(["Even" if num%2 == 0 else "Odd" for num in numberss])
