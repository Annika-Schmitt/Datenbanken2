import sqlite3
import pandas as pd


class BookStoreDatabaseManager:
    """
    Class to store and retrieve data from / to a sqlite database.
    """

    def __init__(self):
        self.connection = sqlite3.connect("bookstore.db")
        self.cursor = self.connection.cursor()

    def create_table_books(self):
        # Create new table "Books"
        table = """ CREATE TABLE IF NOT EXISTS Books (
                    BookID TEXT PRIMARY KEY,
                    Title TEXT,
                    AuthorID TEXT,
                    FOREIGN KEY (authorID) 
                       REFERENCES Author (authorID) 
                          ON DELETE CASCADE 
                ); """

        self.cursor.execute(table)
        self.connection.commit()

    def insert_data_to_books(self, book_id, title, author_id):
        # Insert data into table (one row only)
        self.cursor.execute("INSERT OR REPLACE INTO Books VALUES (:BookID, :Title, :AuthorID)", {'BookID': book_id,
                                                                                                 'Title': title,
                                                                                                 'AuthorID': author_id})
        self.connection.commit()

    def get_all_book_entries(self):
        book_entries = self.cursor.execute("SELECT * FROM Books")
        return book_entries.fetchall()

    def read_csv_to_table(self, path, table_name):
        data = pd.read_csv(path, sep=";")
        data.to_sql(table_name, self.connection, if_exists='replace', index=False)
        self.connection.commit()

    # Without method: Read .csv data into tables
    # connection = sqlite3.connect("bookstore.db")
    # cursor = connection.cursor()
    # book_csv = pd.read_csv('data//books.csv', sep=";")
    # book_csv.to_sql('Books', connection, if_exists='replace', index=False)

    def create_all_tables(self):
        self.read_csv_to_table('data//books.csv', 'Books')
        self.read_csv_to_table('data//author.csv', 'Author')
        self.read_csv_to_table('data//publisher.csv', 'Publisher')
        self.read_csv_to_table('data//info.csv', 'Info')

    # Update Title
    def update_book_title_by_book_id(self, new_title, book_id):
        self.cursor.execute('''UPDATE Books SET Title = :Title WHERE BookID = :BookID''',
                            {'Title': new_title, 'BookID': book_id})
        self.connection.commit()

    def get_books_by_title(self, title):
        data = self.cursor.execute('''SELECT * FROM Books WHERE Title = :Title''', {'Title': title})
        return data.fetchall()

    def get_titles_by_author_id(self, author_id):
        data = self.cursor.execute('''SELECT Title FROM Books WHERE AuthorID LIKE :AuthorID''',
                                   {'AuthorID': author_id})
        return data.fetchall()

    def order_books_entries(self, order_criteria):
        data = self.cursor.execute('''SELECT * FROM Book ORDER BY {order_criteria}'''.
                                   format(order_criteria=order_criteria))
        return data.fetchall()

    def join_books_and_info_by_book_id(self):
        data = self.cursor.execute('''SELECT Title FROM Books INNER JOIN Info ON Books.BookID = Info.BookID''')
        self.connection.commit()
        return data

    def get_oldest_publishing_house(self):
        data = self.cursor.execute('''SELECT "Publishing House", MIN("Year Established") FROM Publisher''')
        return data.fetchone()

    def insert_book(self, bookID, title, authorID):
        with self.connection:
            self.cursor.execute("INSERT INTO Books VALUES (:BookID, :Title, :AuthorID)", {'BookID': bookID,
                                                                                          'Title': title,
                                                                                          'AuthorID': authorID})
            self.connection.commit()
