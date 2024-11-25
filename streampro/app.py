import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title and Description
st.title("Interactive Data Visualization App")
st.write("Upload a CSV file and visualize the data interactively!")

# File Upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Load Data
    data = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.write(data.head())

    # Select Columns for Plotting
    columns = data.columns.tolist()
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)
    hue = st.selectbox("Select Hue (Optional)", [None] + columns)

    # Plot
    if x_axis and y_axis:
        st.write(" Bor Plot")
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=data, x=x_axis, y=y_axis, hue=hue)
        plt.title(f"{y_axis} vs {x_axis}")
        st.pyplot(plt)

        # Display correlation
        if pd.api.types.is_numeric_dtype(data[x_axis]) and pd.api.types.is_numeric_dtype(data[y_axis]):
            correlation = data[x_axis].corr(data[y_axis])
            st.write(f"### Correlation: {correlation:.2f}")

else:
    st.write("Upload a CSV file to get started!")

