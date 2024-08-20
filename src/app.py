import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load and preprocess data
# Load and preprocess data
@st.cache_data
def load_data():
    retail_df = pd.read_csv('data/retail_sales_dataset.csv')
    ecommerce_df = pd.read_csv('data/E-commerce Customer Behavior - Sheet1.csv')
    
    # Display column names
    st.write("Retail Data Columns:", retail_df.columns.tolist())
    st.write("E-commerce Data Columns:", ecommerce_df.columns.tolist())
    
    # Preprocess retail data
    retail_df['Total_Spent'] = retail_df['Quantity'] * retail_df['Price per Unit']
    retail_df['Segment'] = KMeans(n_clusters=3).fit_predict(retail_df[['Total_Spent', 'Quantity']])
    
    return retail_df, ecommerce_df

# Predict customer segment
def predict_segment(model, total_spent, total_purchase):
    return model.predict([[total_spent, total_purchase]])[0]

# Build recommendation system
def recommend_products(segment):
    recommendations = {
        0: ['Product A', 'Product B', 'Product C'],
        1: ['Product D', 'Product E', 'Product F'],
        2: ['Product G', 'Product H', 'Product I']
    }
    return recommendations.get(segment, [])

# Train a simple classifier for segment prediction
def train_classifier(retail_df):
    X = retail_df[['Total_Spent', 'Quantity']]
    y = retail_df['Segment']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    
    return model, report

# Visualize clusters
def plot_clusters(retail_df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Total_Spent', y='Quantity', hue='Segment', data=retail_df, palette="deep")
    plt.title("Customer Segments")
    st.pyplot(plt)

def main():
    st.title("AI-Driven Customer Segmentation and Prediction")
    
    # Load data
    retail_df, ecommerce_df = load_data()
    
    # Train classifier
    model, report = train_classifier(retail_df)
    
    # Input fields for prediction
    st.header("Predict Customer Segment")
    total_spent = st.number_input("Total Spent ($)", value=500.00)
    total_purchase = st.number_input("Total Purchase ($)", value=300.00)
    
    # Predict and display the segment
    predicted_segment = predict_segment(model, total_spent, total_purchase)
    st.write(f"The predicted customer segment is: {predicted_segment}")
    
    # Display model performance
    st.header("Model Performance")
    st.json(report)
    
    # Recommend products
    st.header("Recommended Products")
    recommended_products = recommend_products(predicted_segment)
    st.write("Recommended Products for this Customer:")
    st.write(recommended_products)
    
    # Visualize clusters
    st.header("Customer Segments Visualization")
    plot_clusters(retail_df)

if __name__ == "__main__":
    main()
