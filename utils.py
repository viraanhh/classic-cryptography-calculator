import numpy as np
import string

def clean_text(text):
    """Membersihkan teks: hanya huruf dan diubah ke uppercase"""
    return ''.join([c for c in text.upper() if c in string.ascii_uppercase])


def mod_inverse(a, m):
    """Mencari modular inverse dari a mod m"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def vigenere(text, key, mode='encrypt'):
    text = clean_text(text)
    key = clean_text(key)

    if not key:
        return text

    result = ""
    key_idx = 0

    for char in text:
        p = ord(char) - 65
        k = ord(key[key_idx % len(key)]) - 65

        if mode == 'encrypt':
            c = (p + k) % 26
        else:
            c = (p - k) % 26

        result += chr(c + 65)
        key_idx += 1

    return result

def affine(text, a, b, mode='encrypt'):
    text = clean_text(text)
    result = ""

    if mode == 'encrypt':
        for char in text:
            p = ord(char) - 65
            c = (a * p + b) % 26
            result += chr(c + 65)

    else:
        a_inv = mod_inverse(a, 26)
        if a_inv is None:
            return "Error: 'a' tidak memiliki invers modulo 26!"

        for char in text:
            c = ord(char) - 65
            p = (a_inv * (c - b)) % 26
            result += chr(p + 65)

    return result

def generate_playfair_matrix(key):
    key = clean_text(key).replace('J', 'I')
    matrix = []
    used = set()

    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
            used.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return -1, -1


def playfair(text, key, mode='encrypt'):
    text = clean_text(text).replace('J', 'I')
    matrix = generate_playfair_matrix(key)

    if mode == 'encrypt':
        i = 0
        prepared_text = ""

        while i < len(text):
            prepared_text += text[i]

            if i + 1 < len(text):
                if text[i] == text[i+1]:
                    prepared_text += 'Q'
                else:
                    prepared_text += text[i+1]
                    i += 1
            i += 1

        if len(prepared_text) % 2 != 0:
            prepared_text += 'Q'

        text = prepared_text

    result = ""
    shift = 1 if mode == 'encrypt' else -1

    for i in range(0, len(text), 2):
        r1, c1 = find_position(matrix, text[i])
        r2, c2 = find_position(matrix, text[i+1])

        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]

        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result

def hill(text, key_matrix, mode='encrypt'):
    import numpy as np

    text = clean_text(text)
    n = key_matrix.shape[0]

    while len(text) % n != 0:
        text += 'X'

    result = ""

    if mode == 'encrypt':
        for i in range(0, len(text), n):
            block = text[i:i+n]
            P = np.array([[ord(char)-65] for char in block])
            C = np.dot(key_matrix, P) % 26
            result += ''.join([chr(int(num)+65) for num in C.flatten()])

    else:
        det = int(round(np.linalg.det(key_matrix))) % 26
        det_inv = mod_inverse(det, 26)

        if det_inv is None:
            return "Error: Matriks tidak memiliki invers modulo 26."

        # Cari matriks kofaktor (adjugate)
        cofactors = np.zeros((n,n))

        for r in range(n):
            for c in range(n):
                minor = np.delete(np.delete(key_matrix, r, axis=0), c, axis=1)
                cofactors[r][c] = ((-1)**(r+c)) * int(round(np.linalg.det(minor)))

        adj = cofactors.T % 26
        K_inv = (det_inv * adj) % 26

        for i in range(0, len(text), n):
            block = text[i:i+n]
            C = np.array([[ord(char)-65] for char in block])
            P = np.dot(K_inv, C) % 26
            result += ''.join([chr(int(num)+65) for num in P.flatten()])

    return result

def enigma_rotor(text, mode='encrypt'):
    text = clean_text(text)

    R0 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    R1 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    R2 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

    rotors = [R0, R1, R2]
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""

    for i, char in enumerate(text):
        pos = i % 3

        if mode == 'encrypt':
            idx = alphabet.find(char)
            result += rotors[pos][idx]
        else:
            idx = rotors[pos].find(char)
            result += alphabet[idx]

    return result