import streamlit as st

st.title("BMI Calculator")

height = st.number_input("Enter your height in meters", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Enter your weight in kg", min_value=10.0, max_value=300.0, step=0.5)

if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"Your BMI is **{bmi:.2f}**")

        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")
    else:
        st.error("Please enter a valid height")
