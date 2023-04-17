import sqlite3
import pandas as pd

# Connecting to a new sqlite database
connection = sqlite3.connect("bookstore.db")

# Creating a new cursor object
cursor = connection.cursor()

# Creating new table "book"
table = """ CREATE TABLE IF NOT EXISTS Book (
            BookID TEXT PRIMARY KEY,
            Title TEXT,
            AuthorID TEXT,
            FOREIGN KEY (AuthorID) 
               REFERENCES Author (AuthorID) 
                  ON DELETE CASCADE 
        ); """

cursor.execute(table)

# reading all table names
table_list = [table for table in cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
print(table_list)

# Commit the connection
connection.commit()

# Insert data into table (one row only)
cursor.execute("""INSERT INTO Book (BookID, Title, AuthorID)
                    VALUES
                        ("BB196", "Ballinby Boys", "AM329");
               """)

book_entries = [row for row in cursor.execute("SELECT * FROM Book")]
print(book_entries)

# Insert multiple rows into table
book_csv = pd.read_csv('data//book.csv', sep=";")
book_csv.to_sql('Book', connection, if_exists='replace', index=False)

author_csv = pd.read_csv('data//author.csv', sep=";")
author_csv.to_sql('Author', connection, if_exists='replace', index=False)

publisher_csv = pd.read_csv('data//publisher.csv', sep=";")
publisher_csv.to_sql('Publisher', connection, if_exists='replace', index=False)

info_csv = pd.read_csv('data//info.csv', sep=";")
info_csv.to_sql('Info', connection, if_exists='replace', index=False)

# Commit and close the connection
connection.commit()
connection.close()


