import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO volunteers (aadhar_number, phone_number, traffic_violation,major_crime) VALUES (?, ?, ?, ?)", ('456386429831', '+919547773307', 1, 0))

cur.execute("INSERT INTO volunteers (aadhar_number, phone_number, traffic_violation,major_crime) VALUES (?, ?, ?, ?)", ('456386429830', '+917679952548', 0, 0))

cur.execute("INSERT INTO volunteers (aadhar_number, phone_number, traffic_violation,major_crime) VALUES (?, ?, ?, ?)", ('456386429832', '+917679952548', 0, 1))

connection.commit()
connection.close()