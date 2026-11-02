str="Bhandary"

#Print D from last
print(str[-4])

#Reverse the str yradnahb
print(f"Here is the reversed word {str[::-1]}")


#Strings are Immutable
immutable="Tanjiro"

print(f"Upper case {immutable.upper()}")
print(f"lower case {immutable.lower()}")
print(f"title case {immutable.title()}")

#Print Ranjiro
print(f"Here is our word {"R" + immutable[1:]}")

#immutable[0]="R"
print(immutable[0])