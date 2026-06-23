# Telecom Customer Churn Analysis & Segmentation

## 📌 Overview
This project focuses on analyzing telecom customer data to understand churn rates and grouping customers into natural segments using **Unsupervised Machine Learning (K-Means Clustering)**. The goal is to extract actionable business insights to improve customer retention.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas
* **Machine Learning:** Scikit-Learn (K-Means, PCA, StandardScaler)
* **Data Visualization:** Matplotlib, Seaborn

## 📂 Project Structure
* `pandas_eda.py`: Initial data exploration, handling missing values, and answering business questions using Pandas.
* `data_cleaning_scaling.py`: Data preprocessing, One-Hot Encoding, and feature scaling.
* `kmeans_elbow.py`: Finding the optimal number of clusters (K) using the Elbow Method and Silhouette Score, plus 2D PCA visualization.
* `cluster_profiling.py`: Generating a Seaborn heatmap to profile each cluster and extract business strategies.
* `data/`: Contains the raw and cleaned CSV datasets.
* `outputs/`: Contains generated visualizations (e.g., `cluster_heatmap.png`).

## 📊 Key Business Insights (Customer Segments)
Based on the K-Means clustering (K=4), we identified four distinct customer profiles:
1. **Loyal VIPs (Cluster 2):** Longest tenure (~56 months) and highest monthly charges. *Strategy: Provide loyalty programs and VIP support.*
2. **High-Risk Spenders (Cluster 1):** High monthly charges but very short tenure (~15 months). *Strategy: Immediate retention efforts and discounted annual contracts.*
3. **Steady Average (Cluster 0):** Average tenure and average monthly charges. *Strategy: Gentle upselling to higher-tier plans.*
4. **Budget Catch (Cluster 3):** Average tenure but lowest monthly charges. *Strategy: Maintain stable essential services without aggressive marketing.*

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/Khaled32610/Pandas-Telecom-Churn-Analysis.git](https://github.com/Khaled32610/Pandas-Telecom-Churn-Analysis.git)