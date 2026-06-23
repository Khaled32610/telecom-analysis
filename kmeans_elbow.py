import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

print("1. Loading the cleaned data from Day 8...")
df_cleaned = pd.read_csv('data/cleaned.csv')

# Initialize empty lists to store evaluation metrics
inertias = []
silhouette_scores = []
k_range = range(2, 9)  # Testing cluster sizes from 2 to 8

print("2. Running K-Means and calculating scores. Please wait...\n")

# Loop through each K to find the optimal number of clusters
for k in k_range:
    # Initialize the K-Means model
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    
    # Fit the model to the cleaned data
    kmeans.fit(df_cleaned)
    
    # Save the Inertia (measures how tightly grouped the clusters are)
    inertias.append(kmeans.inertia_)
    
    # Calculate and save the Silhouette Score (measures separation distance between clusters)
    score = silhouette_score(df_cleaned, kmeans.labels_)
    silhouette_scores.append(score)
    
    print(f"K = {k} | Inertia: {kmeans.inertia_:.2f} | Silhouette Score: {score:.4f}")

# ==========================================
# Final Step: Plotting the Elbow Curve
# ==========================================
print("\n3. Plotting the Elbow Curve...")

plt.figure(figsize=(8, 5))
plt.plot(k_range, inertias, marker='o', linestyle='-', color='b')
plt.title('Elbow Curve to Find Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()