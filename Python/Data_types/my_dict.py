my_dict = {"name": "John"}
print(my_dict.values() is my_dict.values())
print(my_dict.values() == my_dict.values()) #The output will be false because the two calls to my_dict.values() return different view objects.
# The values() method returns a view object that displays a list of all the values in the dictionary.
# The view object is dynamic and reflects any changes made to the dictionary.
print(my_dict.values() is not my_dict.values()) #The output will be true because the two calls to my_dict.values() return different view objects.