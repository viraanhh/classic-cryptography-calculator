import streamlit as st
from utils import affine

st.title("Affine Cipher")

st.info("Kunci 'a' harus relatif prima dengan 26")

text_input = st.text_area("Masukkan Teks:")
col1, col2 = st.columns(2)

with col1:
    a = st.number_input("Kunci a:", value=7, step=1)
with col2:
    b = st.number_input("Kunci b:", value=10, step=1)

mode = st.radio("Mode:", ["Encrypt", "Decrypt"])
mode_val = "encrypt" if mode == "Encrypt" else "decrypt"

if st.button("Proses"):
    result = affine(text_input, int(a), int(b), mode_val)
    st.success("Hasil:")
    st.code(result)