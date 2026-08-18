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

plt.hist(df['Math'], bins=5)
# Creates a histogram of Math marks

plt.xlabel("Math Marks")
# Adds a label to the X-axis

plt.ylabel("Frequency")
# Adds a label to the Y-axis

plt.title("Distribution of Math Marks")
# Adds a title to the histogram

plt.show()
# Displays the histogram