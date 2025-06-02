# Examples of lists in python
oranges = ['banana', 'apple', 'bitruit']
vehicles = ['car', 'bus', 'motorcycle', 'bicycle']
cars = ['Toyota', 'Honda', 'Ford', 'Chevrolet']
clubs = ['Manchester United', 'Chelsea', 'Arsenal', 'Liverpool']
laptops = ['Dell', 'HP', 'Lenovo', 'Apple']

#lists with mixed data types
mixed_list = ['John', 25, 5.9, True, None, ['nested', 'list'], {'key': 'value'}]

#lists with different data types
different_data_types = [42, 3.14, 'Hello', True, None, ['nested', 'list'], {'key': 'value'}]

# A simple list of student names
students = ["Alice", "Bob", "Charlie"]

#  Accessing elements
print(students[0])  # Output: Alice

# Adding an element
students.append("Diana")

# Removing an element
students.remove("Bob")

# Updating an element
students[1] = "Carlos"  # Replaces Charlie with Carlos

# Looping through a list
for student in students:
    print(student)
    
# A list of students, where each student is represented by a dictionary
students = [
    {"name": "Alice", "grades": [85, 90, 88]},
    {"name": "Bob", "grades": [75, 80, 70]},
    {"name": "Charlie", "grades": [95, 92, 96]}
]

# Print each student's average grade
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}'s average grade: {avg}")
    
# Common list operations
# 1. Creating a list
numbers = [1, 2, 3, 4, 5]

# 2. Accessing elements


# Length of list
print(len(numbers))  # 5

# Slicing
print(numbers[1:4])  # [2, 3, 4]
