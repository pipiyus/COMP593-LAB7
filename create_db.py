"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker


# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    sql_create_table = """
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            location TEXT
        )
    """
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(sql_create_table)
        print("Table 'people' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    
    fake = Faker()
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            for _ in range(200):
                name = fake.name()
                age = fake.random_int(min=18, max=100)
                location = fake.city()
                cur.execute("INSERT INTO people (name, age, location) VALUES (?, ?, ?)",
                            (name, age, location))
            conn.commit()
        print("Data inserted into 'people' table successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
        
if __name__ == '__main__':
   main()