import sqlite3
import datetime

DB_NAME = "technova.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create Contacts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    
    # Create Works/Projects table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS works (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT,
            timestamp TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn

# Contact Operations
def add_contact(name: str, email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    cursor.execute('INSERT INTO contacts (name, email, timestamp) VALUES (?, ?, ?)', (name, email, timestamp))
    conn.commit()
    conn.close()
    return {"name": name, "email": email, "timestamp": timestamp}

def get_all_contacts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts ORDER BY id DESC')
    contacts = cursor.fetchall()
    conn.close()
    return [dict(row) for row in contacts]

# Work/Portfolio Operations
def add_work(title: str, description: str, image_url: str = ""):
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().isoformat()
    cursor.execute('INSERT INTO works (title, description, image_url, timestamp) VALUES (?, ?, ?, ?)', 
                   (title, description, image_url, timestamp))
    conn.commit()
    conn.close()
    return {"title": title, "description": description, "image_url": image_url}

def get_all_works():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM works ORDER BY id DESC')
    works = cursor.fetchall()
    conn.close()
    return [dict(row) for row in works]

# Initialize the db on module load
init_db()
