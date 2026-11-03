#Python allows us to use else with both for and while loops.

#The else block executes when the loop finishes normally, without being terminated by break.

for num in range(1,6):
    if num == 3:
        break;
    print(num)
else:
    print("Loops completed successfully")


numbers = [10, 20, 30, 40]
target = 30

for num in numbers:
    if num == target:
        print("Found");
        break;
else:
 print("Not Found")

#Find out the sum
print(sum(numbers))

total=0;

for num in numbers:
    total=total + num;

print(total)
