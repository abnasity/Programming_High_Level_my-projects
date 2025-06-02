
# Examples of dictionaries in python
Example ={
      "key1": "value1",
       "key2": "value2"
       }

# Example of a dictionary with mixed data types

movie = {   
    "title": "Inception",
    "year": 2010,
    "director": "Christopher Nolan",
    "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
    "rating": 8.8
}


person = {
    "name" : "Alice",
    "Age" : 24,
    "City" : "New York"
}

Car = {
    "Brand" : "Mercedes",
    "Year" : 2009,
    "FUel" : "Diesel",
}


phone = {
     "Brand" : "Nokia",
     "Model" : "3310",
        "Year" : 2000,
}


imei = {
    digits 
    
    
    
}

# Creating a dictionary
student = {
     "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}


# Accessing values
print(student["name"])  # Output: Alice













my_dict = {"name": "John"}
print(my_dict.values() is my_dict.values())
print(my_dict.values() == my_dict.values()) #The output will be false because the two calls to my_dict.values() return different view objects.
# The values() method returns a view object that displays a list of all the values in the dictionary.
# The view object is dynamic and reflects any changes made to the dictionary.
print(my_dict.values() is not my_dict.values()) #The output will be true because the two calls to my_dict.values() return different view objects.




fruit_stores = {'apple': {'store1': 1.0, 'store2': 1.5},
               'banana': {'store1': 2.0, 'store2': 1.8}
         }
#Write a python function that takes a nested dictionary where the inner dictionaries represent items and their prices in different stores. The function should return a new dictionary where the keys are the items and the store with the lowest price as the value. For example, the fruits_stores nested dictionary above should return {'apple': 'store1', 'banana': 'store2'}.
def find_lowest_price_store(fruit_stores):
    lowest_price_stores = {}
    for fruit, stores in fruit_stores.items():
        lowest_store = min(stores, key=stores.get)
        lowest_price_stores[fruit] = lowest_store
    return lowest_price_stores
print(find_lowest_price_store(fruit_stores)) #Output: {'apple': 'store1', 'banana': 'store2'}


fruits = ['apple', 'banana', 'apple', 'cherry']

#Given a list of strings, write a python function that returns a dictionary where the keys are the strings and the values are the number of times each string appears in the list. For example, the fruits list above should return {'apple': 2, 'banana': 1, 'cherry': 1}.
def count_fruits(fruits):
    fruit_count = {}
    for fruit in fruits:
        if fruit in fruit_count:
            fruit_count[fruit] += 1
        else:
            fruit_count[fruit] = 1
    return fruit_count
print(count_fruits(fruits)) #Output: {'apple': 2, 'banana': 1, 'cherry': 1}