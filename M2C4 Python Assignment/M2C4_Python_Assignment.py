# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

from decimal import Decimal

my_list = ["Grease", "It", "Titanic", "Troya", "Wonka"]
my_tuple = ("air", "water", "fire", "earth")
my_float = 99.50
my_integer = 2025
my_decimal = Decimal('67.95')
my_dict = {
    1: "Python", 
    2: "JavaScript", 
    3: "SQL"
}


# Exercise 2: Round your float up.

import math

rounded_float = math.ceil(my_float)


# Exercise 3: Get the square root of your float.

sqrt_float = math.sqrt(my_float) 


# Exercise 4: Select the first element from your dictionary.

first_pair = list(my_dict.items())[0] # (1, "Python")

first_key = list(my_dict.keys())[0] # 1

first_value = list(my_dict.values())[0] # "Python"


# Exercise 5: Select the second element from your tuple.

second_element = my_tuple[1] 


# Exercise 6: Add an element to the end of your list.

my_list.append("Alien")


# Exercise 7: Replace the first element in your list.

my_list[0] = "Armageddon" 


# Exercise 8: Sort your list alphabetically.

my_list.sort()  


# Exercise 9: Use reassignment to add an element to your tuple.

my_tuple += ("cyberspace",) 