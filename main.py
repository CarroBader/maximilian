"""
This program will present the user with some menu choices were they can get information
from Maximilian the turtle.
"""

import marvin
import emission_functions

def start_maximilian():
    """
    Starts Maximilians menu.
    """
    maximilian_image = r"""
                                        ___-------___
                                    _-~~             ~~-_
                                _-~                    /~-_
                /^\__/^\         /~  \                   /    \
            /|  O|| O|        /      \_______________/        \
            | |___||__|      /       /                \          \
            |          \    /      /                    \          \
            |   (_______) /______/                        \_________ \
            |         / /         \                      /            \
            \         \^\         \                  /               \     /
                \         ||           \______________/      _-_       //\__//
                \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                    ~-----||====/~     |==================|       |/~~~~~
                    (_(__/  ./     /                    \_\      \.
                            (_(___/                         \_____)_)
    """


    """
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(maximilian_image)
        print("Hi, I'm Maximilian the turtle. I know it all. What can I do you for?")
        print("1) Greet Maximilian the turtle.")
        print("2) Convert temprature (C -> F).")
        print("3) Word multiplier.")
        print("4) Sum and average.")
        print("5) Compare numbers.")
        print("6) Character multiplier.")
        print("7) Check if it is an isogram.")
        print("8) Check if a string contains another string.")
        print("9) Multiply your way to 0123456789.")
        print("10) Replace Tab with 3 whitespaces.")
        print("11) Concatenate names.")
        print("12) Count score for players.")
        print("13) To enter the backpack function")
        print("14) Scramble word")
        print("15) Check if words are anagram")
        print("16) Create an acronym")
        print("17) Filter and only shows number higher than 10")
        print("18) Get grade from points")
        print("19) Check strings content")
        print("20) Search in emission with country")
        print("21) Search in emission with year")
        print("22) Search in emission with year per capita")
        print("q) Quit.")

        choice = input("--> ") 

        # Choice 1 --- Greet bot
        if choice == "1":
            marvin.greeting()

        # Choice 2 --- Temprature Converter 
        elif choice == "2":
            marvin.convert_C_to_F()

        # Choice 3 -- Word multiplyer
        elif choice == "3":
            marvin.word_multiplyer()

        # Choice 4 -- Sum and Average
        elif choice == "4":
            marvin.sum_and_avarage()

        # Choice 5 -- Compare numbers
        elif choice == "5":
            marvin.compare_numbers()

            # Choice 6 -- Character multiplier
        elif choice == "6":
            marvin.character_multiplyer()

            # Choice 7 -- Check if it iss an isogram
        elif choice == "7": 
            marvin.isogram()

        # Choice 8 -- Check if a string contains another string
        elif choice == "8":
            marvin.contains_string()

        # Choice 9 -- 0123456789 
        elif choice == "9":
            marvin.contains_all_numbers()

        # Choice 10 -- Replace Tab with 3 whitespaces
        elif choice == "10":
            marvin.replace_tab_with_space()

        # Choice 11 -- Concatenate names 
        elif choice == "11":
            marvin.concat_names()  

        # Choice 12 -- Count score for players       
        elif choice == "12":
            marvin.point_counter()  

        # Choice inv -- Backpack function
        elif choice == "13":
            marvin.backpack()

        # Choice 14 -- Scramle word 
        elif choice == "14":
            marvin.word_scrambler()

        # Choice 15 -- Check if words are anagrams
        elif choice == "15":
            marvin.anagram()

        # Choice 16 -- Create an acronym
        elif choice == "16":
            marvin.acronym()

        # Choice 17 -- Filter numbers higher than 10
        elif choice == "17":
            marvin.filter_higher_than_ten()

        # Choice 18 -- Grade 
        elif choice == "18":
            marvin.grade()

         # Choice 19 -- String content 
        elif choice == "19":
            marvin.string_content()

        # Choice 20 -- Search in emission with country
        elif choice == "20":
            emission_functions.search_country()

        # Choice 21 -- Search in emission with year
        elif choice == "21":
            emission_functions.search_year()

        # Choice 22-- Search in emission with year per capita
        elif choice == "22":
            emission_functions.search_year_capita()

            # Chice q -- Quit search_year() 
        elif choice == "q":
            print("Awesome Possum, see you next time!")
            break    

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    start_maximilian()
