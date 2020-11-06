from flask_sqlalchemy import SQLAlchemy
import os, psycopg2
from dotenv import load_dotenv
load_dotenv()



try:
    connection = psycopg2.connect(user = os.getenv('DB_USER'),
                                  password = os.getenv('DB_PASSWORD'),
                                  host = os.getenv('DB_HOST'),
                                  port = os.getenv('DB_PORT'),
                                  database = os.getenv('DB_NAME'))

    print("PostgreSQL connection is open")

    cursor = connection.cursor()                               
    my_query = (''' select * from test;''')
    cursor.execute(my_query)

    print("PostgreSQL ok")

    # print("The query retrieved", cursor.rowcount, "records\n")
    # print("All records are:\n")
    # row = cursor.fetchall()
    # print(row)
    # print("\nThe records are:\n")
    # for r in row:
    #     print(r)

    
    connection.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")