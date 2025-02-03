# Write a program that takes two numbers as input and prints their sum, difference, product, and quotient.

first_number = 10
second_number = 20

first_input_number = input('Enter first number: ')
second_input_number = input('Enter second number: ')

print(first_number + second_number)
print(int(first_input_number) + int(second_input_number))

# Above I gave two ways on how the first question can be solved.

# Ask the user for their age and check if they are old enough to vote (18 or older). Print "You can vote!" or "You are too young to vote."

user_age = input("Enter your age: ")

if int(user_age) >= 18:
    print("You can vote!")
else :
    print("You are too young to vote.")

# Above is the solution to question two

# Create a program that asks for a user's age and country. Print "Eligible" if the user is at least 18 and from a specific country (e.g., USA), otherwise print "Not eligible".

user_age = input("Enter your age: ")
user_country = input("Enter your country: ")

if int(user_age) >= 18 and user_country:
    print("Eligible to vote in " + user_country)
else:
    print("Not eligible")

# Above is the solution to question three

# Write a program that takes a number as input and prints "Even" if it's even and "Odd" if it's odd, using a ternary operator.

user_number = input("Enter a number: ")

if int(user_number) % 2 == 0:
    print("Even")
else:
    print("Odd")

# Above is the solution to question four

#  Evaluate and print the result of this expression: result = 10 + 2 * 3 - 4 / 2 ** 2

result = 10 + 2 * 3 - 4 / 2 ** 2
print(result)
