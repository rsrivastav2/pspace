name = "Rajat"
age = 30
cursor.execute("INSERT INTO Employees (Name, Age) VALUES (?, ?)", (name, age))
