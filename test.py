import pyodbc

db_file = r"C:\path\to\your\database.accdb"
conn_str = (
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
    f"DBQ={db_file};"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT * FROM YourTable")

for row in cursor.fetchall():
    print(row)

conn.close()
