import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the RFM data
rfm_retail_df = pd.read_csv('data/rfm_retail_clustered.csv')
rfm_ecommerce_df = pd.read_csv('data/rfm_ecommerce_clustered.csv')

# Title of the Web App
st.title("Customer Segmentation using RFM Analysis")

# Select the Dataset to View
dataset = st.selectbox("Select Dataset:", ["Retail", "E-commerce"])

if dataset == "Retail":
    st.header("Retail Data")
    data = rfm_retail_df
else:
    st.header("E-commerce Data")
    data = rfm_ecommerce_df

# Show the Dataframe
st.subheader("Data Preview")
st.dataframe(data.head())

# Plotting the Clusters
st.subheader("RFM Clusters")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Recency', y='Monetary', hue='Cluster', palette='viridis')
plt.title(f'{dataset} Data: RFM Clustering')
plt.xlabel('Recency')
plt.ylabel('Monetary')
st.pyplot(plt)
