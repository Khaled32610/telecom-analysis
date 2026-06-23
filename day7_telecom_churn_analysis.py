# Day 7: Loading Data, EDA, and Answering Business Questions using Pandas

import pandas as pd

# 1. Load the dataset
print("1. Loading the dataset...")
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"Current Data Size: {df.shape[0]} rows and {df.shape[1]} columns\n")

# 2. Initial Inspection
print("2. Displaying the first 5 rows:")
print(df.head())
print("-" * 50)

# 3. Data Cleaning (Fixing the TotalCharges trap)
print("3. Cleaning data and checking for missing values...")
# Convert 'TotalCharges' to numeric, forcing spaces to become NaN (Missing Values)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Check the count of missing values after the fix
print("Missing values count per column:")
print(df.isnull().sum())
print("-" * 50)

# 4. Answering Business Questions

# Question 1: Which contract type has the highest churn rate?
print("Q1: Churn rate based on Contract type (%):")
# Convert Churn column to numeric (1 for Yes, 0 for No)
df['Churn_Numeric'] = df['Churn'].map({'Yes': 1, 'No': 0})
churn_by_contract = df.groupby('Contract')['Churn_Numeric'].mean() * 100
print(churn_by_contract.sort_values(ascending=False))
print("-" * 50)

# Question 2: Does tenure correlate with churn?
print("Q2: Average tenure (in months) by Churn status:")
print(df.groupby('Churn')['tenure'].mean())
print("-" * 50)

# Question 3: Which internet services do churned customers use most?
print("Q3: Most used internet services by churned customers:")
# Filter the dataframe for customers who churned
churned_customers = df[df['Churn'] == 'Yes']
print(churned_customers['InternetService'].value_counts())
print("-" * 50)

print("Day 7 script executed successfully!")
