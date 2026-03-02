import streamlit as st

st.title("Rotor Cipher")

plaintext = st.text_input("Masukkan Teks").upper()

st.subheader("Masukkan 3 Kunci Substitusi")

k0 = st.text_input("K0").upper()
k1 = st.text_input("K1").upper()
k2 = st.text_input("K2").upper()

start_pos = st.number_input("Posisi Awal Rotor", min_value=0, max_value=2, value=0)

def valid_keys(k0, k1, k2):
    if len(k0) != len(k1) or len(k1) != len(k2):
        return False
    
    if len(set(k0)) != len(k0):
        return False
    
    if set(k0) != set(k1) or set(k1) != set(k2):
        return False
    
    return True

def rotor_process(text, keys, alphabet, start_pos, mode):
    result = ""
    rotor_pos = start_pos

    for char in text:
        if char not in alphabet:
            return "Error: Teks mengandung huruf di luar alfabet."
        
        if mode == "Encrypt":
            idx = alphabet.index(char)
            result += keys[rotor_pos][idx]
        else:  # Decrypt
            idx = keys[rotor_pos].index(char)
            result += alphabet[idx]

        rotor_pos = (rotor_pos + 1) % len(keys)

    return result

if valid_keys(k0, k1, k2):

    alphabet = k0
    keys = [k0, k1, k2]

    mode = st.radio("Mode", ["Encrypt", "Decrypt"])

    if st.button("Proses"):
        result = rotor_process(plaintext, keys, alphabet, start_pos, mode)
        st.success("Hasil:")
        st.code(result)

else:
    st.warning("Kunci harus memiliki panjang sama, huruf unik, dan berisi himpunan huruf yang sama.")