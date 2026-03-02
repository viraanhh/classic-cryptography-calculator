import streamlit as st

st.set_page_config(
    page_title="Classic Cryptography Calculator",
    page_icon="🔐",
    layout="centered"
)

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #0f2027, #203a43, #2c5364);
            color: white;
        }
        h1, h2, h3 {
            color: #4FC3F7;
        }
        .stButton>button {
            background-color: #1E88E5;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
        }
        .stTextInput>div>div>input {
            background-color: #E3F2FD;
        }
        .stTextArea textarea {
            background-color: #E3F2FD;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Cryptography Calculator")

st.markdown("""
Selamat datang di **Cryptography Calculator** 

Aplikasi ini menyediakan berbagai algoritma kriptografi klasik:

- 🔢 Affine Cipher
- ⚙️ Enigma / Rotor Cipher 
- 🧮 Hill Cipher
- 🔲 Playfair Cipher
- 🔑 Vigenere Cipher
         

Silakan pilih algoritma melalui sidebar.
""")