from math import ceil


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    alphabet_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 4
    alphabet_low = alphabet_high.lower()
    key = str(keyword * ceil(len(plaintext) / len(keyword)))[:len(plaintext)]
    keys = [alphabet_high.find(s.upper()) for s in key]
    i = 0
    for letter in plaintext:
        if letter in alphabet_high:
            ciphertext += alphabet_high[alphabet_high.find(letter) + keys[i]]
            i += 1
        elif letter in alphabet_low:
            ciphertext += alphabet_low[alphabet_low.find(letter) + keys[i]]
            i += 1
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alphabet_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 4
    alphabet_low = alphabet_high.lower()
    key = str(keyword * ceil(len(ciphertext) / len(keyword)))[:len(ciphertext)]
    keys = [alphabet_high.find(s.upper()) for s in key]
    i = 0
    for letter in ciphertext:
        if letter in alphabet_high:
            plaintext += alphabet_high[alphabet_high.find(letter) - keys[i]]
            i += 1
        elif letter in alphabet_low:
            plaintext += alphabet_low[alphabet_low.find(letter) - keys[i]]
            i += 1
        else:
            plaintext += letter
    return plaintext


print(encrypt_vigenere('ATTACKATDAWN', 'LEMON'))
print(decrypt_vigenere('LXFOPVEFRNHR', 'LEMON'))