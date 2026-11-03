
balance=25000;

print(
    "1.check Balance",
    "2.Deposit",
    "3.Withdraw",
    "4.Exit"
)

choice=int(input("What would to like to do:"));
print(f"You selected option {choice}");

if choice == 1:
    print(balance)
elif choice == 2:
    print("Deposit selected")
elif choice == 3:
    print("Withdraw selected")
elif choice == 4:
    print("Thank you for visiting us")
else:
    print("Invalid Option")

