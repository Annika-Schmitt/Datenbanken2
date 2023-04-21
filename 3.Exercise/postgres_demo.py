import psycopg2
from psycopg2 import extensions

# Create a connection to the existing database (use same values as during setup)
connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' port='5432' password='postgres'")
cursor = connection.cursor()

# Verify if database is used correctly
cursor.execute("""SELECT country from country""")
rows = cursor.fetchall()
for row in rows:
    print(row[0])

connection.commit()
connection.close()

# Writing Transactions
# use try - except - finally blocks
try:
    # establish a connection to the database
    connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' port='5432' password='postgres'")

    # disable autocommit mode
    connection.autocommit = False
    cursor = connection.cursor()

    # write query as part of a transaction
    query = """SELECT title FROM film WHERE rental_duration = 3"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])

    cursor.execute("""UPDATE film SET rental_duration = 3 WHERE rental_duration = 2""")

    # committing changes
    connection.commit()
    print("successfully finished the transaction ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error in transaction, reverting all changes using rollback ", error)
    connection.rollback()

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL database connection is closed")

# use with-Statement
connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' port='5432' password='postgres'")

# transaction 1
with connection:
    with connection.cursor() as cursor:
        cursor.execute("""SELECT title FROM film WHERE rental_duration = 2""")
        # transaction 1 has started
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])

        cursor.execute("""UPDATE film SET rental_duration = 3 WHERE rental_duration = 2""")
        # will be executed within transaction 1


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

connection.close()

# Two-Phase Commit Protocol
# Will result in a config error due to missing max_prepared transactions parameter
# try:
#     # establish a connection to the database
#     connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' port='5432' password='postgres'")
#
#     # get transaction ID
#     xid = connection.xid(235, "global235", "branch")
#
#     # BEGIN transaction (all queries afterwards are part of same transaction)
#     connection.tpc_begin(xid)
#
#     cursor = connection.cursor()
#     cursor.execute("""SELECT title FROM film WHERE rental_duration = 4""")
#     cursor.execute("""UPDATE film SET rental_duration = 4 WHERE rental_duration = 5""")
#
#     # PREPARE transaction
#     connection.tpc_prepare()
#
#     # COMMIT if no exception was raised
#     connection.tpc_commit(xid)
#
# except (Exception, psycopg2.DatabaseError) as error:
#     print("Error in transaction, reverting all changes using rollback ", error)
#     # ROLLBACK if error happened
#     connection.tpc_rollback(xid)
#
# finally:
#     # closing database connection.
#     if connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL database connection is closed")
#

# Setting the isolation level
connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' port='5432' password='postgres'")
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
print("isolation_level:", connection.isolation_level)

connection.close()


