# This is the third version of the Hacking Game.
# This version includes all game features and user-defined functions in the code.

# Import functions.
import random

#Define/Assign variables.
words = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING']
password = random.choice(words)
guessesRemaining = 4
print(password)

# Define user-defined functions.
def instructionList():
# Display instructions.
    instructions = ['A group of possible passwords will be displayed.', 'You must guess the password. You have at most 4 guesses.', 'If you are incorrect, you will be told how many letters ', 'in your guess were exactly the correct location of the password.']
    
    for anInstruction in instructions:
        print(anInstruction)

def passwordList():   
# Display list of possible words to be password.
    for word in words:
        print(word)

def guessingPassword(password, guessesRemaining):
# Prompt player to input a password and display number of guesses remaining.
    while guessesRemaining > 0:
        guessPrompt = 'Enter password ' + '(' + str(guessesRemaining) + ' guesses remaining' + ') > '
        guess = input(guessPrompt)
        guessesRemaining = guessesRemaining - 1

        if guess != password:
            print('Password Incorrect.')
    
            def correctLetters():
            # Display number of correct letters in the incorrect word/password that are in the same position as the correct password.
                correct = 0
                for number in range(0, len(guess)):
                    if number < len(password) and guess[number] == password[number]:
                        correct += 1
                print(str(correct) + '/7')   
            
            correctLetters()
                
        else:
                break
    
    if guess == password:
        print('User login successful!')

    else:
        print('User login unsuccessful.')

# Create main() function to call user-defined functions.
def main():
    instructionList()
    passwordList()
    guessingPassword(password, guessesRemaining)

# Call main() function.
main()