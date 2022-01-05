import random
def play_game():
    playing = True
    the_choices = ['rock', 'paper', 'scissors']
    print("Welcome to rock, paper, scissors")
    user_score = 0
    computer_score = 0
    while playing == True:
        while computer_score < 3 and user_score < 3:
            user_pick = input("Make your choice:\r\n")
            computer_pick = random.choice(the_choices)
            print(f"Computer picked {computer_pick}")
            if (user_pick == 'rock' and computer_pick == 'scissors') or (user_pick == 'scissors' and computer_pick == 'paper') or (user_pick == 'paper' and computer_pick == 'rock'):
                print("Point to user") 
                user_score += 1 
            elif user_pick == computer_pick:
                print("Tie. Go again")
                continue
            else:
                print("Point to computer") 
                computer_score += 1 
            print(f"User - {user_score}. Computer - {computer_score}")       
        if computer_score == 3:
            print("Computer wins")
        elif user_score == 3:
            print("User wins")    
        playing = False    

play_game()        