# Dictionary Manipulation:
# Create a dictionary for a student record with name, age, grade, and subject.
# Print the student’s name and subject using both [] and .get().
# Add a new key "email" and update "grade" to a higher value.
# Remove the "age" key and print the final dictionary.

student = {
    "name": "John",
    "age": 20,
    "grade": "C",
    "subject": "Math"
}

print(student["name"])
print(student.get("subject"))

student["email"] = "john@example.com"
student["grade"] = "B"

print(student)

del student["age"]
print(student)

# Nested Dictionary:
# Create a nested dictionary for 3 employees with name, position, and salary.
# Print the second employee’s position.
# Increase all salaries by 10% using update().
# Print the updated dictionary.

employees = {
    "employee1": {
        "name": "John",
        "position": "Manager",
        "salary": 50000
    },
    "employee2": {
        "name": "Jane",
        "position": "Developer",
        "salary": 60000
    },
    "employee3": {
        "name": "Jim",
        "position": "Designer",
        "salary": 55000
    }
}

print(employees["employee2"]["position"])

for employee in employees:
    employees[employee]["salary"] = employees[employee]["salary"] * 1.1

print(employees)

# Set Operations:
# Create two sets: frontend_devs and backend_devs.
# Find developers who are in both sets.
# Find developers who are only in frontend_devs but not in backend_devs.
# Merge both sets into a new set and print the result.

frontend_devs = {"John", "Jane", "Jim"}
backend_devs = {"Jim", "Jane", "Alice"}

print(frontend_devs.intersection(backend_devs))
print(frontend_devs.difference(backend_devs))
print(frontend_devs.union(backend_devs))

# Set Manipulation:
# Create a set of your favorite 5 numbers.
# Remove the largest number.
# Add two new numbers.
# Check if a specific number (e.g., 7) exists in the set.

numbers = {1, 2, 3, 4, 5}
numbers.remove(max(numbers))
numbers.add(6)
numbers.add(7)
print(7 in numbers)


# Dictionary Copying & Modification:
# Create a dictionary car with brand, model, and year.
# Copy it into car2 and change year in car2 without affecting car.
# Print both dictionaries to confirm they are independent copies.

car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

car2 = car.copy()
car2["year"] = 2021
print(car, car2)

