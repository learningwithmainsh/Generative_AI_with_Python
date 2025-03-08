# Import module
import streamlit as st

# Application Title
st.title("Welcome to BMI Calculator! Your own Health Monitor!!!")

# Take Weight
weight = st.number_input("Enter your weight (in Kgs)", min_value=0.0, format="%.2f")

# Take Height
height_unit = st.radio("Select your height format:", ("cms", "meters", "feet"))

# Initialize BMI variable
bmi = None

if height_unit == "cms":
    height = st.number_input("Enter your height in centimeters", min_value=0.0, format="%.2f")
    if height > 0:
        bmi = weight / ((height / 100) ** 2)
    else:
        st.text("Please enter a valid height.")

elif height_unit == "meters":
    height = st.number_input("Enter your height in meters", min_value=0.0, format="%.2f")
    if height > 0:
        bmi = weight / (height ** 2)
    else:
        st.text("Please enter a valid height.")

else:
    height = st.number_input("Enter your height in feet", min_value=0.0, format="%.2f")
    if height > 0:
        bmi = weight / ((height / 3.28) ** 2)
    else:
        st.text("Please enter a valid height.")

# Check if the button is pressed
if st.button("Calculate BMI") and bmi is not None:
    st.text(f"Your BMI is: {round(bmi, 2)}")

    # Display BMI Category
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        st.success("You are Healthy")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight")
    elif bmi >= 30:
        st.error("You are Obese")
