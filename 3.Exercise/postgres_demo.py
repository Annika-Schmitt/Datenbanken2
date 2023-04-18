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
        cursor.execute("""SELECT title FROM film WHERE rental_duration = 3""")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])

# transaction 2
with connection:
    with connection.cursor() as cursor:
        cursor.execute("""SELECT title FROM film WHERE rental_duration = 5""")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])

connection.close()

# Setting the isolation level
connection = psycopg2.connect("dbname='dvdrental' user='postgres' host='localhost' port='5432' password='postgres'")
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
print("isolation_level:", connection.isolation_level)

connection.close()


