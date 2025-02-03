import math

# User Greeting Formatter
user_first_name = input("Enter your first name: ").strip()
user_last_name = input("Enter your last name: ").strip()

print("Welcome", user_first_name + " " + user_last_name + "!")

# Sentence Formatter
user_sentence = input("Enter a sentence: ").strip()

print(user_sentence.upper())
print(user_sentence.lower())
print(user_sentence.title())

# Math Operations on Numbers
# Ask the user for two numbers.
# Print the sum, difference, product, and quotient.
# Also, print the square root of the first number using math.sqrt().

user_first_number = int(input("Enter your first number: "))
user_second_number = int(input("Enter your second number: "))

print(user_first_number + user_second_number)
print(user_first_number - user_second_number)
print(user_first_number * user_second_number)
print(user_first_number / user_second_number)
print(math.sqrt(user_first_number))

# Boolean Evaluation
# Ask the user to input a word.
# Print whether the word starts with "A" (case insensitive) using startswith().
# Print whether the word is longer than 5 characters.

user_word = input("Enter a word: ")

print(user_word.startswith("A"))
print(len(user_word) > 5)

# Price Menu Formatter
# Create a simple menu with three food items and their prices.
# Use .ljust() and .rjust() to align the names and prices neatly.

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$2".rjust(4))
print("Burger".ljust(16, ".") + "$5".rjust(4))
print("Pizza".ljust(16, ".") + "$8".rjust(4))