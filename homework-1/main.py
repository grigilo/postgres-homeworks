"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from config import FILE_1, FILE_2, FILE_3
from func import data_read

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='Pjkeirf8$')
cur = conn.cursor()

for row in data_read(FILE_1):
    cur.execute("INSERT INTO customers"
                "(customer_id, company_name, contact_name) "
                "VALUES (%s, %s, %s)", row)
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    conn.commit()

for row in data_read(FILE_2):
    cur.execute("INSERT INTO employees"
                "(employee_id, first_name, last_name, "
                "title, birth_date, notes) "
                "VALUES (%s, %s, %s, %s, %s, %s)", row)
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.commit()

for row in data_read(FILE_3):
    cur.execute("INSERT INTO orders"
                "(order_id, customer_id, employee_id, "
                "order_date, ship_city) "
                "VALUES (%s, %s, %s, %s, %s)", row)
    cur.execute("SELECT * FROM orders")
    rows = cur.fetchall()
    conn.commit()
