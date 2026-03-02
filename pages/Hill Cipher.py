import streamlit as st
import numpy as np
from utils import hill

st.title("Hill Cipher")

text_input = st.text_area("Masukkan Teks:")

size = st.selectbox(
    "Pilih Ukuran Matriks:",
    [2, 3, 4, 5],
    index=1
)

st.subheader(f"Input Matriks Kunci ({size}x{size})")

matrix_values = []

for i in range(size):
    cols = st.columns(size)
    row = []
    for j in range(size):
        value = cols[j].number_input(
            f"K{i+1}{j+1}",
            value=1 if i == j else 0,
            step=1,
            key=f"{i}-{j}"
        )
        row.append(value)
    matrix_values.append(row)

key_matrix = np.array(matrix_values) % 26

mode = st.radio("Mode:", ["Encrypt", "Decrypt"])
mode_val = "encrypt" if mode == "Encrypt" else "decrypt"

if st.button("Proses"):
    result = hill(text_input, key_matrix, mode_val)
    st.success("Hasil:")
    st.code(result)