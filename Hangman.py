def check_letter(guess): # Loops until user gives valid letter
    for char in range(len(guess)):
        if not guess[char].isalpha() and not guess[char] == " ":
            guess = input("Not a valid letter. Guess again. ")
    '''while not guess.isalpha():
        guess = input("Not a valid letter. Guess again. ")'''
    return guess

def in_word(guess, lives):
    if guess not in hidden_word_arr:
        lives = lives - 1
    while guess.lower() in hidden_word_arr: # Loops until no more guessed letter in hidden_word_arr
        index = hidden_word_arr.index(guess.lower()) # Index of guess in hidden_word_arr
        hidden_word_arr[index] = "_" # Sets guess in hidden_word_arr to _
        display_word_arr[index] = guess.lower() # Sets corresponding place in display_word_arr to guess
    return lives

def display_word(display_word_arr):
    for char in range(len(display_word_arr)): # Numbers 0 to length of display_word_arr - 1
        print(display_word_arr[char], end = " ") # Displays parts of display_word_arr on the same line
    print("\n")

def whole_word(guess, lives):
    if guess == hidden_word: # If the guess for the whole word is correct
        for char in range(len(display_word_arr)): # Numbers 0 to length of display_word_arr - 1
            if display_word_arr[char] == "_": # If the character in display_word_arr is blank
                display_word_arr[char] = hidden_word_arr[char] # Change the blank char to the char in hidden_word_arr
    else:
        lives = lives - 1
    return lives

# Main program
hidden_word = "we are so screwed" # Word being guessed
lives = 6
hidden_word_arr = []
display_word_arr = []
for char in range(len(hidden_word)):
    hidden_word_arr.append(hidden_word[char]) # Fills hidden_word_arr with one letter per space
    if hidden_word[char] != " ": # If the character in the word being guessed is not a space
        display_word_arr.append("_") # Fills display_word_arr with _
    else: # If the character is a space
        display_word_arr.append(" ")
#print(hidden_word)
#print(hidden_word_arr)
#print(display_word_arr)
while lives != 0 and "_" in display_word_arr:
    display_word(display_word_arr)
    guess = input("Guess a letter or the whole word: ") # User inputs letter or whole word
    guess = check_letter(guess) # Checks if guess is letter
    if len(guess) == 1:
        lives = in_word(guess, lives) # Checks if letter guess is in word, changes lives
    else:
        lives = whole_word(guess, lives) # Checks if whole word guess is right, changes lives
    print("You have "+str(lives)+" lives left.")
    
display_word(display_word_arr)
