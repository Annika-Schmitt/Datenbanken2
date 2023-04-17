import sqlite3

# Connecting to a new sqlite database
connection = sqlite3.connect("bookstore.db")

# Creating a new cursor object
cursor = connection.cursor()

# Read data
print("Book Table: ")
data = cursor.execute('''SELECT * FROM Book''')
for row in data:
    print(row)

# Further queries:
# Gebe alle Titel aus, deren AutorID mit 'CF' anfängt
print("Authors starting with CF")
data = cursor.execute('''SELECT Title FROM Book WHERE AuthorID LIKE "CF%"''')
for row in data:
    print(row)

# Gebe alle Inhalte der Books Tabelle in alphabetisch sortierte Reihenfolge nach BookID aus
print("Ordering the contents of Books table")
data = cursor.execute('''SELECT * FROM Book ORDER BY BookID''')
for row in data:
    print(row)

# Gebe alle Buchtitel des Genre 'Fiction' aus
print("Titles that belong to Genre = Fiction")
data = cursor.execute('''SELECT Title FROM Book INNER JOIN Info ON Book.BookID = Info.BookID''')
for row in data:
    print(row)

# Welcher Verlag existiert am längsten ('Year Established’)
print("Publishing House with min. Year Established")
data = cursor.execute('''SELECT "Publishing House", MIN("Year Established") FROM Publisher''')
for row in data:
    print(row)


connection.commit()
connection.close()
