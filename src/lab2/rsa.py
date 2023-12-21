import random
import typing as tp


def is_prime(n: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if b != 0:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.
    >>> multiplicative_inverse(7, 40)
    23
    """
    if gcd(e, phi) != 1:
        return None

    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1

        return gcd, x, y

    _, x, _ = extended_gcd(e, phi)
    while x < 0:
        x += phi
    return x


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal")
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(pk: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    public, private = generate_keypair(p, q)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print(decrypt(public, encrypted_msg))