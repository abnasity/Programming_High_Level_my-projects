
# Examples of Tuples in python
Phones = ('Samsung', 'Iphone', 'Infinix', 'Tecno', 'X-tigi', 'Nokia')
Tea_Factories = ('Kapset', 'Chemalal', 'Stegro', 'Kapkoros', 'Motigo')
imei = ('356789123456789', '356789123456788', '356789123456787', '356789123456786', '356789123456785')
products = ('Laptop', 'Phone', 'Tablet', 'Smart Watch', 'Smart TV')
customers = ('Calvin', 'John', 'Jane', 'Doe', 'Alice')

# Creating tuples
t = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (1, "hello", True)

# single = (42,)   # The comma is required!
single = (42,)   # The comma is required!


# Accessing elements
print(t[0])  # Output: 1
print(t2[1])  # Output: 'b'

# without parentheses
t4 = 1, 2, 3  # This is also a tuple

# looping through a tuple
for item in t3:
    print(item)
    
# Tuple unpacking
a, b, c = t
print(a)  # Output: 1
print(b)  # Output: 2
person = ("Alice", 30)
name, age = person
print(name)  # Alice
print(age)   # 30

# Using asterisk for unpacking
def unpack_tuple(t):
    a, b, *rest = t
    return a, b, rest
result = unpack_tuple((1, 2, 3, 4, 5))
print(result)  # Output: (1, 2, [3, 4, 5])