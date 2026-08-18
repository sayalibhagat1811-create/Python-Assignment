import pandas as pd
import numpy as np

Border = "-" * 40

data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

df = pd.DataFrame(data2)

print(Border)
print("DataFrame with Missing Values")
print(Border)
print(df)

df['Math'] = df['Math'].fillna(df['Math'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())

print(Border)
print("DataFrame after Filling Missing Values")
print(Border)
print(df)