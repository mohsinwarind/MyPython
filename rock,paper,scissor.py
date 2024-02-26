def play_game():
    import random
    choices = ['rock', 'paper', 'scissor']  
    
    won = 0 
    lost = 0
    
    while True:
        computer_choice = random.choice(choices)  
        user_choice = input("Choose something from 'rock', 'paper', and 'scissor', or 'exit' to exit: ").lower()
        
        print(f"You Chose: {user_choice}")
        print(f"Computer Chose: {computer_choice}")
        
        if user_choice == 'exit':
            print("Exiting the Game...")
            break
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissor' and computer_choice == 'paper'):
            print("You Won!")
            won += 1
            print(f"You won {won} times")
        elif user_choice == computer_choice:
            print("It's a Tie.")
        elif user_choice not in choices:
            print("Please Enter a Valid Input.")
        else:
            print("You Lost.")
            lost += 1
            print(f"You lost {lost} times.")
    
    print(f"You Won {won} games and lost {lost} games.")

play_game()
