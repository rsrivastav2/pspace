import pandas as pd

# Load search values from Excel
excel_file = 'your_excel_file.xlsx'
sheet_name = 'Sheet1'
column_name = 'SearchValues'

df = pd.read_excel(excel_file, sheet_name=sheet_name)
search_values = df[column_name].astype(str).tolist()

# Input and output file paths
text_file = 'your_text_file.txt'
output_file = 'matched_lines_with_values.txt'

# Search and write matching lines with corresponding Excel value
with open(text_file, 'r', encoding='utf-8', errors='ignore') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        for value in search_values:
            if value in line:
                # Write both the matched value and the line
                outfile.write(f"{value} ==> {line}")
                break  # avoid multiple matches per line, optional
