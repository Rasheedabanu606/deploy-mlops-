import streamlit as st
import pickle

# Load the pickled model
with open('modelsal.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web app
st.header("Streamlit demo")

st.sidebar.header("This is a web app")

exp = st.sidebar.slider("Select Exp to get salary", 0, 10, 5)

st.write("Experience is:", exp)

salary = model.predict([[exp]])

# st.write("b0 is", round(model.intercept_, 3))
# st.write("b1 is", round(model.coef_[0], 3))
st.write("Salary is", salary)
