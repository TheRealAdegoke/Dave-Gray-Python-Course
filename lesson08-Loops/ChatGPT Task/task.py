# While Loop Task - Countdown Timer ⏳
# Write a while loop that counts down from 10 to 1.
# When it reaches 3, print "Almost there!" but continue counting.
# When it reaches 1, print "Blast off!".

value = 10
while value >= 1:
    if value == 3:
        print("Almost there!")
    elif value == 1:
        print("Blast off!")
    value -= 1

# While Loop Task - Sum of Even Numbers
# Ask the user for a number (n).
# Use a while loop to sum only the even numbers from 1 to n.
# Print the result.

user_input = int(input("Enter a number: "))
sum = 0
while user_input >= 1:
    if user_input % 2 == 0:
        sum += user_input
    user_input -= 1
print(sum)

# For Loop Task - Reverse a Word 🔄
# Ask the user for a word.
# Print each letter of the word in reverse order using a for loop.

user_input = input("Enter a word: ")
for letter in user_input[::-1]:
    print(letter)

# For Loop Task - Multiplication Table 🔢
# Ask the user for a number (n).
# Print the multiplication table for n from 1 to 10.

user_input = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{user_input} * {i} = {user_input * i}") 

# Nested Loop Task - Combinations 🎲
# Create a list of colors = ["red", "blue", "green"].
# Create a list of shapes = ["circle", "square", "triangle"].
# Use nested loops to print all possible color-shape combinations.

colors = ["red", "blue", "green"]
shapes = ["circle", "square", "triangle"]
for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")

# Range Task - Print Odd Numbers 🧮
# Use a for loop with range() to print all odd numbers from 1 to 20.

for i in range(1, 21):
    if i % 2 != 0:
        print(i)
