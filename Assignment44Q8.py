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

Amit = df[df['Name'] == 'Amit'].iloc[0]

Subjects = ['Math', 'Science', 'English']
Marks = [Amit['Math'], Amit['Science'], Amit['English']]

print(Border)
print("Amit's Marks")
print(Border)
print(Amit)

plt.plot(Subjects, Marks, marker='o')
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit's Marks Across All Subjects")
plt.show()