import pandas as pd

Border = "-" * 40

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)
# Creates a DataFrame from the given student data

df = df.rename(columns={'Math': 'Mathematics'})
# Renames the Math column to Mathematics

print(Border)
print("DataFrame after Renaming Column")
print(Border)
print(df)