
#Holy moly, because the class's average was super low on the test, the teacher just added a curve for the test grades! 😭

#Create a grades.py program that checks whether a grade is above or below 55.

#Start by creating a variable called grade and give it a value between 0-100.

#Write a if/else statement for the following:

  #  If grade is greater than or equal to 55, then print "You passed."
   # Else, print "You failed."

#After you run the code, change grade's value and rerun it. Do this a few times to make sure it's working as intended.


# grade = 40
# if grade >= 55:
#      print("You passed")
# else:
#      print("You failed")
     
#Relational Operators

#A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values:

   # == equal to
  #  != not equal to
  #  > greater than
  #  < less than
  #  >= greater than or equal to
  #  <= less than or equal to

# Elif

#One or more elif statements (short for "else if") can be optionally added in between the if and else to provide additional condition(s) to check. Sometimes two is simply not enough.

#USE CASES:

#In chemistry, pH is a scale used to specify the acidity or basicity of a liquid. 🧪

#Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

#First, create a ph variable and ask the user for a value between 0 and 14.

#Write an if, elif, else statement that:

  #  If ph is greater than 7, output "Basic".
   # If ph is less than 7, output "Acidic".
    #Else, output "Neutral".


# ph = int(input("What is the pH level: "))

# if ph < 0 or ph > 14:
#     print("Invalid! Please enter a value between 0 and 14.")
# elif ph > 7:
#     print("Basic")
# elif ph < 7:
#     print("Acidic")
# else:  # ph == 7
#     print("Neutral")

#Working with factorials

# def fact(n):
#  if n == 0:
#     return 1
#  else:
#     return n * fact(n-1)
# result =fact(5)
# print(result)

#Working with an arithmetic calculator

num1 = float(input("Enter the first number: "))
operator = input("Enter operator i.e (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
     print("Error!, cannot divide a number by zero")
    else:
     print(num1 / num2)