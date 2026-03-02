import streamlit as st
from utils import playfair

st.title("Playfair Cipher")

text_input = st.text_area("Masukkan Teks:")
key = st.text_input("Masukkan Kunci:", "GADJAH")

mode = st.radio("Mode:", ["Encrypt", "Decrypt"])
mode_val = "encrypt" if mode == "Encrypt" else "decrypt"

if st.button("Proses"):
    result = playfair(text_input, key, mode_val)
    st.success("Hasil:")
    st.code(result)