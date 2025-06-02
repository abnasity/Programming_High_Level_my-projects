# Examples of sets in python

books = {'Encyclopaedia', 'Social studies', 'Maths'}

Teachers = {'Mufti', 'Rop', 'Daisy'}

students = {'Calvin', 'John', 'Jane', 'Doe', 'Alice'}

products = {'Laptop', 'Phone', 'Tablet', 'Smart Watch', 'Smart TV'}

imei = {'356789123456789', '356789123456788', '356789123456787', '356789123456786', '356789123456785'}


# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}

print(fruits)  # Output: {'banana', 'cherry', 'apple'} (no duplicates)

# Add an item
fruits.add("orange")

# Remove an item
fruits.remove("banana")

# Check if an item is in the set
print("apple" in fruits)  # True


# Loop through a set
for fruit in fruits:
    print(fruit)
    
# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of two sets
print(set1 | set2)   # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(set1 & set2)   # {3, 4}

# Difference
print(set1 - set2)   # {1, 2}

# Symmetric Difference (in either, but not both)
print(set1 ^ set2)   # {1, 2, 5, 6}

#  Real-World Example: Removing Duplicate Student Names
students = ["Alice", "Bob", "Charlie", "Alice", "Bob"]
unique_students = set(students)
print(unique_students)  # {'Charlie', 'Alice', 'Bob'}
# Real-World Example: Inventory Management
inventory = {"apple", "banana", "orange", "apple"}
print(inventory)  # {'banana', 'orange', 'apple'} (no duplicates)
# Real-World Example: Social Media Followers
followers = {"alice", "bob", "charlie", "alice"}
print(followers)  # {'charlie', 'alice', 'bob'} (no duplicates)





