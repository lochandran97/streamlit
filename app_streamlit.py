import streamlit as st
#from factorial import factorial

#calculator with streamlit
st.title("Factorial Calculator")
st.write("Enter a non-negative integer to compute its factorial.")  
number = st.number_input("Enter a non-negative integer:", min_value=0, step=1)

def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if st.button("Calculate Factorial"):
    result = factorial(number)
    st.success(f"The factorial of {number} is {result}")
    
    st.balloons()
