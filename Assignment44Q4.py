import pandas as pd

Border = "-" * 40

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

Result = df[df['Science'] > 85]

print(Border)
print("Students who scored more than 85 in Science")
print(Border)
print(Result)