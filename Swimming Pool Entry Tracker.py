print("=== Swimming Pool Entry Checker ===")
print("Answer 3 quesions and you will be told which pool you can use.\n")

age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes/no): ").lower()
adult_here = input("Is an adult with you? (yes/no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 30)

if age <= 4:
    print("Toddler : splash pool only, always with an adult")
elif age <= 12:
    print("Child : main pool with an adult")
elif age <= 18:
    print("Teen : main pool only if you can swim")
else:
    print("Adult : all pools open for you")

if can_swim not in ("yes", "no"):
    print("Please answer with 'yes' or 'no'.")
    swim_known = False
else:
    swim_known = True

if adult_here not in ("yes", "no"):
    print("Please answer with 'yes' or 'no'.")
    adult_known = False
else:
    adult_known = True

if can_swim == "yes" and adult_here == "yes":
    print("You are allowed in the deep pool")
else:
    print("It is better to not go to the deep side.")

if age <= 12 or can_swim == "no":
    print("Stay in the shallow side for you own safety!")

if adult_known == True and not adult_here == "yes" :
    print("There is no adult with you - inform the lifeguard!")

if swim_known == False or adult_known == False:
    print("Cannot decide until both questions are answered properly.")
elif age >= 18 and can_swim == "yes":
    print("Ful acces given. Enjoy your swim.")
elif age >= 12 and can_swim == "yes" and adult_here == "yes":
    print("Main pool access given with adult nearby.")
elif can_swim == "no" and not (adult_here == "yes"):
    print("Use shallow end only, please find an adult.")
else:
    print("Shallow end today, come back with an adult for more.")

print()
print("Have a safe swim!")



