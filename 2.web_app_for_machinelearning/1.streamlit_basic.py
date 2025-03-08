# Import Streamlit module
import streamlit as st

# Webpage title 
st.title("Hello! My team!!")

# Success, Info, Warning, Error, Exception messages
st.success("Success")
st.info("Info")
st.warning("Warning")
st.error("Error")

# Correcting the typo in 'exception'
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Checkbox
if st.checkbox("Show/hide"):
    st.text("Showing the message")

# Radio button for city selection
city = st.radio("Select City:", ("Pune", "Bangalore", "Delhi", "Mumbai", "Chennai"))

if city == "Pune":
    st.success("Pune")
elif city == "Bangalore":
    st.success("Bangalore")
elif city == "Delhi":
    st.success("Delhi")
elif city == "Chennai":
    st.success("Chennai")
else:
    st.success("Mumbai")

# Selection Box for single hobby
hobby = st.selectbox("Select a Hobby:", ["Debate", "Reading", "Sport"])
st.write("Your hobby is", hobby)

# Multi-select box for multiple hobbies
hobbies = st.multiselect("Select Multiple Hobbies:", ["Debate", "Reading", "Sport", "Music", "Traveling"])

# Display selected hobbies and count
if hobbies:
    st.write("Your hobbies are:", ", ".join(hobbies))
    st.write("You have selected", len(hobbies), "hobbies.")
else:
    st.write("You haven't selected any hobbies yet.")

# Create a simple button
if st.button("Click Me"):
    st.text("Button Clicked!")

if st.button("See More..."):
    st.text("Button Click Operation is done...")

# Text Input
name = st.text_input("Enter your name", "Type here...")
if st.button("Submit"):
    st.success(f"Hello, {name.title()}!")

# Slider for selecting a level
level = st.slider("Select the level", 1, 10)
st.text(f"Selected:  {level}")

# Command to run this app:
# Run the following command in your terminal:
# streamlit run python_file_name.py
