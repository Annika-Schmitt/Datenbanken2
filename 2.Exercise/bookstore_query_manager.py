import bookstore_database_manager

# Create table Books, fill with data, and get all entries
bookstore_database_manager = bookstore_database_manager.BookStoreDatabaseManager()
bookstore_database_manager.create_table_books()
bookstore_database_manager.insert_data_to_books(book_id="BB196", title="Ballinby Boys", author_id="AM329")
books_entries = bookstore_database_manager.get_all_book_entries()
print('Show all entries in Books table: ')
for entry in books_entries:
    print(entry)

# Update book title and check if update worked as expected
bookstore_database_manager.update_book_title_by_book_id(new_title='Thatchwork Cottage 2', book_id='TC188')
books_entries_by_title = bookstore_database_manager.get_books_by_title(title='Thatchwork Cottage 2')
print('\nShow all books with title == Thatchwork Cottage 2: ')
for book in books_entries_by_title:
    print(book)

# Weitere Aufgaben:
# Erstelle alle Tabellen aus den .csv Dateien
bookstore_database_manager.create_all_tables()

# Gebe alle Titel aus, deren AutorID mit 'CF' anfängt
titles_by_author_id = bookstore_database_manager.get_titles_by_author_id(author_id='CF')
print('\nShow all titles where author_id starts with CF: ')
for book in titles_by_author_id:
    print(book)

# Gebe alle Inhalte der Books Tabelle in alphabetisch sortierte Reihenfolge nach BookID aus
books_ordered_by_book_id = bookstore_database_manager.order_books_entries(order_criteria='BookID')
print('\nShow all books ordered by book_id: ')
for book in books_ordered_by_book_id:
    print(book)

# Gebe alle Buchtitel des Genre 'Fiction' aus
titles = bookstore_database_manager.join_books_and_info_by_book_id()
print('\nShow all books with genre == Fiction: ')
for title in titles:
    print(title)

# Welcher Verlag existiert am längsten ('Year Established’)
publishing_house = bookstore_database_manager.get_oldest_publishing_house()
print('\nShow oldest publishing house: ')
print(publishing_house)




