import sqlite3

# Connecting to a new sqlite database
connection = sqlite3.connect("bookstore.db")

# Creating a new cursor object
cursor = connection.cursor()

# Read data
print("Books Table: ")
data = cursor.execute('''SELECT * FROM Books''')
for row in data:
    print(row)

connection.commit()
connection.close()
