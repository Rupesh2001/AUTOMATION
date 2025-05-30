
import sqlite3

name = input("Enter your name: ")
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

# Insert the name into the table, avoiding duplicates
cursor.execute('INSERT OR IGNORE INTO users (name) VALUES (?)', (name,))  # Pass the name as a tuple
conn.commit()

# Optionally, print a success message or retrieve the data
print("Name inserted successfully.")


# cursor.execute('UPDATE users SET name = ? WHERE id = ?', ('Rupesh', 1))
# conn.commit()

# cursor.execute('DELETE FROM users WHERE id = ?', (1,))  # Corrected DELETE statement
# conn.commit()

cursor.execute('SELECT * FROM users')
print(cursor.fetchall())  # Should print [] since user was deleted

conn.close()

import sqlite3

name = input("Enter your name: ")
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

# Insert the name into the table, avoiding duplicates
cursor.execute('INSERT OR IGNORE INTO users (name) VALUES (?)', (name,))  # Pass the name as a tuple
conn.commit()

# Optionally, print a success message or retrieve the data
print("Name inserted successfully.")


# cursor.execute('UPDATE users SET name = ? WHERE id = ?', ('Rupesh', 1))
# conn.commit()

# cursor.execute('DELETE FROM users WHERE id = ?', (1,))  # Corrected DELETE statement
# conn.commit()

cursor.execute('SELECT * FROM users')
print(cursor.fetchall())  # Should print [] since user was deleted

conn.close()

