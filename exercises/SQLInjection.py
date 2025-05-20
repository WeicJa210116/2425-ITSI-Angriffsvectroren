import sqlite3

# Datenbank erstellen
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Tabelle erstellen und Testdaten einfügen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT
    )
''')
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
conn.commit()

def login():
    username = input("Username: ")
    password = input("Password: ")
    
    # Absichtlich unsichere SQL-Abfrage
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    print(f"\nAusgeführte SQL-Abfrage:")
    print(query)
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        print("\nLogin erfolgreich!")
    else:
        print("\nLogin fehlgeschlagen!")

while True:
    print("\n=== Login System ===")
    login()
    if input("\nNochmal versuchen? (j/n): ").lower() != 'j':
        break

conn.close()