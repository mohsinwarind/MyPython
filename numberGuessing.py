def guess_number():
    import random
    secret_number  = random.randint(1,10)
    attempts = 0 
    print("Welcome to my Number Guessing Game ! ")
    print("I'm thinking of a number between 1 to 10 . Can you guess it ? ")
    while True:
        try:
            # Printing the computer Number ///
            # print(secret_number)
            guess = int(input("Enter your Number  : "))
            attempts+=1
            
            if guess < secret_number : 
                print("Oh Man ! You are to low , think a bit higher")
            elif guess > secret_number:
                print("Shh ,  You got to high Man ! ")
            else:
                print("Wow ! You guessed it right this time .")
                print(f"It toook you {attempts} to guessed the right number.")
                break;
        except:
            print("Please enter a Valid Number.")
            

# guess_number()        