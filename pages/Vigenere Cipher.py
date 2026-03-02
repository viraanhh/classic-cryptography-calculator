import streamlit as st
from utils import vigenere

st.title("Vigenere Cipher")

text_input = st.text_area("Masukkan Teks:")
key = st.text_input("Masukkan Kunci:", "SONY")

mode = st.radio("Mode:", ["Encrypt", "Decrypt"])
mode_val = "encrypt" if mode == "Encrypt" else "decrypt"

if st.button("Proses"):
    result = vigenere(text_input, key, mode_val)
    st.success("Hasil:")
    st.code(result)