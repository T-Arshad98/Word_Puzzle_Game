# Lab 2 - Word Puzzle Game, Version 3
# This is the final version of the program
# It runs in a python window
# The number of guesses is limited to 4
# If an incorrect guess or a repeated guess is entered, number of guesses remaining decreases by 1
# All letters are unknown

import random
from uagame import Window

def create_window():
    window_width = 600
    window_height = 800
    window = Window('Word Puzzle', window_width, window_height)
    return window

def display_instructions(window, instructions, string_coords):
    text_size = 24
    text_color = "white"
    window.set_font_size(text_size)
    window.set_font_color(text_color)    
    
    for instruction in instructions: # draw 6 lines of instructions
        window.draw_string(instruction, string_coords[0], string_coords[1])
        string_coords[1] += window.get_font_height()
        
def display_puzzle_string(window, puzzle, string_coords):
    puzzle_str = '' # create empty string for the puzzle's current state
    for element in puzzle:
        puzzle_str += element + ' ' # take the puzzle list and turn it into a string
    window.draw_string('The answer so far is: ' + puzzle_str, string_coords[0], string_coords[1],)
    string_coords[1] += window.get_font_height()   
    
def play_game(window, puzzle, answer, string_coords):
    num_guesses = 4 # initial number of gueses
    guess_list = '' # blank list of letters guessed so far
    word_found = False  # bool if the word has been found
    is_win = False  # bool if game has been won
    
    while (num_guesses > 0) and (word_found == False):  #while number of guesses is greater than 0 and word has been found   
        guess = get_guess(window, puzzle, num_guesses, string_coords)   # get the current guess
        
        repeated_letter = False
        repeated_test = 0
        for element in guess_list:
            if element == guess:
                repeated_test += 1
        if repeated_test > 0:
            repeated_letter = True  # this means the letter has been previously entered
            
        guess_list += guess # concatenate the current guess to guess_list
        update_performed = update_puzzle_string(puzzle, answer, guess)  # check if puzzle list is updated
        display_puzzle_string(window, puzzle, string_coords) 
                
        if repeated_letter == True: # if current guess was previously entered, decrease number of guesses remaining by 1
            num_guesses = num_guesses - 1  
        elif update_performed == False: # or if guess is not correct, decrease number of guesses by 1
            num_guesses = num_guesses - 1
        elif update_performed == True:  # or if guess is correct and puzzle is updated, check if whole word is solved
            word_found = is_word_found(puzzle)
            if word_found == True:  # if word is solved, game has been won
                is_win = True
    
    return is_win
    
def get_guess(window, puzzle, num_guesses, string_coords):
    guess_is_alpha = False
    while guess_is_alpha == False: 
        guess = (window.input_string('Guess a letter(' + str(num_guesses) + ' guesses remaining):',string_coords[0], string_coords[1])).lower()   
        string_coords[1] += window.get_font_height()                
        if len(guess) > 1:  # check if user input is a single entry only
            guess_is_alpha = False
        elif guess.isalpha() == True:   # check if user input is alphanumerical
            guess_is_alpha = True
    return guess

def update_puzzle_string(puzzle, answer, guess):
    #else:
    index = 0
    update_performed = False
    for letter in answer:  # for every letter in answer (loop through each)
        if guess == letter: # check to see if the user guess is equal to the current letter in the loop
            puzzle[index] = guess
            index += 1
            update_performed = True
        else:
            index += 1
    return update_performed
    
def is_word_found(puzzle):
    word_found = False
    for letter in puzzle:
        if letter == '_':   # check if there are any unknowns(underscores) left in the puzzle
            word_found = False
            break
        else:
            word_found = True
    return word_found
            
        
    
def display_result(window, is_win, answer, string_coords):
    if is_win == True:  # if the user has solved the word
        window.draw_string('Good job! You found the word ' + answer + '!', string_coords[0], string_coords[1],)
        string_coords[1] += window.get_font_height()
    elif is_win == False:   # if the user has run out of guesses
        window.draw_string('Not quite, the correct answer was ' + answer + '. Better luck next time.', string_coords[0], string_coords[1],)
        string_coords[1] += window.get_font_height()

def end_game(window, string_coords):
    window.input_string('Press enter to end the game',string_coords[0], string_coords[1])
    window.close()    
    


def main():
    window = create_window()
    
    instructions = ['I’m thinking of a secret word.', 
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
    
    string_coords = [0, 0]  # element 1 is x_coord, element 2 is y_coord  

    display_instructions(window, instructions, string_coords)    
    
    words_list = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    answer = random.choice(words_list) # randomly pick a word from the list
    puzzle = len(answer)*['_']
    
    display_puzzle_string(window, puzzle, string_coords) 
    is_win = play_game(window, puzzle, answer, string_coords)
    display_result(window, is_win, answer, string_coords)
    end_game(window, string_coords)

main()