age = int(input("What is your age?:"))
if age > 40 and age < 64:
    print("you're over the hill")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirment!")
elif age == 21:
    print("Congrats on your 21st")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is just a number")
        
