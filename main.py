import streamlit as st

#set the app tittle
st.title('My First Streamlit  App')

#display a awelcome message
st.write('Welcome to my first Streamlit app! :books:')

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")
