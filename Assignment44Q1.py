import pandas as pd

Border = "-" * 40

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print(Border)
print("DataFrame")
print(Border)
print(df)

print(Border)
print("Shape")
print(Border)
print(df.shape)

print(Border)
print("Columns")
print(Border)
print(df.columns)

print(Border)
print("Data Types")
print(Border)
print(df.dtypes)