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

df['Gender'] = ['Male', 'Male', 'Female']
# Adds a Gender column to the DataFrame

df = pd.get_dummies(df, columns=['Gender'], dtype=int)
# Performs one-hot encoding on the Gender column

print(Border)
print("DataFrame after One-Hot Encoding")
print(Border)
print(df)