#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
These are the functions Maximilian calls when a menu choice have been chosen.
"""

import random

def greeting():
    """
        Will ask for the persons name and greet the person.
    """
    name = input("What is the name of my new friend? ")
    print("\n Maximilian says:\n")
    print("Zup, %s! Kingen." % name)
    print("What can I do you for?!")
    

def convert_C_to_F():
    """
    Converts celsius to farenheit
    """
    celsius = input("Enter your degrees in Celsius and I'll convert it to Farenheit for you ")
    farenheit = float(celsius) * 9 / 5 + 32

    print(str(celsius) + 'C' + ' is ' + str(farenheit) + 'F')

def word_multiplyer():
    """
    Repeats a word x amount of times.
    """
    word = input("What word would you like to repeat? ")
    number = input("How many times would you like to repeat it? ")

    num = 1
    while num <= int(number):
        print(word)
        num += 1 
      
         
def sum_and_avarage():
    """
    Sums and calculates the average of the chosen numbers.
    """   
    result = 0
    iterations = 0
    user_input = ""
    print("When you are happy with your numbers write done to get the sum and average")

    while user_input != "done":
        user_input = input("Write a number: ")

        if user_input != "done":
            result += int(user_input)
            iterations += 1
        
    average = result / iterations
    print("---------------")
    print("Sum " + str(result))
    print("Average: " + str(average))


def compare_numbers():
    """
    Checks is the previous number is bigger, smaller or the same as the current number.
    """
    number_entered = ""
    saved_number = 0
    print("When you are done using it, write done")

    while number_entered != "done":
        number_entered = input("Write a number: ")

        if number_entered != "done" and saved_number != 0:
            if int(number_entered) < int(saved_number):
                print("Less than the previous.")
            elif int(number_entered) > int(saved_number):
                print("Bigger than the previous.")
            elif int(number_entered) == int(saved_number):
                print("Same as previous.")

        saved_number = number_entered
      
def character_multiplyer():
    """
    Multiply all th chars with their place in the sequence +1.
    """   
    iterator = 1
    new_word = ""
    word = input("Write a word to manipulate: ")

    for i, _ in enumerate(word):
        new_word += word[i] * iterator
        if i != len(word) - 1:
            new_word += "-"
        iterator += 1

    print(new_word)


def isogram():
    """
    Checks if a word is a isogram.
    """       
    no_match = False
    word = input("Write a word to check if it is an isogram: ").lower()

    for letter in word:
        no_match = word.count(letter) > 1

    answer = "No Match" if no_match else "Match" 
    print(answer)   


def contains_string():
    """
    Checks if one string contains another.
    """    
    first_word = input("Write the first word: ")
    second_word = input("Write the second word: ")

    match = second_word in first_word

    answer = "Match" if match else "No match" 
    print(answer)  


def contains_all_numbers():
    """
    Checks how many times a number needs to be multiplied with 2 to contain all numbers (0123456789).
    """    
    print("Firstly write a number to multiply with 2 secondly write how many times it should happen. ")
    numbers = "1234567890"
    did_not_contain_numbers = True
    iteration = 0
    result = 0

    first_number = input("Write the first number: ")
    second_number = input("Write the second number: ")

    while iteration < int(second_number):

        for num in numbers:
            if num in str(first_number):
                result += 1

        first_number = int(first_number) * 2

        if result == 10:
            print(iteration)
            did_not_contain_numbers = False
            break
        
        result = 0
        iteration += 1

    if did_not_contain_numbers:
        print("-1")

        
def replace_tab_with_space():
    """
    Replace tabs in sentences with whitespaces.
    """
    input_sentence = input("Write a sentence containing at least on tab: ")
    new_sentence = ""

    for letter in input_sentence:
        if letter == "\t":
            new_sentence = input_sentence.replace("\t", "   ")
            print(new_sentence)

def concat_names():
    """
    Concatenate names.
    """
    print("Enter two names so I can concatenate them: ")

    new_name = ""
    vowels = "aeiouy"
    first_name = input("Enter the first name: ").lower()
    second_name = input("Enter the second name: ").lower()

    for i, letter in enumerate(first_name):
        if letter in vowels:
            new_name = first_name[:i]
            break
    
    for i, letter in enumerate(second_name):
        if letter in vowels:
            new_name += second_name[i:]
            break

    print(new_name)

def point_counter():
    """
    Sum the points (numbers) from different player (letters).
    """
    print("Enter a string with each other letter and every other number: ")
    input_string = input("Enter string here: ")
    player_dict = {}
    player_points = ""

    for i, _ in enumerate(input_string):
        key_lower = input_string[i].lower()
        if i % 2 == 0:
            if key_lower not in player_dict:
                player_dict[key_lower] = 0
            if input_string[i].isupper():
                player_dict[key_lower] -= int(input_string[i + 1])
            else:
                player_dict[key_lower] += int(input_string[i + 1])

    i = 0
    for player, points_per_player in player_dict.items():
        player_points += str(player) + " " + str(points_per_player)
        if i != len(player_dict) - 1:
            player_points += ", "
        i += 1
    print(player_points)

def backpack():
    """
    Allows the user to store items (strings) in a backpack (list). 
    The user can add (even on a specific place in the backpack),
    remove items, show items (even a item on a specific place) 
    and swap places on items in the backpack.
    """
    print("Welcome to the backpack function.")
    print("Commands:")
    print("---------------------------------------------------------------------------")
    print("inv - Prints all the items in the backpack.")
    print("inv pick 'your input' - Adds an item in the backpack.")
    print("inv drop 'your input' - Deletes an item from the backpack.")
    print("inv swap 'your input' 'your input' - Swaps places of the two items entered.")
    print("q - Quit program.")
    print("---------------------------------------------------------------------------")
    print("If you add a number in the end of your inv or pick  you will directly point at the value in that index.")
    
    bag = []
    user_input = ""

    while user_input != "q":
        user_input = input("Write a command: ")
        print(">>>" + user_input)
        user_input_list = user_input.split()
        first_element = user_input_list[0]
        last_element = user_input_list[-1] 

        if first_element == "inv":
            if(len(user_input_list) <= 2):
                # DISPLAY
                if last_element.isdigit():
                    if int(last_element) < len(bag):
                        print(str(bag[int(last_element)]) + " is at index " + last_element)
                    else:
                        print("There is no item on that index.")
                else:
                    print("There is " + str(len(bag)) + " items in the backpack. " +  str(bag))
            else:
                second_element = user_input_list[1]
                second_last_element = user_input_list[2]
                # SAVE
                if second_element == "pick":
                    if last_element.isdigit():
                        if int(last_element) < len(bag):
                            bag.insert(int(last_element), second_last_element)
                            print("I have added " + second_last_element + " at index " \
                                    + last_element + " in the backpack.")
                        else:
                            print("You can not add to that index.")
                    else:
                        bag.append(last_element)
                        print("I have added " + last_element + " in the backpack.")
                # REMOVE
                elif second_element == "drop":
                    if last_element in bag:
                        bag.remove(last_element)
                        print("I have dropped " + last_element + " from the backpack.")
                    else:
                        print("The item is not in the backpack.")

                # SWAP        
                elif second_element == "swap":
                    if second_last_element in bag and last_element in bag and second_last_element != last_element:
                        first_item_index = bag.index(second_last_element)
                        second_item_index = bag.index(last_element)
                        
                        temp = bag[first_item_index]
                        bag[first_item_index] = bag[second_item_index]
                        bag[second_item_index] = temp

                        print("I have now swapped places on " + second_last_element + " and " + last_element)
                    else:
                        print("Either you have chosen the same item twice or the items does't exist in backpack.")
        
def word_scrambler():
    """
    Scramble the letters in a word.
    """
    user_input = input("Write a word to scramble: ")

    user_input_list = list(user_input)
    random.shuffle(user_input_list)
    scrambled_word = ''.join(user_input_list)
    print(scrambled_word)

def anagram():
    """
    Check if two words are anagrams.
    """
    print("Enter two words and I'll check if they are anagrams: ")
    first_word = input("First word: ")
    second_word = input("Second word: ")

    if(sorted(first_word.lower()) == sorted(second_word.lower())):
        print("Match")
    else:
        print("No match")

def acronym():
    """
    Takes a name and put all capital letters into an acronym.
    """
    acronym_list = []
    user_input = input("Write a name and I'll make an acronym: ")

    for char in user_input:
        if char.isupper():
            acronym_list.append(char)

    acroym = ''.join(acronym_list)
    print(acroym)

def filter_higher_than_ten():
    """
    Filter the numbers so it only keeps number higher than 10
    """
    user_input = input("Write a sequence of numbers: ")
    number_list = user_input.split(" ")

    number_list_int = list(map(int, number_list))

    def higher_than_ten(n):
        '''Return all numbers higher than 10'''

        return n > 10

    result = list(filter(higher_than_ten, number_list_int))

    print(result)

def grade():
    """
    This function will return a grade when given the max points and the users points.
    """
    max_points = input("What is the max points: ")
    pupil_points = input("What is the pupil's points: ")

    max_p = int(max_points)
    pup_p = float(pupil_points)

    if pup_p >= (max_p * 0.9):
        print("A")
    elif pup_p >= (max_p * 0.8):
        print("B")
    elif pup_p >= (max_p * 0.7):
        print("C")
    elif pup_p >= (max_p * 0.6):
        print("D")
    elif pup_p < (max_p * 0.6):
        print("F")


def string_content():
    """
    This function checks if a string starts with another string, contains another one and ends with another string.
    """
    first_string = input("Write your first word: ")
    string_start = input("Write another string to check if your first string starts with this string: ")
    string_contains = input("Write another string to check if your first string contains this string: ")
    string_end = input("Write another string to check if your first string ends with this string: ")
    #result = False
    #result = text.startswith('Python is ')

    if first_string.startswith(string_start) and string_contains in first_string and first_string.endswith(string_end):
        print("Match")
    else:
        print("No Match")

        


 
