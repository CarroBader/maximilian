"""
This file includes all functions that has to do with emission.
"""

import emission_data

def search_country():
    """
    This fuction lets the user search for countries in emission_data.
    """
    country = input("What country are you looking for? ")

    for key in emission_data.country_data:
        if country.lower() in key.lower():
            print(key)

def search_year():
    """
    This fuction lets the user search for CO2 after year.
    """
    print("The year we have data from are 1990, 2005 and 2017.")
    print("If you only want to see a specific amount of countrys add a number after the year.")
    print("Ex. 1990 10")
    user_input = input("What year would you like to know CO2 for? ")
    print(" ")

    if user_input == '1990' or (user_input.startswith('1990') and len(user_input) > 5):
        emission_dict = get_emission_dict('1990', 'country')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2005' or (user_input.startswith('2005') and len(user_input) > 5):
        emission_dict = get_emission_dict('2005', 'country')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2017' or (user_input.startswith('2017') and len(user_input) > 5):
        emission_dict = get_emission_dict('2017', 'country')
        print_country_emission_dict(emission_dict, user_input)  
    else:
        print("We do not have data for that year.")

def search_year_capita():
    """
    This fuction lets the user search for CO2 after year and sorts on capita.
    """
    print("The year we have data from are 1990, 2005 and 2017.")
    print("If you only want to see a specific amount of countrys add a number after the year.")
    print("Ex. 1990 10")
    user_input = input("What year would you like to know CO2 per capita for? ")
    print(" ")

    if user_input == '1990' or (user_input.startswith('1990') and len(user_input) > 5):
        emission_dict = get_emission_dict('1990', 'capita')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2005' or (user_input.startswith('2005') and len(user_input) > 5):
        emission_dict = get_emission_dict('2005', 'capita')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2017' or (user_input.startswith('2017') and len(user_input) > 5):
        emission_dict = get_emission_dict('2017', 'capita')
        print_country_emission_dict(emission_dict, user_input)  
    else:
        print("We do not have data for that year.")

def search_year_area():
    """
    This fuction lets the user search for CO2 after year and sorts on area.
    """
    print("The year we have data from are 1990, 2005 and 2017.")
    print("If you only want to see a specific amount of countrys add a number after the year.")
    print("Ex. 1990 10")
    user_input = input("What year would you like to know CO2 per area for? ")
    print(" ")

    if user_input == '1990' or (user_input.startswith('1990') and len(user_input) > 5):
        emission_dict = get_emission_dict('1990', 'area')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2005' or (user_input.startswith('2005') and len(user_input) > 5):
        emission_dict = get_emission_dict('2005', 'area')
        print_country_emission_dict(emission_dict, user_input)
    elif user_input == '2017' or (user_input.startswith('2017') and len(user_input) > 5):
        emission_dict = get_emission_dict('2017', 'area')
        print_country_emission_dict(emission_dict, user_input)  
    else:
        print("We do not have data for that year.")

def get_emission_dict(year, kind):
    """
    Return a dictionary with country and emisson as key/value pair.
    """
    emission_dict = {}
    if year == '1990':
        if kind == 'country':
            emission_dict = create_country_emission_dict(emission_data.emission_1990)
        elif kind == 'capita':
            emission_dict = create_capita_emission_dict(emission_data.emission_1990, year)
        elif kind == 'area':
            emission_dict = create_area_emission_dict(emission_data.emission_1990)
    if year == '2005':
        if kind == 'country':
            emission_dict = create_country_emission_dict(emission_data.emission_2005)
        elif kind == 'capita':
            emission_dict = create_capita_emission_dict(emission_data.emission_2005, year)
        elif kind == 'area':
            emission_dict = create_area_emission_dict(emission_data.emission_2005)
    if year == '2017':
        if kind == 'country':
            emission_dict = create_country_emission_dict(emission_data.emission_2017)
        elif kind == 'capita':
            emission_dict = create_capita_emission_dict(emission_data.emission_2017, year)
        elif kind == 'area':
            emission_dict = create_area_emission_dict(emission_data.emission_2017)

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

def create_capita_emission_dict(year_dict, year):
    """
    Creates the emisson per capita dictionary paired with country.
    """
    capita_emission_dict = {}
    calculated_capita = 0
    for emission_key, emission_val in year_dict.items():
        for country_key, country_val in emission_data.country_data.items():
            if emission_key == country_val['id']:
                population = country_val['population']
                if len(population) != 0:
                    if year == '1990':
                        capita = (emission_val * 1000000) /population[0]
                    elif year == '2005':
                        capita = (emission_val * 1000000)/population[1]
                    elif year == '2017':
                        capita = (emission_val * 1000000)/population[2]

            capita_emission_dict[capita] = country_key 

    return capita_emission_dict

def create_area_emission_dict(year_dict):
    """
     Creates the emisson per area dictionary paired with country.
    """
    area_emission_dict = {}
    for emission_key, emission_val in year_dict.items():
        for country_key, country_val in emission_data.country_data.items():
            if emission_key == country_val['id']:
                area_country = country_val['area']
                if area_country != 0:
                    area = (emission_val * 1000000)/(area_country * 100)
            area_emission_dict[area] = country_key 

    return area_emission_dict


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
            