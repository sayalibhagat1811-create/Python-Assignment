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
# Assigns Pass or Fail according to total marks

PassCount = (df['Status'] == 'Pass').sum()
# Counts the number of students having Pass status

print(Border)
print("Number of Students Passed")
print(Border)
print(PassCount)