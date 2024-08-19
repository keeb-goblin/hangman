import time; import random
# Importing Time and Random for the script and sleep.

# Name input
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
# Sleeby time
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)
# Select a random word from file "words.txt"
with open("words.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split()))
word = (random.choice(words))
# Creates an variable with an empty value
guesses = ''
# Determine the number of turns
turns = 10

# Create a while loop
# Check if the turns are more than zero
while turns > 0:         
    # Make a counter that starts with zero
    failed = 0             
    # For every character in the random chosen word
    for char in word:     
    # See if the character is in the player's guess
        if char in guesses:    
        # Print then out the character
            print (char,end=" "),    
        else:
        # If not found, print a dash
            print ("_",end=" "),        
        # And increase the failed counter with one
            failed += 1    
    # If failed is equal to zero
    if failed == 0:        
        print (" You won") ; time.sleep(2)
        break         

    guess = input(" guess a lowercase character:") 
    # Set the players guess to guesses
    guesses += guess          
    if guess not in word:  
     # Turns counter decreases by 1
        turns -= 1        
        print ("Wrong")  
        print ("You have", + turns, 'more guesses' )
    # If the turns are equal to zero
        if turns == 0:           
    
            print ("You Lose"  ) ; time.sleep(2)
