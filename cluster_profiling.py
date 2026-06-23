import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

print("1. Loading original and cleaned data...")
# Load original data to see actual business values (currency and months) instead of scaled numbers
df_original = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
df_cleaned = pd.read_csv('data/cleaned.csv')

# Quick cleaning for the TotalCharges column in the original data to calculate its mean
df_original['TotalCharges'] = pd.to_numeric(df_original['TotalCharges'], errors='coerce').fillna(0)

print("2. Running K-Means with K=4 (as requested for the final segments)...")
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(df_cleaned)

print("3. Adding cluster labels back to the original dataset...")
# Add a new column to the original dataframe containing the cluster number for each customer
df_original['Cluster'] = cluster_labels

print("4. Building the profile table (calculating means per cluster)...")
# Select key numeric columns and calculate their mean for each cluster
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Cluster']
profile_table = df_original[numeric_cols].groupby('Cluster').mean()

print("5. Generating and saving the Seaborn Heatmap...")
# Create 'outputs' folder to save charts
os.makedirs('outputs', exist_ok=True)

plt.figure(figsize=(10, 6))

# The Heatmap colors the squares based on the values
# annot=True displays the exact numbers inside the squares
sns.heatmap(profile_table, annot=True, fmt=".1f", cmap="YlOrBr", linewidths=.5)

plt.title('Cluster Profiling: Feature Means per Segment')
plt.ylabel('Cluster Segment (0 to 3)')
plt.xlabel('Features')

# Save the image in the outputs folder
heatmap_path = 'outputs/cluster_heatmap.png'
plt.savefig(heatmap_path)
plt.show()

print(f"\nHeatmap saved successfully to {heatmap_path}")