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

plt.boxplot(df['English'])
# Creates a boxplot of English marks

plt.ylabel("English Marks")
# Adds a label to the Y-axis

plt.title("Boxplot of English Marks")
# Adds a title to the boxplot

plt.show()
# Displays the boxplot