#problem
#get a positive input from a user
#generate a random number between the number provided.
#Prompt user to guess the number ( a posivie integer)
#if it's less, Print too small! and reprompt the user
#if it's too big, print too large! & reprompt the user
#if the guess is right, print Just right! and break


#My solution

from random import randrange

# Prompt the user for an input - a positive integer & randomize the input
# Prompt the user again for an input called guess - a positive integer
# Check if the user guess is the same has the randomized result.
# if yes, print just right else print too small or too big if it's too small or too big & reprompt the user to
# guess the randomized result again.

def main():
    randomized_no = randomize_no()
    while True:
        user_guessed_input = guess()
        if int(user_guessed_input) > randomized_no:
            print("Too large!")
            continue
        elif int(user_guessed_input) < randomized_no:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break

# make sure whatever the user inputted is a positive integer.
def is_positive_integer(n):
    """This function takes an input and check if the user input is an integer"""
    while True:
        try:
            num = int(n)
            if int(num) < 1:
                return False
        except ValueError:
            return False
        else:
            return True

#Prompt the user for an input and check if what user inputted is a positive interger

def get_user_input():
    """Prompt the user for an input and check if it's a positive integer"""
    while True:
        user_input = input("Level 1: ")
        if (is_positive_integer(user_input)):
            return int(user_input)


#Prompt the user to guess and check if that number is a positive integer.
def guess():
    "Prompt the user for an input guess, and check if it's an integer"
    while True:
        user_guess = input("Guess: ")
        if is_positive_integer(user_guess):
            return user_guess


# call get_user_input which collects an input from user and check if it's an integer
# Randomize the number collected from the get_user_input function and return it.
def randomize_no():
    """Randomize number"""
    user_inputted_number = get_user_input()
    if int(user_inputted_number) > 1:
        random_number = randrange(1,  user_inputted_number)
        return random_number
    else:
        return int(user_inputted_number)

if __name__ == "__main__":
    main()














