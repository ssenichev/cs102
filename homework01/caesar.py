import unittest

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
    result = ""

    for i, ch in enumerate(plaintext):
        char = ch
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt_caesar(cipher_text: str, shift: int = 3) -> str:
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

    decrypted = ''
    for i, ch in enumerate(cipher_text):
        char = ch
        if char.isupper():
            decrypted += chr((ord(char) - shift + 65) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - shift + 97 - 12) % 26 + 97)
        else:
            decrypted += char

    return decrypted
