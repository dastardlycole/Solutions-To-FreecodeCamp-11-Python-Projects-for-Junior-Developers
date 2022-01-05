my_var = 8
while my_var == 8:
    user_name = input("Enter your name:\r\n")
    while len(user_name) < 2:
        print("Enter a valid username")
        user_name = input("Enter your name:\r\n")    
    dob = input("Enter your date of birth:\r\n")    
    addy = input("Enter your address:\r\n")
    pgoals = input("Enyter your personal goals:\r\n")
    break

print(f"- Name: {user_name}")
print(f"- Date of Birth: {dob}")
print(f"- Address: {addy}")
print(f"- Personal goals: {pgoals}")

