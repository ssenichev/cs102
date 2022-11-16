start_lowercase = ord("a")
start_uppercase = ord("A")
alph_length = ord("z") - ord("a") + 1
start_lowercase = ord('a')
start_uppercase = ord('A')


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

    for c in plaintext:
        char = c
        if char.isupper():
            result += chr((ord(char) + shift - start_uppercase) % alph_length + start_uppercase)
        elif char.islower():
            result += chr((ord(char) + shift - start_lowercase) % alph_length + start_lowercase)
            result += chr((ord(char) + shift - start_uppercase) % 26 + start_uppercase)
        elif char.islower():
            result += chr((ord(char) + shift - start_lowercase) % 26 + start_lowercase)
        else:
            result += char

    return result


def decrypt_caesar(cipher_text: str, shift: int = 3) -> str:
    """
    decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    decrypted = ""
    for c in cipher_text:
        char = c
        if char.isupper():
            decrypted += chr((ord(char) - shift - start_uppercase) % alph_length + start_uppercase)
        elif char.islower():
            decrypted += chr((ord(char) - shift - start_lowercase) % alph_length + start_lowercase)
            decrypted += chr((ord(char) - shift - start_uppercase) % 26 + start_uppercase)
        elif char.islower():
            decrypted += chr((ord(char) - shift - start_lowercase) % 26 + start_lowercase)
        else:
            decrypted += char

    return decrypted
