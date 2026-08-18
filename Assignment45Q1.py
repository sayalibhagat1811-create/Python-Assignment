import pandas as pd

from sklearn.preprocessing import MinMaxScaler

Border = "-" * 40

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)
# Creates a DataFrame from the given student data

Scaler = MinMaxScaler()
# Creates a Min-Max Scaler object

df['Math_Normalized'] = Scaler.fit_transform(df[['Math']])
# Normalizes Math marks between 0 and 1

print(Border)
print("DataFrame after Min-Max Scaling")
print(Border)
print(df)