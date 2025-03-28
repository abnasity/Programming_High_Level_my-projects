
# Modules are files containing a set of functions
#A file is named first then imported
#Naming a module:
#**module_name.function_name**
#i.e  separate by a dot
# 
# def greeting(my_name):
#     print("Hello" + my_name)
# import mymodule
# mymodule.greeting("Jonathan")


# student1 = {
#     "name" : "Abnas",
#     "Age" : 26,
#     "country" : "Kenya"
# }

# import mymodule
# q = mymodule.student1["Age"]
# print(q)

#Built in modules
# import platform
# a = platform.system()
# print(a)

#The dir() function
#Used to import all function belonging to a module.
#USE CASE:
# import platform
# a = dir(platform)
# print(a)

#The for function:
#Used to import specific parts from a module
#USE CASE:
#Syntax is from module_name import something
# from math import sqrt
# print(sqrt(16))
#importing multiple items
# from math import ceil, floor
# print(ceil(4.3))
# print(floor(4.3))

# from math import pi 
# print(pi)

def greeting(name):
 print("Hello" + name)

student1 = {
    "name" : "Abnas",
    "Age" : 25,
    "nationality" : "Kenyan" 
}
# from mymodule import student1
# print(student1["nationality"])
#OR
import mymodule
print(student1["Age"])



#Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
