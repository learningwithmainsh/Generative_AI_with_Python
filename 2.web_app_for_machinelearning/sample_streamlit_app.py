import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Add a subheader
st.subheader("Welcome to your first Streamlit app!")

# User input for name
name = st.text_input("Enter your name:", "")

# Display greeting if the user enters their name
if name:
    st.write(f"Hello, **{name}**! 👋")

# Add a slider to select a number
number = st.slider("Select a number:", 1, 100, 25)
st.write(f"You selected: {number}")

# Generate random data for a chart
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(1, number, size=10)
})

# Display the data in a table
st.write("Generated Data:", data)

# Display the data as a line chart
st.line_chart(data.set_index('x'))

# Add a button
if st.button("Click me!"):
    st.success("You clicked the button!")

# Add a sidebar
st.sidebar.header("Sidebar")
option = st.sidebar.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"You selected: {option}")
