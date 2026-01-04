import streamlit as st
from factorial import factorial

#calculator with streamlit
st.title("Factorial Calculator")
st.write("Enter a non-negative integer to compute its factorial.")  
number = st.number_input("Enter a non-negative integer:", min_value=0, step=1)

if st.button("Calculate Factorial"):
    result = factorial(number)
    st.success(f"The factorial of {number} is {result}")
    
    st.balloons()