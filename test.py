def get_machine_from_jil(job_name):
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=path_to_your_db.accdb;')
    cursor = conn.cursor()

    cursor.execute("SELECT machine_name FROM JIL WHERE job_name = ?", (job_name,))
    result = cursor.fetchone()
    
    if result:
        return result[0]
    else:
        return None
