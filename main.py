import pandas as pd

# Read the Excel file
df = pd.read_excel("sample.xlsx")

# Count rows before removing duplicates
rows_before = len(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Count rows after removing duplicates
rows_after = len(df)

# Save the cleaned data
df.to_excel("cleaned_data.xlsx", index=False)

# Print the results
print("Excel cleaned successfully!")
print("Rows before:", rows_before)
print("Rows after:", rows_after)
print("Duplicates removed:", rows_before - rows_after)
print("New file saved as cleaned_data.xlsx")