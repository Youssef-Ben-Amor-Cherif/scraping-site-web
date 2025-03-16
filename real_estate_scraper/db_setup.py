import sqlite3
import json

conn = sqlite3.connect("annonces.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS annonces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        property_type TEXT,
        location TEXT,
        area TEXT,
        description TEXT,
        contact TEXT,
        publication_date TEXT,
        url TEXT
    )
''')

# Load JSON data and insert into table
with open("data/annonces.json", "r") as f:
    data = json.load(f)
    for item in data:
        cursor.execute('''
            INSERT INTO annonces (title, price, property_type, location, area, description, contact, publication_date, url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (item["title"], item["price"], item["property_type"], item["location"], item["area"],
              item["description"], item["contact"], item["publication_date"], item["url"]))

conn.commit()
conn.close()