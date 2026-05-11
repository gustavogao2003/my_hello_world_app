import streamlit as st

st.title('🎈 Hello World App!!!')

st.write('This is my first Streamlit App!')

x = st.slider("Select a value")
st.write(x, "squared is", x * x)
