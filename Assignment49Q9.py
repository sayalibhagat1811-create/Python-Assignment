from sklearn.metrics import classification_report
# Import classification_report to evaluate the classification model

Actual = [1, 1, 1, 1, 0, 0, 0, 0]
# Store actual values

Predicted = [1, 1, 0, 1, 0, 1, 0, 0]
# Store predicted values

Report = classification_report(Actual, Predicted)
# Generate the complete classification report

print("Classification Report :")
print(Report)
# Display the classification report