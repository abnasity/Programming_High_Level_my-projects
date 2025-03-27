
#FUNCTIONS
#A function is a block of code which only runs when it is called


# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes") 

#Arguments also known as args are values passed when function is called
#A variable is inside the function definition

# def greet(name):
#   print("Hello", name)
#   print("How do you do")
  
# greet("Jack")

#Nested functions:
#This is a function defined within the body of another function, allowing it to access and modify variables from the outer function scope.
#this is a nested function example
# def calculator(operation):
#     def add(a ,b):
#         return a + b
    
#     def subtract(a ,b):
#         return a - b
    
#     def multiply(a ,b):
#         return a * b
    
#     def divide(a ,b):
#         return a / b
    
#     if operation == "add":
#         return add
    
#     elif operation == "subtract":
#         return subtract
    
#     elif operation == "multiply":
#         return multiply
    
#     elif operation == "divide":
#         return divide
#     else:
#         return"Invalid operation"
    
    
# result_add = calculator("add")(3,4)
# print(f"addition results:{result_add}")


#You can add an input and an operator to a function so the user can enter two numbers and perform arithmetic operations
#USE CASE:
def calculator(operaton):
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b
    
    if operation == "add":
        return add
    
    elif operation == "subtract":
        return subtract
    
    elif operation == "multiply":
        return multiply
    
    elif operation == "divide":
        return divide
    else:
        return"Invalid operation"
    
    
# # User input
#We use strip to ensure that the use can enter empty space without givine an error.
#We use lower() to ensure that the user can enter lowercase letters.
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# # Perform calculation
calculation = calculator(operation)
if calculation:
    result = calculation(a, b)
    print(f"Result: {result}")
else:
    print("Invalid operation")
    
    
    
 
  