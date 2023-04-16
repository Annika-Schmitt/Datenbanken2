import sqlite3
import pandas as pd

# Connecting to a new sqlite database
connection = sqlite3.connect("bookstore.db")

# Creating a new cursor object
cursor = connection.cursor()

# Creating new table "book"
table = """ CREATE TABLE IF NOT EXISTS Books (
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
cursor.execute("""INSERT INTO Books (BookID, Title, AuthorID)
                    VALUES
                        ("BB196", "Ballinby Boys", "AM329");
               """)

book_entries = [row for row in cursor.execute("SELECT * FROM Books")]
print(book_entries)

# Insert multiple rows into table
book_csv = pd.read_csv('data/bookstore/book.csv')
book_csv.to_sql('Books', connection, if_exists='replace', index=False)

cursor.execute("SELECT * FROM Books")
for row in cursor.fetchall():
    print(row)

# Commit and close the connection
connection.commit()
connection.close()


