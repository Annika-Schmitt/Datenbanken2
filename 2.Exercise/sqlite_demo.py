import sqlite3
import pandas as pd

# Connect to a new sqlite database
connection = sqlite3.connect("bookstore.db")

# Create a new cursor object
cursor = connection.cursor()

# Create new table "book"
table = """ CREATE TABLE IF NOT EXISTS Book (
            BookID TEXT PRIMARY KEY,
            Title TEXT,
            AuthorID TEXT,
            FOREIGN KEY (authorID) 
               REFERENCES Author (authorID) 
                  ON DELETE CASCADE 
        ); """
cursor.execute(table)
connection.commit()

# Insert data into table (one row only)
cursor.execute("""INSERT INTO Book (BookID, Title, AuthorID)
                    VALUES
                        ("BB196", "Ballinby Boys", "AM329");
               """)

# Insert multiple rows into new tables
book_csv = pd.read_csv('data//book.csv', sep=";")
book_csv.to_sql('Book', connection, if_exists='replace', index=False)

author_csv = pd.read_csv('data//author.csv', sep=";")
author_csv.to_sql('Author', connection, if_exists='replace', index=False)

publisher_csv = pd.read_csv('data//publisher.csv', sep=";")
publisher_csv.to_sql('Publisher', connection, if_exists='replace', index=False)

info_csv = pd.read_csv('data//info.csv', sep=";")
info_csv.to_sql('Info', connection, if_exists='replace', index=False)

# Manipulate data
# Update Data
cursor.execute('''UPDATE Book SET Title = 'Thatchwork Cottage 2' WHERE BookID = "TC188"''')

# Run queries
# Display data
book_entries = [row for row in cursor.execute("SELECT * FROM Book")]
print(book_entries)

print("Books Table: ")
data = cursor.execute('''SELECT * FROM Book WHERE Title = "'Thatchwork Cottage 2"''')

for row in data:
    print(row)

print(cursor.fetchall())

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


# Structuring queries as functions
def get_books_by_author(authorID):
    cursor.execute("SELECT * FROM Book WHERE AuthorID=:author", {'author': authorID})
    return cursor.fetchall()


get_books_by_author('GG800')


def insert_book(bookID, title, authorID):
    with connection:
        cursor.execute("INSERT INTO Book VALUES (:BookID, :Title, :AuthorID)", {'BookID': bookID, 'Title': title,
                                                                                 'AuthorID': authorID})


insert_book('DB2345', 'Databases 2', 'DB2301')


# Commit and close the connection
connection.commit()
connection.close()
