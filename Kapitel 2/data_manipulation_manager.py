import sqlite3

# Connecting to a new sqlite database
connection = sqlite3.connect("bookstore.db")

# Creating a new cursor object
cursor = connection.cursor()

# Update Data
cursor.execute('''UPDATE Book SET Title = 'Thatchwork Cottage 2' WHERE BookID = "TC188"''')

# Display data
print("Books Table: ")
data = cursor.execute('''SELECT * FROM Book WHERE Title = "'Thatchwork Cottage 2"''')
for row in data:
    print(row)

connection.commit()
connection.close()
