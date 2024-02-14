import psycopg2
from psycopg2 import extensions

# establish a connection to the database
connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost'"
                              " port='5432' password='postgres'")

# for testing purposes set autocommit to False
connection.autocommit = False
cursor = connection.cursor()

# Writing transactions with try-except-block
try:
    # write the transaction query
    cursor.execute("""INSERT INTO city (postal_code, city, country_code) 
                        VALUES (74072, 'Heilbronn', DE) """)
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
    # in case of an error rollback all changes done before
    print(error)
    connection.rollback()

# finally:
    #  closing the database connection.
    # if connection:
    #     cursor.close()
    #     connection.close()

# Writing transactions with with-Statement
# transaction 1
connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost'"
                              " port='5432' password='postgres'")
with connection:
    with connection.cursor() as cursor:
        cursor.execute("""SELECT title FROM film WHERE rental_duration = 2""")
        cursor.execute("""UPDATE film SET rental_duration = 3 WHERE rental_duration = 2""")
        cursor.execute("""SELECT title FROM film WHERE rental_duration = 3""")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])


# transaction 2
with connection:
    with connection.cursor() as cursor:
        cursor.execute("""SELECT title FROM film WHERE rental_duration = 5""")
        # transaction 2 has started
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])

        cursor.execute("""UPDATE film SET rental_duration = 4 WHERE rental_duration = 5""")
        # will be executed within transaction 2

# connection.close()

# Two-Phase Commit Protocol
# Create two connections
connection1 = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost'"
                              " port='5432' password='postgres'")
connection2 = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost'"
                              " port='5432' password='postgres'")
cursor1 = connection1.cursor()
cursor2 = connection2.cursor()

# Initiate transactions
connection1.tpc_begin(connection1.xid(42, 'transaction ID', 'connection 1'))
connection2.tpc_begin(connection2.xid(42, 'transaction ID', 'connection 2'))

try:
    cursor1.execute("""SELECT title FROM film WHERE rental_duration = 4""")
    cursor1.execute("""UPDATE film SET rental_duration = 4 WHERE rental_duration = 5""")
    cursor2.execute("""SELECT title FROM film WHERE rental_duration = 3""")
    cursor2.execute("""UPDATE film SET rental_duration = 2 WHERE rental_duration = 3""")

# Prepare transactions to verify if an error would occur
    connection1.tpc_prepare()
    connection2.tpc_prepare()

except (Exception, psycopg2.DatabaseError) as error:
    print("Error in transaction, reverting all changes using rollback ", error)
    # Rollback if error had happened
    connection1.tpc_rollback()
    connection2.tpc_rollback()
else:
    # If prepare worked without error, commit transactions
    connection1.tpc_commit()
    connection2.tpc_commit()
#finally:
    # close database connection
    # if connection:
    #     cursor.close()
    #    connection.close()

# Setting the isolation level
connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' port='5432' password='postgres'")
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
print("isolation_level:", connection.isolation_level)

connection.close()


