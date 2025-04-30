import pandas as pd

# Load Excel file
excel_file = 'your_excel_file.xlsx'  # Replace with your file path
sheet_name = 'Sheet1'  # Replace with your sheet name if different
column_name = 'SearchValues'  # Replace with your actual column name

# Read the Excel column
df = pd.read_excel(excel_file, sheet_name=sheet_name)
search_values = df[column_name].astype(str).tolist()

# Open the text file and search for lines
text_file = 'your_text_file.txt'  # Replace with your text file path
matching_lines = []

with open(text_file, 'r', encoding='utf-8') as file:
    for line in file:
        if any(value in line for value in search_values):
            matching_lines.append(line.strip())

# Output the results
for line in matching_lines:
    print(line)
