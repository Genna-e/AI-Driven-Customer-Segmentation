import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load the RFM data
retail_sales_path = 'C:/Users/Elite/AI-Driven-Customer-Segmentation/data/rfm_retail_data.csv'
ecommerce_data_path = 'C:/Users/Elite/AI-Driven-Customer-Segmentation/data/rfm_ecommerce_data.csv'

rfm_retail_df = pd.read_csv(retail_sales_path)
rfm_ecommerce_df = pd.read_csv(ecommerce_data_path)

# Select the RFM features for clustering
X_retail = rfm_retail_df[['Recency', 'Frequency', 'Monetary']]
X_ecommerce = rfm_ecommerce_df[['Recency', 'Frequency', 'Monetary']]

# Apply K-Means Clustering for Retail Data
kmeans_retail = KMeans(n_clusters=4, random_state=42)
kmeans_retail.fit(X_retail)
rfm_retail_df['Cluster'] = kmeans_retail.labels_

# Apply K-Means Clustering for E-commerce Data
kmeans_ecommerce = KMeans(n_clusters=4, random_state=42)
kmeans_ecommerce.fit(X_ecommerce)
rfm_ecommerce_df['Cluster'] = kmeans_ecommerce.labels_

# Save the clustered data
rfm_retail_df.to_csv('C:/Users/Elite/AI-Driven-Customer-Segmentation/data/rfm_retail_clustered.csv', index=False)
rfm_ecommerce_df.to_csv('C:/Users/Elite/AI-Driven-Customer-Segmentation/data/rfm_ecommerce_clustered.csv', index=False)

# Visualize the Clusters for Retail Data
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rfm_retail_df, x='Recency', y='Monetary', hue='Cluster', palette='viridis')
plt.title('Retail Data: RFM Clustering')
plt.xlabel('Recency')
plt.ylabel('Monetary')
plt.show()

# Visualize the Clusters for E-commerce Data
plt.figure(figsize=(10, 6))
sns.scatterplot(data=rfm_ecommerce_df, x='Recency', y='Monetary', hue='Cluster', palette='viridis')
plt.title('E-commerce Data: RFM Clustering')
plt.xlabel('Recency')
plt.ylabel('Monetary')
plt.show()

print("Clustering and visualization completed.")
