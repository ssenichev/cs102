import random
import typing as tp


def is_prime(num: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
    if num % 2 == 0:
        return False

    start = 3
    while start**2 <= num and num % start != 0:
        start += 2
    return start**2 > num


def gcd(num_1: int, num_2: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """

    if a == 0 and b == 0:
        return 0
    elif min(a, b) == 0:
        return max(a, b)
    while b != 0:
        a, b = b, a % b
    return a
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    return num_1


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two number.
    >>> multiplicative_inverse(7, 40)
    23
    """
    t_t = 0
    newt = 1
    r_r = phi
    newr = e

    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if t < 0:
        t += phi
    if r > 1:
        q = r_r // newr
        t_t, newt = newt, t_t - q * newt
        r_r, newr = newr, r_r - q * newr
    if r_r > 1:
        return 0
    if t_t < 0:
        t_t = t_t + phi
    return t_t


def generate_keypair(p: int, q: int) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """
    generating the keypair
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal")

    num = p * q
    phi = (p - 1) * (q - 1)
    n = p * q
    phi = (p-1) * (q-1)
    # Choose an integer e such that e and phi(n) are coprime
    m_e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(m_e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(m_e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, num), (d, num))
    return ((m_e, num), (d, num))


def encrypt(p_k: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    """
    encryption of the text
    """
    # Unpack the key into it's components
    key, num = p_k
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % num for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(p_k: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """
    decryption of the text
    """
    # Unpack the key into its components
    key, num = p_k
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char**key) % num) for char in ciphertext]
    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
