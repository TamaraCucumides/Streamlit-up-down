import streamlit as st

st.title("Hola")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    st.write("Subiste algo!")

    st.download_button(
    label="Download data as CSV",
    data=uploaded_file,
    file_name='archivo_descargado.csv',
    mime='text/csv',
)