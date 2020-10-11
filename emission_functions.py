"""
This file includes all functions that has to do with emission.
"""

import emission_data

def search_country():
    """
    This fuction lets the user search for countries in emission_data.
    """
    country = input("What country are you looking for? ")

    for key, val in emission_data.country_data.items():
        if country.lower() in key.lower():
            print(key)

# På föregående menyval, lägg till att användaren även kan skriva in hur många länder som ska skrivas ut i utskriften. 
# T.ex. 1990 10, då ska bara de 10 länder med mest utsläpp skrivas ut för år 1990. Om användaren enbart skriver in ett 
# år ska alla länder skrivas ut. Ni kan välja själva om ni vill räkna från 0 eller 1.

def search_year():
    """
    This fuction lets the user search for CO2 after year.
    """
    print("search_year")
    print("The year we have data from are 1990, 2005 and 2017.")
    print("If you only want to see a specific amout of countrys add a number after the year.")
    print("Ex. 1990 10")
    user_input = input("What year would you like to know CO2 for? ")
    print(" ")

    if user_input == '1990' or (user_input.startswith('1990') and len(user_input) > 5):
        emission_dict = get_country_emission('1990', 'country')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2005' or (user_input.startswith('2005') and len(user_input) > 5):
        emission_dict = get_country_emission('2005', 'country')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2017' or (user_input.startswith('2017') and len(user_input) > 5):
        emission_dict = get_country_emission('2017', 'country')
        print_country_emission_dict(emission_dict, user_input)  
    else:
        print("We do not have data for that year.")


# Användaren ska skriva in ett år och få utskriften varje lands utsläpp per capita, sortera it storleksordning. 
# Det ska även gå att skriva in hur många länder som ska skriva ut. Om användaren enbart skriver in ett år ska alla länder skrivas ut.

def search_year_capita():
    """
    This fuction lets the user search for CO2 after year and sorts on capita.
    """
    print("search_year_capita")
    print("The year we have data from are 1990, 2005 and 2017.")
    print("If you only want to see a specific amout of countrys add a number after the year.")
    print("Ex. 1990 10")
    user_input = input("What year would you like to know CO2 per capita for? ")
    print(" ")

    if user_input == '1990' or (user_input.startswith('1990') and len(user_input) > 5):
        emission_dict = get_country_emission('1990', 'capita')
        print_country_emission_dict(emission_dict, user_input)
    # elif user_input == '2005' or (user_input.startswith('2005') and len(user_input) > 5):
    #     emission_dict = get_country_emission('2005')
    #     print_country_emission_dict(emission_dict, user_input)
    # elif user_input == '2017' or (user_input.startswith('2017') and len(user_input) > 5):
    #     emission_dict = get_country_emission('2017')
    #     print_country_emission_dict(emission_dict, user_input)  
    else:
        print("We do not have data for that year.")


def get_country_emission(year, kind):
    """
    Return a dictionary with country and emisson as key/value pair.
    """
    emission_dict = {}
    if year == '1990':
        if kind == 'country':
            print("Country")
            emission_dict = create_country_emission_dict(emission_data.emission_1990)
        elif kind == 'capita':
            print("Capita")
            emission_dict = create_capita_emission_dict(emission_data.emission_1990)
    # if year == '2005':
    #     if kind == 'country':
    #         emission_dict = create_country_emission_dict(emission_data.emission_1990)
    #     elif kind == 'capita':
    #         emission_dict = create_capita_emission_dict(emission_data.emission_1990)
    # if year == '2017':
    #     if kind == 'country':
    #         emission_dict = create_country_emission_dict(emission_data.emission_1990)
    #     elif kind == 'capita':
    #         emission_dict = create_capita_emission_dict(emission_data.emission_1990)

    # for key, val in emission_dict.items():
    #     print(val, key)
    return emission_dict

def create_country_emission_dict(year_dict):
    """
    Creates the emisson dictionary paired with country.
    """
    country_emission_dict = {}
    for emission_key, emission_val in year_dict.items():
        for country_key, country_val in emission_data.country_data.items():
            if emission_key == country_val['id']:
                country_emission_dict[emission_val] = country_key
    return country_emission_dict

def create_capita_emission_dict(year_dict):
    """
    Creates the emisson per capita dictionary paired with country.
    """
    print("create_capita_emission_dict")
    capita_emission_dict = {}
    for emission_key, emission_val in year_dict.items():
        for country_key, country_val in emission_data.country_data.items():
            if emission_key == country_val['id']:
                capita_emission_dict[emission_val] = country_key
                population = country_val['population']
                #print(country_key + " " + str(population))
                if len(population) != 0:
                    #print("Country: " + country_key + " Emisson val: " + str(emission_val) + " Population: " + str(population[0]))
                    capita = emission_val/population[0]
                    #print(country_key + " " + str(capita))
                    capita_emission_dict[capita] = country_key 

    return capita_emission_dict

def print_country_emission_dict(emission_dict, user_input):
    """
    Print the country and emission dict.
    """
    if len(user_input) > 5:
        amount = int(user_input[5:])
        for key, val  in sorted(emission_dict.items(), reverse=True)[:amount]:
            print(val + ": " + str(key))
    else:
        for key, val  in sorted(emission_dict.items(), reverse=True):
            print(val + ": " + str(key))