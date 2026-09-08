# ============================================================
# DEEP LEARNING ASSIGNMENT
# LOAN DEFAULT PREDICTION USING MULTI-LAYER PERCEPTRON
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT REQUIRED LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


# ------------------------------------------------------------
# 2. CREATE SAMPLE DATASET
# ------------------------------------------------------------

random.seed(42)

rows = []

# Generate 300 records
for i in range(300):

    age = random.randint(21, 65)

    income = random.randint(25000, 150000)

    loan_amount = random.randint(5000, 100000)

    credit_score = random.randint(450, 850)

    employment_years = random.randint(0, 35)

    existing_loans = random.randint(0, 5)

    monthly_debt = random.randint(500, 25000)

    loan_term = random.choice([12, 24, 36, 48, 60, 72, 84])

    previous_default = random.choice(["Yes", "No"])

    home_ownership = random.choice(
        ["Rent", "Own", "Mortgage"]
    )

    risk_score = 0

    if credit_score < 600:
        risk_score += 2
    elif credit_score < 680:
        risk_score += 1

    if income < 45000:
        risk_score += 1

    if loan_amount > income * 0.60:
        risk_score += 2
    elif loan_amount > income * 0.40:
        risk_score += 1

    if existing_loans >= 3:
        risk_score += 1

    if monthly_debt > income / 4:
        risk_score += 1

    if employment_years < 2:
        risk_score += 1

    if previous_default == "Yes":
        risk_score += 3

    if home_ownership == "Rent":
        risk_score += 0.5

    risk_score += random.choice([-1, 0, 0, 0, 1])

    if risk_score >= 4:
        default = 1
    else:
        default = 0

    rows.append([
        age,
        income,
        loan_amount,
        credit_score,
        employment_years,
        existing_loans,
        monthly_debt,
        loan_term,
        previous_default,
        home_ownership,
        default
    ])


# ------------------------------------------------------------
# 3. CREATE DATAFRAME
# ------------------------------------------------------------

columns = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "EmploymentYears",
    "ExistingLoans",
    "MonthlyDebt",
    "LoanTerm",
    "PreviousDefault",
    "HomeOwnership",
    "Default"
]

df = pd.DataFrame(
    rows,
    columns=columns
)

print("First Five Records:")
print(df.head())


# ------------------------------------------------------------
# 4. SAVE DATASET AS CSV
# ------------------------------------------------------------

df.to_csv(
    "loan_default_prediction.csv",
    index=False
)

print("\nCSV file created successfully!")
print("File Name: loan_default_prediction.csv")


# ------------------------------------------------------------
# 5. LOAD DATASET FROM CSV
# ------------------------------------------------------------

df = pd.read_csv(
    "loan_default_prediction.csv"
)

print("\nDataset:")
print(df.head())


# ------------------------------------------------------------
# 6. UNDERSTAND THE DATASET
# ------------------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())


# ------------------------------------------------------------
# 7. EXPLORATORY DATA ANALYSIS
# ------------------------------------------------------------

print("\nUnique Values:")

print("PreviousDefault:")
print(df["PreviousDefault"].unique())

print("HomeOwnership:")
print(df["HomeOwnership"].unique())

print("Default:")
print(df["Default"].unique())


# ------------------------------------------------------------
# 8. CHECK MISSING VALUES
# ------------------------------------------------------------

missing_values = df.isnull().sum()

print("\nMissing Values:")
print(missing_values)


# ------------------------------------------------------------
# 9. CHECK DUPLICATE VALUES
# ------------------------------------------------------------

duplicates = df.duplicated().sum()

print("\nNumber of Duplicate Rows:", duplicates)

# ------------------------------------------------------------
# 10. CHECK TARGET CLASS BALANCE
# ------------------------------------------------------------

class_count = df["Default"].value_counts()

print("\nTarget Class Count:")
print(class_count)

class_percentage = (
    df["Default"]
    .value_counts(normalize=True)
    * 100
)

print("\nTarget Class Percentage:")
print(class_percentage)

# ------------------------------------------------------------
# 11. PLOT TARGET CLASS DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    x="Default",
    data=df
)

plt.title(
    "Loan Default Class Distribution"
)

plt.xlabel(
    "Default Class"
)

plt.ylabel(
    "Number of Applicants"
)

plt.show()

# ------------------------------------------------------------
# 12. SEPARATE X AND y
# ------------------------------------------------------------

X = df.drop(
    "Default",
    axis=1
)

y = df["Default"]

print("\nFeatures X:")
print(X.head())

print("\nTarget y:")
print(y.head())

# ------------------------------------------------------------
# 13. DEFINE CATEGORICAL AND NUMERICAL COLUMNS
# ------------------------------------------------------------

categorical_columns = [
    "PreviousDefault",
    "HomeOwnership"
]

numerical_columns = [
    "Age",
    "Income",
    "LoanAmount",
    "CreditScore",
    "EmploymentYears",
    "ExistingLoans",
    "MonthlyDebt",
    "LoanTerm"
]

# ------------------------------------------------------------
# 14. TRAIN TEST SPLIT
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data Shape:")
print(X_train.shape)

print("\nTesting Data Shape:")
print(X_test.shape)

print("\nTraining Target Distribution:")
print(y_train.value_counts(normalize=True))

print("\nTesting Target Distribution:")
print(y_test.value_counts(normalize=True))

# ------------------------------------------------------------
# 15. CREATE PREPROCESSING PIPELINE
# ------------------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        
        (
            "categorical",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            categorical_columns
        ),
        
        # Scale numerical columns
        (
            "numerical",
            StandardScaler(),
            numerical_columns
        )
    ]
)

# ------------------------------------------------------------
# 16. FIT AND TRANSFORM TRAINING DATA
# ------------------------------------------------------------

X_train_processed = preprocessor.fit_transform(
    X_train
)

X_test_processed = preprocessor.transform(
    X_test
)

print(
    "\nProcessed Training Shape:",
    X_train_processed.shape
)

print(
    "Processed Testing Shape:",
    X_test_processed.shape
)

# ------------------------------------------------------------
# 17. CREATE MLP CLASSIFIER
# ------------------------------------------------------------

mlp = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print("\nMLP Model:")
print(mlp)


# ------------------------------------------------------------
# 18. TRAIN THE MODEL
# ------------------------------------------------------------

mlp.fit(
    X_train_processed,
    y_train
)

print("\nModel Training Completed!")


# ------------------------------------------------------------
# 19. MAKE PREDICTIONS
# ------------------------------------------------------------

y_pred = mlp.predict(
    X_test_processed
)

print("\nPredicted Values:")
print(y_pred)

# ------------------------------------------------------------
# 20. CALCULATE ACCURACY
# ------------------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)

print(
    "Accuracy Percentage:",
    accuracy * 100,
    "%"
)

# ------------------------------------------------------------
# 21. CONFUSION MATRIX
# ------------------------------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)

print("Confusion Matrix:")
print(cm)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=[
        "Low Risk",
        "High Risk"
    ],
    yticklabels=[
        "Low Risk",
        "High Risk"
    ]
)

plt.title(
    "Confusion Matrix"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)
plt.show()

# ------------------------------------------------------------
# 22. CLASSIFICATION REPORT
# ------------------------------------------------------------

report = classification_report(
    y_test,
    y_pred,
    target_names=[
        "Low Default Risk",
        "High Default Risk"
    ]
)

print("\nClassification Report:")
print(report)

# ------------------------------------------------------------
# 23. PRECISION
# ------------------------------------------------------------

precision = precision_score(
    y_test,
    y_pred
)

print("\nPrecision:", precision)

# ------------------------------------------------------------
# 24. RECALL
# ------------------------------------------------------------

recall = recall_score(
    y_test,
    y_pred
)

print("Recall:", recall)

# ------------------------------------------------------------
# 25. F1 SCORE
# ------------------------------------------------------------

f1 = f1_score(
    y_test,
    y_pred
)
print("F1 Score:", f1)

# ------------------------------------------------------------
# 26. TRAINING LOSS GRAPH
# ------------------------------------------------------------

loss_values = mlp.loss_curve_

plt.figure(figsize=(8, 5))

plt.plot(
    loss_values
)
plt.title(
    "MLP Training Loss Curve"
)

plt.xlabel(
    "Iterations"
)

plt.ylabel(
    "Loss"
)

plt.grid()
plt.show()

# ------------------------------------------------------------
# 27. TEST NEW LOAN APPLICANT
# ------------------------------------------------------------

new_applicant = pd.DataFrame({
    
    "Age": [35],
    
    "Income": [70000],
    
    "LoanAmount": [25000],
    
    "CreditScore": [720],
    
    "EmploymentYears": [8],
    
    "ExistingLoans": [1],
    
    "MonthlyDebt": [5000],
    
    "LoanTerm": [36],
    
    "PreviousDefault": ["No"],
    
    "HomeOwnership": ["Own"]
})

print("\nNew Applicant:")
print(new_applicant)

# ------------------------------------------------------------
# 28. PREPROCESS NEW APPLICANT
# ------------------------------------------------------------

new_applicant_processed = preprocessor.transform(
    new_applicant
)

# ------------------------------------------------------------
# 29. PREDICT NEW APPLICANT
# ------------------------------------------------------------

new_prediction = mlp.predict(
    new_applicant_processed
)

new_probability = mlp.predict_proba(
    new_applicant_processed
)

print("\nNew Applicant Prediction:")

print(
    "Predicted Class:",
    new_prediction[0]
)

print(
    "Low Default Risk Probability:",
    new_probability[0][0]
)

print(
    "High Default Risk Probability:",
    new_probability[0][1]
)

# ------------------------------------------------------------
# 30. DISPLAY FINAL PREDICTION
# ------------------------------------------------------------

if new_prediction[0] == 0:
    
    print(
        "\nResult: LOW DEFAULT RISK"
    )

else:
    
    print(
        "\nResult: HIGH DEFAULT RISK"
    )

# ============================================================
# HYPERPARAMETER EXPERIMENTS
# ============================================================

# ------------------------------------------------------------
# 31. EXPERIMENT 1 - ACTIVATION FUNCTION
# ------------------------------------------------------------

activation_functions = [
    "identity",
    "logistic",
    "tanh",
    "relu"
]

activation_results = {}

for activation in activation_functions:

    model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model.fit(
        X_train_processed,
        y_train
    )

    predictions = model.predict(
        X_test_processed
    )

    score = accuracy_score(
        y_test,
        predictions
    )

    activation_results[activation] = score

print("========================================")
print("EXPERIMENT 1 - ACTIVATION FUNCTION")
print("========================================")

for activation, score in activation_results.items():
    
    print(
        activation,
        ":",
        score
    )

# ------------------------------------------------------------
# 32. PLOT ACTIVATION RESULTS
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.bar(
    activation_results.keys(),
    activation_results.values()
)

plt.title(
    "Activation Function Comparison"
)

plt.xlabel(
    "Activation Function"
)

plt.ylabel(
    "Accuracy"
)

plt.ylim(
    0,
    1
)

plt.show()

# ------------------------------------------------------------
# 33. EXPERIMENT 2 - HIDDEN LAYERS
# ------------------------------------------------------------
hidden_layers = [
    (10,),
    (20, 10),
    (50, 25),
    (100, 50, 25)
]
hidden_results = {}

for layers in hidden_layers:

    model = MLPClassifier(
        hidden_layer_sizes=layers,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model.fit(
        X_train_processed,
        y_train
    )

    predictions = model.predict(
        X_test_processed
    )

    score = accuracy_score(
        y_test,
        predictions
    )

    hidden_results[str(layers)] = score

print("========================================")
print("EXPERIMENT 2 - HIDDEN LAYERS")
print("========================================")

for layers, score in hidden_results.items():
    
    print(
        layers,
        ":",
        score
    )

# ------------------------------------------------------------
# 34. PLOT HIDDEN LAYER RESULTS
# ------------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.bar(
    hidden_results.keys(),
    hidden_results.values()
)

plt.title(
    "Hidden Layer Architecture Comparison"
)

plt.xlabel(
    "Hidden Layer Architecture"
)

plt.ylabel(
    "Accuracy"
)

plt.ylim(
    0,
    1
)

plt.xticks(
    rotation=20
)

plt.show()
# ------------------------------------------------------------
# 35. EXPERIMENT 3 - LEARNING RATE
# ------------------------------------------------------------
learning_rates = [
    0.0001,
    0.001,
    0.01,
    0.1
]

learning_results = {}

for rate in learning_rates:

    model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=rate,
        max_iter=1000,
        random_state=42
    )

    model.fit(
        X_train_processed,
        y_train
    )

    predictions = model.predict(
        X_test_processed
    )

    score = accuracy_score(
        y_test,
        predictions
    )
    learning_results[rate] = score

print("========================================")
print("EXPERIMENT 3 - LEARNING RATE")
print("========================================")

for rate, score in learning_results.items():
    
    print(
        rate,
        ":",
        score
    )
# ------------------------------------------------------------
# 36. PLOT LEARNING RATE RESULTS
# ------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(
    list(learning_results.keys()),
    list(learning_results.values()),
    marker="o"
)
plt.title(
    "Learning Rate Comparison"
)

plt.xlabel(
    "Learning Rate"
)

plt.ylabel(
    "Accuracy"
)

plt.xscale(
    "log"
)
plt.grid()
plt.show()
# ------------------------------------------------------------
# 37. FIND BEST ACTIVATION FUNCTION
# ------------------------------------------------------------

best_activation = max(
    activation_results,
    key=activation_results.get
)

best_activation_accuracy = activation_results[
    best_activation
]

print("\nBest Activation Function:")
print(best_activation)

print(
    "Accuracy:",
    best_activation_accuracy
)
# ------------------------------------------------------------
# 38. FIND BEST HIDDEN LAYER
# ------------------------------------------------------------
best_hidden = max(
    hidden_results,
    key=hidden_results.get
)

best_hidden_accuracy = hidden_results[
    best_hidden
]

print("\nBest Hidden Layer:")
print(best_hidden)

print(
    "Accuracy:",
    best_hidden_accuracy
)

# ------------------------------------------------------------
# 39. FIND BEST LEARNING RATE
# ------------------------------------------------------------

best_learning_rate = max(
    learning_results,
    key=learning_results.get
)

best_learning_rate_accuracy = learning_results[
    best_learning_rate
]

print("\nBest Learning Rate:")
print(best_learning_rate)

print(
    "Accuracy:",
    best_learning_rate_accuracy
)

# ------------------------------------------------------------
# 40. EXPERIMENT RESULTS TABLE
# ------------------------------------------------------------

activation_df = pd.DataFrame(
    list(
        activation_results.items()
    ),
    columns=[
        "Activation",
        "Accuracy"
    ]
)

hidden_df = pd.DataFrame(
    list(
        hidden_results.items()
    ),
    columns=[
        "Hidden Layers",
        "Accuracy"
    ]
)

learning_df = pd.DataFrame(
    list(
        learning_results.items()
    ),
    columns=[
        "Learning Rate",
        "Accuracy"
    ]
)

print("\nActivation Experiment:")
print(activation_df)

print("\nHidden Layer Experiment:")
print(hidden_df)

print("\nLearning Rate Experiment:")
print(learning_df)

# ------------------------------------------------------------
# 41. FINAL MODEL
# ------------------------------------------------------------

best_hidden_tuple = eval(
    best_hidden
)

final_model = MLPClassifier(
    hidden_layer_sizes=best_hidden_tuple,
    activation=best_activation,
    solver="adam",
    learning_rate_init=best_learning_rate,
    max_iter=1000,
    random_state=42
)

# ------------------------------------------------------------
# 42. TRAIN FINAL MODEL
# ------------------------------------------------------------
final_model.fit(
    X_train_processed,
    y_train
)

print("\nFinal Model Training Completed!")
# ------------------------------------------------------------
# 43. FINAL PREDICTION
# ------------------------------------------------------------
final_predictions = final_model.predict(
    X_test_processed
)
# ------------------------------------------------------------
# 44. FINAL EVALUATION
# ------------------------------------------------------------
final_accuracy = accuracy_score(
    y_test,
    final_predictions
)

final_precision = precision_score(
    y_test,
    final_predictions
)

final_recall = recall_score(
    y_test,
    final_predictions
)

final_f1 = f1_score(
    y_test,
    final_predictions
)

# ------------------------------------------------------------
# 45. DISPLAY FINAL RESULTS
# ------------------------------------------------------------

print("=======================================")
print("FINAL MODEL RESULTS")
print("========================================")

print(
    "Accuracy :",
    final_accuracy
)

print(
    "Precision:",
    final_precision
)

print(
    "Recall   :",
    final_recall
)

print(
    "F1 Score :",
    final_f1
)
# ------------------------------------------------------------
# 46. FINAL CONFUSION MATRIX
# ------------------------------------------------------------

final_cm = confusion_matrix(
    y_test,
    final_predictions
)

print("\nFinal Confusion Matrix:")
print(final_cm)

plt.figure(figsize=(7, 5))

sns.heatmap(
    final_cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=[
        "Low Risk",
        "High Risk"
    ],
    yticklabels=[
        "Low Risk",
        "High Risk"
    ]
)

plt.title(
    "Final Model Confusion Matrix"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.show()
# ------------------------------------------------------------
# 47. FINAL CLASSIFICATION REPORT
# ------------------------------------------------------------
final_report = classification_report(
    y_test,
    final_predictions,
    target_names=[
        "Low Default Risk",
        "High Default Risk"
    ]
)

print("\nFinal Classification Report:")
print(final_report)
# ------------------------------------------------------------
# 48. FINAL TRAINING LOSS
# ------------------------------------------------------------
final_loss = final_model.loss_curve_
plt.figure(figsize=(8, 5))
plt.plot(
    final_loss
)
plt.title(
    "Final Model Training Loss"
)
plt.xlabel(
    "Iterations"
)
plt.ylabel(
    "Loss"
)
plt.grid()
plt.show()
# ------------------------------------------------------------
# 49. TEST NEW APPLICANT USING FINAL MODEL
# ------------------------------------------------------------
new_customer = pd.DataFrame({

    "Age": [45],

    "Income": [40000],

    "LoanAmount": [70000],

    "CreditScore": [570],

    "EmploymentYears": [2],

    "ExistingLoans": [4],

    "MonthlyDebt": [15000],

    "LoanTerm": [60],

    "PreviousDefault": ["Yes"],

    "HomeOwnership": ["Rent"]
})

print("\nNew Customer:")
print(new_customer)
# ------------------------------------------------------------
# 50. TRANSFORM NEW CUSTOMER
# ------------------------------------------------------------
new_customer_processed = preprocessor.transform(
    new_customer
)
# ------------------------------------------------------------
# 51. PREDICT NEW CUSTOMER
# ------------------------------------------------------------
customer_prediction = final_model.predict(
    new_customer_processed
)
customer_probability = final_model.predict_proba(
    new_customer_processed
)
# ------------------------------------------------------------
# 52. DISPLAY NEW CUSTOMER RESULT
# ------------------------------------------------------------
print("========================================")
print("NEW CUSTOMER PREDICTION")
print("========================================")

print(
    "Predicted Class:",
    customer_prediction[0]
)

print(
    "Low Default Risk Probability:",
    customer_probability[0][0]
)

print(
    "High Default Risk Probability:",
    customer_probability[0][1]
)
if customer_prediction[0] == 0:

    print(
        "Result: LOW DEFAULT RISK"
    )

else:

    print(
        "Result: HIGH DEFAULT RISK"
    )
# ============================================================
# END OF ASSIGNMENT
# ============================================================

print("========================================")
print("LOAN DEFAULT PREDICTION COMPLETED")
print("========================================")