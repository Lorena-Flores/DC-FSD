# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

my_string = "Hello world!"
my_number = 2025
my_list = ["Australia", 100, False, 24.50, 1/5]
my_boolean = True

# Exercise 2: Use an Index to grab the first 3 letters in your string, store that in a variable.

fist_letters = my_string[:3]

# Exercise 3: Use an index to grab the first element from your list.

first_element = my_list[0]

# Exercise 4: Create a new number variable that adds 10 to your original number.

new_number = my_number + 10

# Exercise 5: Use an index to get the last element in your list.

last_element = my_list[-1]

# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')

# Exercise 7: Get the first word from your string using indexes. 
# Use the upper function to transform the letters into uppercase. 
# Create a new string that takes the uppercase word and the rest of the original string.

first_word = my_string[:5]
first_word_upper = first_word.upper()
new_string = first_word_upper + my_string[5:]

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

print(f"We are on the year {my_number}!")

# Exercise 9: Print “hello world”.

print("hello world")

# Exercise 10: Create a string that contains the word 'Hola'. 
# Using the keyword in the search method or index, find and select 'Hola' in your string. 
# And using the replace function, replace 'Hola' in your string with 'adiós'.

string_two = "Ayer publicaron la revista Hola"

search_method = string_two.find("Hola")
print(string_two[27:])

string_three = string_two.replace("Hola", "adiós")
print(f"{string_three}")