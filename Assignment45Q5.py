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

df['Total'] = df['Math'] + df['Science'] + df['English']
# Calculates total marks for each student

df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
# Assigns Pass when Total is 250 or more, otherwise Fail

print(Border)
print("DataFrame with Status")
print(Border)
print(df)