import random

computer_number = random.randrange(1,50)
tries = 0
playing = True
while playing:
    user_guess = input("Enter a whole number between 1 and 50:\r\n")
    if user_guess.isnumeric():
        user_guess = int(user_guess)
        if user_guess >= 1 and user_guess <= 50:
            tries +=1
            if user_guess == computer_number:
                print("You win!") 
                print(f"You won after {tries} tries.")
                playing = False
            elif user_guess > computer_number:
                print("Nope. Guess lower")
                try_again = input("Do you want to try again?(y/n)\r\n")
                if try_again == 'y':
                    continue    
                elif try_again == 'n':
                    playing = False
            elif user_guess < computer_number:
                print("Nope. Guess higher") 
                try_again = input("Do you want to try again?(y/n)\r\n")
                if try_again == 'y':
                    continue    
                elif try_again == 'n':
                    playing = False       
        else:
            print("Number must be between 1 and 50")       
            continue
    else:
        print("Must be a whole number")   


