import pandas as pd

Border = "-" * 40

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82],
    'Gender': ['Male', 'Male', 'Female']
}

df = pd.DataFrame(data)
# Creates a DataFrame from the given student data

df['Total'] = df['Math'] + df['Science'] + df['English']
# Calculates the total marks of each student

df['Average'] = df['Total'] / 3
# Calculates the average marks of each student

Result = df.groupby('Gender')[['Math', 'Science', 'English', 'Total', 'Average']].mean()
# Groups students by Gender and calculates the average marks

print(Border)
print("Average Marks by Gender")
print(Border)
print(Result)