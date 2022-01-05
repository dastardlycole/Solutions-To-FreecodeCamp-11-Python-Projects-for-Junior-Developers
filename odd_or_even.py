a = 5
while a == 5:
    user_number = int(input("Enter a number between 1 and 1000: \r\n"))
    if user_number >= 1 and user_number <= 1000:
        if user_number % 2 == 0:
            print("That's an even number")
            a = 4
        else:
            print("That's an odd number")   
            a = 4 
    else:
        print("Number must be between 1 and 1000. Try again...")        