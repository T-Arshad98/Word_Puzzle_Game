# Lab 2 - Word Puzzle Game, Version 1
# It runs in a python window
# It does not keep track of the number of guesses
# Only the first letter is unknown and needs to be guessed
# It only gives the user one attempt to guess the word


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
                         'letters are still messing. You will have 4 guesses to', 
                         'guess all of the letters. Good luck!']
    
    text_size = 24
    text_color = "white"
    window.set_font_size(text_size)
    window.set_font_color(text_color)
    line_text_height = window.get_font_height()
    y_coord = 0    
    x_coord = 0
    
    for instruction in instructions_list:
        window.draw_string(instruction, x_coord, y_coord,)
        y_coord += line_text_height
    
    # Statements
    words_list = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    number_words = len(words_list)
    word_random = words_list[random.randint(0,number_words-1)]
    word_selection = '_' + word_random[1:]
    statements = ['The answer so far is: ' + word_selection, 
                  'Guess a letter: ']
    window.draw_string(statements[0], x_coord, y_coord,)
    y_coord += line_text_height
    guess = (window.input_string(statements[1],x_coord, y_coord)).lower()
    y_coord += line_text_height
    
    # Check Letter
    if word_random[0] == guess:
        window.draw_string('Good job! You found the word ' + word_random + '!', x_coord, y_coord,)
        y_coord += line_text_height
    else:
        window.draw_string('Not quite, the correct answer was ' + word_random + '. Better luck next time.', x_coord, y_coord,)
        y_coord += line_text_height
        
    window.input_string('Press enter to end the game',x_coord, y_coord)
    window.close()

main()