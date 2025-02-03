# List Operations
# Create a list of five fruits.
# Print the first and last fruit using both positive and negative indexing.
# Add a new fruit to the end of the list and another at the beginning.
# Remove the second fruit from the list.
# Print the final list.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[0])
print(fruits[-1])
fruits.append("pineapple")
fruits.insert(0, "pear")
fruits.remove("banana")
print(fruits)

# List Sorting & Reversing
# Create a list of five random numbers.
# Print the sorted version without modifying the original list.
# Reverse the list in place.
# Sort the list in descending order.

random_numbers = [10, 9, 8, 7, 6, 4, 100, 30, 90, 20]

print(sorted(random_numbers))
random_numbers.reverse()
print(random_numbers)
random_numbers.sort()
print(random_numbers)
random_numbers.sort(reverse=True)
print(random_numbers)

# Tuple Unpacking
# Create a tuple with four elements: your name, age, country, and favorite color.
# Unpack the values into separate variables and print them.

person = ("John", 30, "USA", "blue")
name, age, country, favorite_color = person
print(name, age, country, favorite_color)

# Tuple Conversion
# Create a tuple of three programming languages.
# Convert it to a list, add another language, and convert it back to a tuple.
# Print the final tuple.

languages = ("Python", "Java", "C#")
languages = list(languages)
languages.append("JavaScript")
languages = tuple(languages)
print(languages)

# List Copying & Modification
# Create a list of three colors.
# Make three different copies of the list using .copy(), list(), and slicing [:].
# Modify only the first copy by adding a new color.
# Print all three lists to show that the other copies remain unchanged.

colors = ["red", "green", "blue"]
colors_copy = colors.copy()
colors_copy2 = list(colors)
colors_copy3 = colors[:]
colors_copy.append("yellow")
print(colors, colors_copy, colors_copy2, colors_copy3)
