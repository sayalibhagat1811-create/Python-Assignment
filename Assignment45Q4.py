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
# Creates a DataFrame from the given student data

Sagar = df[df['Name'] == 'Sagar'].iloc[0]
# Selects Sagar's marks from the DataFrame

Subjects = ['Math', 'Science', 'English']
# Stores the subject names

Marks = [Sagar['Math'], Sagar['Science'], Sagar['English']]
# Stores Sagar's marks for all subjects

plt.pie(Marks, labels=Subjects, autopct='%1.1f%%')
# Creates a pie chart showing Sagar's subject-wise marks

plt.title("Sagar's Subject Marks")
# Adds a title to the pie chart

plt.show()
# Displays the pie chart