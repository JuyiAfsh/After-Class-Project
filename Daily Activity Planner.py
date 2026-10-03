hwk_time = int(input("Enter homework time in minutes: "))
if hwk_time >= 60:
    plan = "Start homework now!!!"
    print("That is a long homework session.")
else:
    plan = "Finish homework quickly"
    print("That is a short homework session.")

free_time = input("Is there free time after homework? (yes/no): ")
if free_time == "yes":
    print("Do any hobbies after homework is done")

print()
print("=== Daily Activity Planner ===")
print(f"Homework Time: {hwk_time}")
print(f"Plan: {plan}")
print(f"Free Time: {free_time}")
print("==============================")