# Example of a string in python
greeting = "Hello, World"

# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = """This is a
multiline string."""

# Common string operations
# Concatenation
name = "Alice"
greeting = "Hello, " + name

# Repitition
repeat = "Ha" * 3  # Output: "HaHaHa"

# Indexing and slicing
first_char = greeting[0]  # 'H'
second_char = greeting[1]  # 'e'
substring = greeting[7:12]  # 'World'

# String methods
length = len(greeting)  # Length of the string
s = "  Hello World  "

s.lower()        # '  hello world  '
s.upper()        # '  HELLO WORLD  '
s.strip()        # 'Hello World'
s.replace("World", "Python")  # '  Hello Python  '
s.split()        # ['Hello', 'World']
"hello" in s     # True


