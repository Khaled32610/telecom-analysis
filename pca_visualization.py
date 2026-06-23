import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

print("1. Loading the cleaned data...")
df_cleaned = pd.read_csv('data/cleaned.csv')

# Choosing K=3 based on the elbow curve
print("2. Running K-Means with K=3...")
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# fit_predict fits the model and directly gives each customer a cluster label (0, 1, or 2)
cluster_labels = kmeans.fit_predict(df_cleaned)

print("3. Applying PCA to reduce data to 2 dimensions...")
pca = PCA(n_components=2)
# Compressing the 20+ columns into just 2 columns
pca_data = pca.fit_transform(df_cleaned)

print("4. Plotting the customer clusters...")
plt.figure(figsize=(10, 7))

# Scatter plot: 
# x = First PCA column, y = Second PCA column
# c = Color based on cluster label
scatter = plt.scatter(pca_data[:, 0], pca_data[:, 1], c=cluster_labels, cmap='viridis', alpha=0.6)

plt.title('Customer Segments in 2D using PCA')
plt.xlabel('Principal Component 1 (Main features summary)')
plt.ylabel('Principal Component 2 (Secondary features summary)')

# Adding a legend (colorbar) to show which color belongs to which cluster
plt.colorbar(scatter, label='Cluster Label (0, 1, 2)')
plt.grid(True)
plt.show()