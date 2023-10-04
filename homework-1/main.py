"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


try:
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='12345'
    )
    conn.autocommit = True

except:
    print('Не смог подключиться к БД')


orders_data = r"C:\python\postgres-homeworks\homework-1\north_data\orders_data.csv"
employees_data = r"C:\python\postgres-homeworks\homework-1\north_data\employees_data.csv"
customers_data = r"C:\python\postgres-homeworks\homework-1\north_data\customers_data.csv"

files_for_upload = {'employee': employees_data, 'customer': customers_data, 'customer_order': orders_data}

try:
    for key, value in files_for_upload.items():

        with open(value, 'r') as db:
            db_reader = csv.reader(db)

            with conn.cursor() as cur:

                for string in db_reader:

                    if '_id' in string[0]:
                        pass
                    else:
                        num_of_args = len(string) - 1
                        sql_comm = f'INSERT INTO {key} VALUES ({"%s, "*num_of_args}%s)'
                        cur.execute(sql_comm, string)
finally:
    conn.close()
