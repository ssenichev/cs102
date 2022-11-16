start_lowercase = ord("a")
start_uppercase = ord("A")
alph_length = ord("z") - ord("a") + 1


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
    result = ""
    shift = [keyword[i % len(keyword)] for i in range(len(plaintext))]

    for i, char in enumerate(plaintext):
        if char.isupper():
            result += chr(
                (ord(char) + (ord(shift[i]) % start_uppercase) - start_uppercase) % alph_length + start_uppercase
            )
        elif char.islower():
            result += chr(
                (ord(char) + (ord(shift[i]) % start_lowercase) - start_lowercase) % alph_length + start_lowercase
            )
        else:
            result += char
    return result


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
    result = ""
    shift = [keyword[i % len(keyword)] for i in range(len(ciphertext))]

    for i, char in enumerate(ciphertext):
        if char.isupper():
            result += chr(
                (ord(char) - (ord(shift[i]) % start_uppercase) - start_uppercase) % alph_length + start_uppercase
            )
        elif char.islower():
            result += chr(
                (ord(char) - (ord(shift[i]) % start_lowercase) - start_lowercase) % alph_length + start_lowercase
            )
        else:
            result += char
    return result
