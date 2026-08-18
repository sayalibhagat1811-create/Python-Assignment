import pandas as pd

Border = "-" * 40

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

df['Name'] = df['Name'].replace('Pooja', 'Puja')

print(Border)
print("Updated DataFrame")
print(Border)
print(df)