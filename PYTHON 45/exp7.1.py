import sqlite3

# Create a connection to the database
conn = sqlite3.connect('EMP_RECORD.db')

# Create a cursor object
cursor = conn.cursor()

# Create the Emp_Details table
cursor.execute("""
    CREATE TABLE Emp_Details (
        Emp_id INTEGER PRIMARY KEY,
        Emp_nm TEXT,
        Emp_Sal REAL,
        Emp_add TEXT
    )
""")

# Insert 3 records into the Emp_Details table
cursor.execute("""
    INSERT INTO Emp_Details (Emp_id, Emp_nm, Emp_Sal, Emp_add)
    VALUES (1, 'John Doe', 50000.0, 'New York')
""")
cursor.execute("""
    INSERT INTO Emp_Details (Emp_id, Emp_nm, Emp_Sal, Emp_add)
    VALUES (2, 'Jane Smith', 60000.0, 'London')
""")
cursor.execute("""
    INSERT INTO Emp_Details (Emp_id, Emp_nm, Emp_Sal, Emp_add)
    VALUES (3, 'Bob Johnson', 70000.0, 'Paris')
""")

conn.commit()

cursor.execute("SELECT * FROM Emp_Details LIMIT 2")
rows = cursor.fetchall()
print("First two records of the table:")
for row in rows:
    print(row)

conn.close()
print("\nThe SQLite connection is closed.")
