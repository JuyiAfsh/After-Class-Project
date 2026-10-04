print("===================================")
print("Welcome to Holiday Activity Planner!!!")
print("===================================")
print()

print("What type of holiday would you like?")
print("   1. Beach Holiday   ")
print("   2. Mountain Holiday   ")

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1 :
    print("Pick your Beach Activity: ")
    print("  a. Swimming  ")
    print("  b. Sandcastle Building")
    print()

    beach_activity = input("Enter a or b: ")
    print()

    if beach_activity == "a":
        print("You picked   : Swimming")
        print("Best Time    : Morning")
        print("Reminder     : Put sunscreen")
    elif beach_activity == "b":
        print("You picked   : Sandcastle Building")
        print("Best Time    : Evening")
        print("Reminder     : Take a bucket and spade")
    else:
        print("That was not a valid choice.") 
        print("Please enter 'a' for Swimming and 'b' for Sandcastle Building")  
        

elif choice == 2 :
    print("Pick your Mountain Activity: ")
    print("  a. Hiking  ")
    print("  b. Camping  ")
    print()

    mountain_activity = input("enter a or b: ")
    print()

    if mountain_activity == "a":
        print("You picked   : Hiking")
        print("Best for     : Exploring trails")
        print("Reminder     : Wear confortable shoes")
    elif mountain_activity == "b":
        print("You picked   : Camping")
        print("Best for     : Spending time with friends and family")
        print("Reminder     : Carry a tent")
    else:
        print("That was not a valid choice.") 
        print("Please enter 'a' for Hiking and 'b' for Camping")

else:
   print("That was not a valid choice.") 
   print("Please enter 1 for Beach Holiday and 2 Mountain Holiday")  

print()
print("==================")
print("    Your holiday plan is ready!     ")
print("    Enjoy the trip!                 ")
print("===================")
