#Checking multiple condition

#AND , OR 
age=20
print(18 <= age and age <= 30)

#IF any of the condition true the system is under pressure
cpu_usage=90;
memory_usage=60;

print(f"is our system under pressure: {cpu_usage >= 90 or memory_usage >= 90}")


#NOT Operator
print(not 10>0)

#Run the if the arra is not empty
isEmpty=False
print(not isEmpty)