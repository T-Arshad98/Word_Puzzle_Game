# Lab 2 - Word Puzzle Game, Version 2
# It runs in a python window
# It does not keep track of the number of guesses
# All letters are unknown
# It only gives the user one attempt to guess a letter


import random
from uagame import Window

def main():
    # Plays the game Word Puzzle
    
    # Window
    window_width = 600
    window_height = 800
    window = Window('Word Puzzle', window_width, window_height)
    
    # Instructions
    instructions_list = ['I’m thinking of a secret word.', 
                         'Try and guess the word. You can guess one letter', 
                         'at a time. Each time you guess I will show you', 
                         'which letters have been correctly guessed and which', 
                         'letters are still missing. You will have 4 guesses to', 
                         'guess all of the letters. Good luck!']
    
    text_size = 24
    text_color = "white"
    window.set_font_size(text_size)
    window.set_font_color(text_color)
    line_text_height = window.get_font_height()
    y_coord = 0    
    x_coord = 0
    
    for instruction in instructions_list: # draw 6 lines of instructions
        window.draw_string(instruction, x_coord, y_coord,)
        y_coord += line_text_height
    
    # Statements
    words_list = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    number_words = len(words_list)
    word_random = words_list[random.randint(0,number_words-1)] # randomly pick a word from the list
    
    word_selection = '' # create empty string to be modified
    for letter in word_random:  # modify the empty string to be the length of the random word, with underscores instead of letters
        word_selection = '_ ' + word_selection
        
    statements = ['The answer so far is: ', 
                  'Guess a letter: ']
    window.draw_string(statements[0] + word_selection, x_coord, y_coord,)
    y_coord += line_text_height
    
    # Check Letter
    guess = (window.input_string(statements[1],x_coord, y_coord)).lower()   # get user guess from input
    y_coord += line_text_height
    
    letters_guessed = 0 # integer that indicates how many times the user picked letter appears in the word
    word_final = '' #  create empty string to be modified
    for letter in word_random:  # for every letter in word_random (loop through each)
        if guess == letter: # check to see if the user guess is equal to the current letter in the loop
            letters_guessed += 1    # if equal, increment letters_guessed by 1
            word_final += guess + ' '   # concatenate word_final with the letter guessed
        else:
            word_final += '_ '    # concatenate word_final with an underscore
               
    if letters_guessed > 0: # if the number of correctly guessed letters is greater than 1
        window.draw_string(statements[0] + word_final, x_coord, y_coord,)       # redraw statement[0] and the word with underscores replaced with guessed letters
        y_coord += line_text_height
        window.draw_string('Good job! You found the word ' + word_random + '!', x_coord, y_coord,)
        y_coord += line_text_height
    else:
        window.draw_string(statements[0] + word_final, x_coord, y_coord,)
        y_coord += line_text_height        
        window.draw_string('Not quite, the correct answer was ' + word_random + '. Better luck next time.', x_coord, y_coord,)
        y_coord += line_text_height
        
    # End Game
    window.input_string('Press enter to end the game',x_coord, y_coord)
    window.close()

main()