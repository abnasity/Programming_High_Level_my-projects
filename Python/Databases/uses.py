
#  How to Use a Database in Python?

# In Python, databases are used to store, manage, and query data efficiently. Python can interact with both SQL and NoSQL databases using various libraries. Whether you're building a small application with SQLite or a large, scalable system with MongoDB or MySQL, Python has the tools to connect to, manipulate, and query databases effectively.



# *************Example: Using SQLite in Python (for SQL-based databases):

# SQLite is a lightweight, file-based database that's built into Python, so it doesn't require any external installation. Here’s a simple example of how to use it.
import sqlite3
conn = sqlite3.connect('mydatabase.db')  # Creates or opens a database file
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY, 
                      name TEXT, 
                      age INTEGER)''')
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
conn.commit()  # Commit changes
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()






#This code:

    # Creates an SQLite database file mydatabase.db if it doesn't exist.

    # Creates a users table with id, name, and age.

    # Inserts data into the table.

    # Queries and prints the stored data.
    
    
# ***************Example: Using MongoDB in Python (for NoSQL-based databases):

# Here’s how you can interact with a NoSQL database like MongoDB using the pymongo library.









# This code:

#     Connects to a local MongoDB server.

#     Creates a users collection in the mydatabase database.

#     Inserts a document and retrieves it.



# 🔹 Types of Database Queries

# Once you've connected to a database, you'll typically use queries to interact with it. Queries allow you to:

#     Insert data into tables or collections.

#     Retrieve data based on certain conditions (like filtering by name or age).

#     Update existing data (changing a user's age, for example).

#     Delete data (removing a record from the database).