import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

print("1. Loading the raw dataset...")
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# ==========================================
# Step 1: Clean the dataset
# ==========================================

# 1. Drop useless columns
# 'customerID' is just an identifier and adds no predictive value
df.drop('customerID', axis=1, inplace=True)

# 2. Fix the TotalCharges column
# Convert string to float, and fill missing values (NaN) with 0
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna(0, inplace=True)

# 3. Binary Encoding
# Convert Yes/No columns to 1/0
binary_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
for col in binary_cols:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# 4. One-Hot Encoding
# Convert remaining categorical text columns into 1/0 dummy variables
df_encoded = pd.get_dummies(df, drop_first=True)

# ==========================================
# Step 2: Prepare for clustering (K-Means)
# ==========================================

print("2. Preparing data for K-Means clustering...")

# 1. Drop the target label (Churn)
# K-Means is an unsupervised learning algorithm, so it doesn't need the answer labels
if 'Churn_Yes' in df_encoded.columns:
    df_encoded.drop('Churn_Yes', axis=1, inplace=True)

# 2. Feature Scaling
# K-Means is distance-based. Scaling ensures all features have equal weight (mean=0, variance=1)
scaler = StandardScaler()
scaled_matrix = scaler.fit_transform(df_encoded)

# Convert the resulting numpy array back to a Pandas DataFrame
df_final = pd.DataFrame(scaled_matrix, columns=df_encoded.columns)

# ==========================================
# Step 3: Save cleaned data
# ==========================================

# Create a 'data' folder if it doesn't exist, and save the CSV
os.makedirs('data', exist_ok=True)
df_final.to_csv('data/cleaned.csv', index=False)

print("\nProcess completed successfully!")
print(f"Final ML-ready dataset shape: {df_final.shape[0]} rows and {df_final.shape[1]} columns.")
print("Saved to: data/cleaned.csv")