programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
# print(programming_dictionary["Bug"])

#  Adding item in a dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# initiating empty dictionnary

programming_dictionary2 = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Editing dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# print(programming_dictionary)

# Looping through  a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# nesting
capitals = {
    "France": "paris",
    "Germany": "Berlin"
}

# Nesting a list in Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"city_looking_to_visit": {"Berlin", "Hamburg", "Stuttgart"}, "total": 5}

}

print(travel_log)

# nesting dictionary inside a list
travel_log_list = {
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {"country": "Germany",
     "city_looking_to_visit": {"Berlin", "Hamburg", "Stuttgart"},
     "total": 5
     }

}
