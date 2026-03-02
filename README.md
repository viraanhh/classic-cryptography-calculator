# Classic Cryptography Calculator

## Overview

Classic Cryptography Calculator is a web-based cryptography application developed using **Python** and the **Streamlit** framework.

This application implements several classical cryptographic algorithms in an interactive format to help users understand encryption and decryption processes in a visual and practical way.

---

## Project Objectives

The main objectives of this project are:

- To help users understand fundamental concepts of classical cryptography  
- To provide interactive encryption and decryption simulations  
- To implement mathematical cryptographic algorithms into a functional web application  
- To serve as a learning medium for Cryptography coursework  

---

## Technologies Used

- Python  
- Streamlit  
- NumPy  
- Git & GitHub  

---

## Implemented Algorithms

### Affine Cipher

A linear substitution cipher defined by the formula:

#### Encryption
```text
C = (aP + b) mod 26
```

#### Decryption
```text
P = a⁻¹(C - b) mod 26
```

**Features:**

- Text input  
- Custom key input (`a` and `b`)  
- Modular inverse validation  
- Encrypt / Decrypt mode  

---

### Vigenère Cipher

A polyalphabetic substitution cipher using a keyword.

#### Formula
```text
C = (P + K) mod 26
```

**Features:**

- Text input  
- Keyword input  
- Encrypt / Decrypt mode  

---

### Playfair Cipher

A digraph substitution cipher using a 5×5 key matrix.

**Features:**

- 5×5 key matrix (I/J combined)  
- Letter pairing process  
- Encrypt / Decrypt mode  

---

### Hill Cipher

A matrix-based cipher using matrix multiplication modulo 26.

**Features:**

- Matrix size selection (2×2 up to 5×5)  
- Custom key matrix input  
- Determinant calculation  
- Modular inverse matrix computation  
- Encrypt / Decrypt mode  

---

### Rotor Cipher (Simplified Enigma Simulation)

A simplified simulation of a rotor-based encryption system inspired by the Enigma machine.

**Features:**

- Three rotor substitution inputs  
- Unique character validation  
- Initial rotor position setting  
- Automatic rotor rotation mechanism  
- Encrypt / Decrypt mode  

> Note:  
> This version is a simplified simulation and does not include reflector or plugboard components found in the original Enigma machine.

---

## Application Workflow

1. The user enters text and cryptographic keys  
2. The system validates the input  
3. The selected algorithm function is called from `utils.py`  
4. The encryption/decryption process is executed  
5. The result is displayed on the web interface  

---

## Project Structure

```bash
classic-cryptography-calculator/
│
├── Home.py
├── utils.py
├── requirements.txt
│
└── pages/
    ├── Affine Cipher.py
    ├── Enigma Cipher.py
    ├── Hill Cipher.py
    ├── Playfair Cipher.py
    └── Vigenere Cipher.py
```

---

## How to Run the Application

### Clone the repository

```bash
git clone https://github.com/viraanhh/classic-cryptography-calculator.git
```

### Navigate to the project folder

```bash
cd classic-cryptography-calculator
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run Home.py
```
