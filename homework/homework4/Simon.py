# Data Structures HW4 
# PROBLEM 3
'''
In the game Simon a four-colored disk can play a random sequence of tones and lights. 
Each color on the disk is actually a button that can be pressed, with a light behind it.
As the game makes a tone, it also flashes the light with that tone. 
The game is for the user to press the buttons in the sequence that is played by the game's controller. 
The sequence starts with a single light/tone, then increases the number of lights/tones by adding one new trial to the sequence each time the player gets the entire order correct. 
The game is over when the user makes a mistake in entering the sequence.
Using the letters R for Red, G for Green, Y for Yellow, and B for Blue, implement the game. When the player makes a mistake in the sequence, ask if they would like to play again. 
Implement the game as follows:
Be sure that the sequence is random. Make your program display the string each time, letter by letter, with the letters separated by spaces. 
Try to make a short delay before each letter is displayed. 
Once all the letters in the sequence are displayed wait one second and then make your program output backspace characters to erase the displayed string. 
Then read the user's input and display each character as it is entered.
When the user makes an error output a mistake message.
'''
import random
import time 
import os
# Sequence to select from:
color_sequence = ['G', 'B', 'R', 'Y']
# Select the letters at random:
rand_index = random.randint(0, len(color_sequence)-1)
# Simon_sequence will store the sequence generated.
Simon_sequence = [ ]
print("Start the game.\n")
time.sleep(1)
Simon_str = '' 
Simon_str_space = ''
user_input = ''  # statements used to enter the while loop. 
back_spaces = ''
while Simon_str == user_input :
    rand_index = random.randint(0, len(color_sequence)-1)
    Simon_sequence.append( color_sequence[rand_index] )
    Simon_str = ''.join(map(str, Simon_sequence)) # systax was obtained from: https://favtutor.com/blogs/print-list-python#:~:text=When%20you%20wish%20to%20print,or%20sep%3D%E2%80%9D%2C%E2%80%9D.
    Simon_str_space = ' '.join(map(str, Simon_sequence))  # if use enters a sentence with spaces, it is interpreted as the same sequence.
    print("Simon's sequence: ", end='')
    # this loop will print the letters in Simon's sequence.
    for i in range(len(Simon_sequence)):
        print(Simon_sequence[i] + ' ' , end='')
        time.sleep(1)
        back_spaces = back_spaces + '\b\b' #thinking about using this for another implementation method.
    time.sleep(0.7)
    os.system("cls")
    user_input = str(input("Enter the sequence: "))
    user_input = user_input.replace(" ", "") # REMOVE SPACES. PROGRAM WILL ACCEPT INPUTS WITH OR WITHOUT SPACES BETWEEN THE LETTERS.
    if Simon_str  != user_input:
        print("Ups wrong sequence. Game over.")
        time.sleep(1)
        break
    time.sleep(1)
    # the following line clears the terminal:
    os.system("cls") # systax from: https://stackoverflow.com/questions/65330048/python3-how-to-clear-previous-prints-while-looping-flush



