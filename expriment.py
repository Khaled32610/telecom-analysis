import pandas as pd

# 1. Load the dataset
print("1. Loading the dataset...")
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# السطر اللي كان ناقص: تحويل عمود Churn لأرقام (1 و 0) عشان نقدر نحسبه
df['Churn_Numeric'] = df['Churn'].map({'Yes': 1, 'No': 0})

# حساب نسبة التسرب لكبار السن مقابل الفئات الأخرى
senior_churn = df.groupby('SeniorCitizen')['Churn_Numeric'].mean() * 100

print("--- Churn Rate by Senior Citizen Status (%) ---")
print(senior_churn)

# حساب نسبة التسرب بناءً على كل طريقة دفع
payment_churn = df.groupby('PaymentMethod')['Churn_Numeric'].mean() * 100

print("\n--- Churn Rate by Payment Method (%) ---")
print(payment_churn.sort_values(ascending=False))