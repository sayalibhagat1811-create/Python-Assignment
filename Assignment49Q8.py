from sklearn.metrics import confusion_matrix
# Import confusion_matrix to calculate TP, TN, FP and FN

Actual = [1, 1, 1, 1, 0, 0, 0, 0]
# Store actual values

Predicted = [1, 1, 0, 1, 0, 1, 0, 0]
# Store predicted values

CM = confusion_matrix(Actual, Predicted)
# Calculate the confusion matrix

TN, FP, FN, TP = CM.ravel()
# Extract TN, FP, FN and TP from the confusion matrix

print("True Positive (TP) :", TP)
# Display True Positive

print("True Negative (TN) :", TN)
# Display True Negative

print("False Positive (FP) :", FP)
# Display False Positive

print("False Negative (FN) :", FN)
# Display False Negative