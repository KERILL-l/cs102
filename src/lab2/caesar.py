def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    if shift > 27:
        return 'Ошибка. Сдвиг больше 27.'
    ciphertext = ''
    alphabet_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 3
    alphabet_low = alphabet_high.lower()
    for letter in plaintext:
        if letter in alphabet_high:
            ciphertext += alphabet_high[alphabet_high.find(letter) + shift]
        elif letter in alphabet_low:
            ciphertext += alphabet_low[alphabet_low.find(letter) + shift]
        else:
            ciphertext += letter
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    if shift > 27:
        return 'Ошибка. Сдвиг больше 27.'
    plaintext = ''
    alphabet_high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_low = alphabet_high.lower()
    for letter in ciphertext:
        if letter in alphabet_high:
            plaintext += alphabet_high[alphabet_high.find(letter) - shift]
        elif letter in alphabet_low:
            plaintext += alphabet_low[alphabet_low.find(letter) - shift]
        else:
            plaintext += letter
    return plaintext
print(encrypt_caesar(''))