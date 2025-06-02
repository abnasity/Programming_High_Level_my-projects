#Examples of intergers
nums = (5 + 5)
print(nums)


#Examples of floats
num = 50.7
nums = 50.9 + 50.8
total = num + nums
print(f"sum {total}")

# Basic Arithmetic
a = 5 + 3      # 8
b = 10 - 4     # 6
c = 4 * 7      # 28
d = 20 / 4     # 5.0 (returns float)

# Floor Division
e = 20 // 3    # 6 (ignores remainder)

# Modulus (Remainder)
f = 20 % 3     # 2

# Exponentiation
g = 2 ** 3     # 8 (2 to the power of 3)

print(f"Sum: {a}, Power: {g}, Division: {d}")

# USING NUMBERS IN REAL WORL SCENARIOS
# average score
scores = [80, 90, 75, 95]
average = sum(scores) / len(scores)
print("Average Score:", average)

# convert celsius to fareneheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)

# calculate area of a circle
import math
radius = 5
area = math.pi * (radius ** 2)
print("Area of Circle:", area)

# Time Conversion
def seconds_to_hours(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours} hours, {minutes} minutes, {remaining_seconds} seconds"
