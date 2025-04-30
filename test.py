import pandas as pd

# Load search values from Excel
excel_file = 'your_excel_file.xlsx'   # Your Excel file
sheet_name = 'Sheet1'                 # Adjust if needed
column_name = 'SearchValues'          # Adjust to your column name
df = pd.read_excel(excel_file, sheet_name=sheet_name)
search_values = set(df[column_name].astype(str))  # Use set for faster lookup

# Input and output file paths
text_file = 'your_text_file.txt'      # Large text file
output_file = 'matched_lines.txt'     # Output file for matching lines

# Search and write matching lines
with open(text_file, 'r', encoding='utf-8', errors='ignore') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if any(val in line for val in search_values):
            outfile.write(line)
