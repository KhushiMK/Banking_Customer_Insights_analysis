import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Preview
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# -------------------------
# DATA CLEANING
# -------------------------

# Fill missing values
df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)
df['Married'].fillna(df['Married'].mode()[0], inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0], inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# -------------------------
# EDA (ANALYSIS)
# -------------------------

# 1. Loan Status Distribution
sns.countplot(x='Loan_Status', data=df)
plt.title("Loan Approval Distribution")
plt.savefig("loan_status.png")
plt.clf()

# 2. Income vs Loan Amount
sns.scatterplot(x='ApplicantIncome', y='LoanAmount', data=df)
plt.title("Income vs Loan Amount")
plt.savefig("income_vs_loan.png")
plt.clf()

# 3. Credit History vs Loan Approval
sns.countplot(x='Credit_History', hue='Loan_Status', data=df)
plt.title("Credit History Impact")
plt.savefig("credit_history.png")
plt.clf()

# 4. Gender vs Loan Approval
sns.countplot(x='Gender', hue='Loan_Status', data=df)
plt.title("Gender vs Loan Approval")
plt.savefig("gender_loan.png")
plt.clf()

# 5. Education vs Loan Approval
sns.countplot(x='Education', hue='Loan_Status', data=df)
plt.title("Education vs Loan Approval")
plt.savefig("education_loan.png")
plt.clf()

print("\nAnalysis completed! Graphs saved as images.")