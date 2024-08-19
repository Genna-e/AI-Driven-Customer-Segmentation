import pandas as pd

# Absolute paths to your data files
retail_sales_path = 'C:/Users/Elite/AI-Driven-Customer-Segmentation/data/retail_sales_dataset.csv'
ecommerce_data_path = 'C:/Users/Elite/AI-Driven-Customer-Segmentation/data/E-commerce Customer Behavior - Sheet1.csv'

# Load the data
retail_df = pd.read_csv(retail_sales_path)
ecommerce_df = pd.read_csv(ecommerce_data_path)

# Data Cleaning
retail_df.fillna(0, inplace=True)
ecommerce_df.fillna(0, inplace=True)

retail_df.drop_duplicates(inplace=True)
ecommerce_df.drop_duplicates(inplace=True)

# Convert date columns to datetime in retail sales data
retail_df['Date'] = pd.to_datetime(retail_df['Date'])

# Feature Engineering - Calculate RFM Values for Retail Sales Data
latest_date = retail_df['Date'].max()
rfm_retail_df = retail_df.groupby('Customer ID').agg({
    'Date': lambda x: (latest_date - x.max()).days,  # Recency
    'Transaction ID': 'count',                      # Frequency
    'Total Amount': 'sum'                           # Monetary
}).reset_index()

# Rename columns appropriately
rfm_retail_df.columns = ['Customer ID', 'Recency', 'Frequency', 'Monetary']

# Feature Engineering - Calculate RFM Values for E-commerce Data
# Replace 'Customer ID', 'Purchase_Column', and 'Spend_Column' with actual column names in your CSV

rfm_ecommerce_df = ecommerce_df.groupby('Customer ID').agg({
    'Customer ID': 'count',       # Frequency: Number of purchases
    'Total Spend': 'sum'          # Monetary: Total spend
})

# Avoiding column name conflict by renaming the index explicitly before resetting it
rfm_ecommerce_df = rfm_ecommerce_df.rename_axis('index').reset_index()

# Ensure the columns are correctly named after reset
rfm_ecommerce_df.columns = ['Customer ID', 'Frequency', 'Monetary']

# Add a placeholder for Recency if not available
rfm_ecommerce_df['Recency'] = 0  # Placeholder if no date information is available

# Reorder columns to match the RFM standard order
rfm_ecommerce_df = rfm_ecommerce_df[['Customer ID', 'Recency', 'Frequency', 'Monetary']]

# Save Processed Data
rfm_retail_output_path = 'C:/Users/Elite/AI-Driven-Customer-Segmentation/data/rfm_retail_data.csv'
rfm_ecommerce_output_path = 'C:/Users/Elite/AI-Driven-Customer-Segmentation/data/rfm_ecommerce_data.csv'

rfm_retail_df.to_csv(rfm_retail_output_path, index=False)
rfm_ecommerce_df.to_csv(rfm_ecommerce_output_path, index=False)

print("Data pipeline completed. Processed RFM data saved.")
