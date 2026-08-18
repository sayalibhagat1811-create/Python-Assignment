import pandas as pd
import matplotlib.pyplot as plt

Border = "-" * 40

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

df['Total'] = df['Math'] + df['Science'] + df['English']

print(Border)
print("Bar Plot of Student Names vs Total Marks")
print(Border)

plt.bar(df['Name'], df['Total'])
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.title("Student Names vs Total Marks")
plt.show()