import re
import typing as tp

a = 97
z = 122
A = 65
Z = 90
rus_first_cap = 1040
rus_first_lower = 1072
rus_last_cap = 1071
rus_last_lower = 1103

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
    ciphertext = ""
    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
            continue
        if bool(re.search("[А-Яа-я]", char)):
            if char.islower():
                new_char = chr(rus_first_lower + ((ord(char) + shift - rus_first_lower) % (rus_last_lower - rus_first_lower + 1)))
            else:
                new_char = chr(rus_first_cap + ((ord(char) + shift - rus_first_cap) % (rus_last_cap - rus_first_cap + 1)))
        else:
            if char.islower():
                new_char = chr(a + ((ord(char) + shift - a) % (z - a + 1)))
            else:
                new_char = chr(A + ((ord(char) + shift - A) % (Z - A + 1)))
        ciphertext += new_char
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
    plaintext = encrypt_caesar(ciphertext, -shift)
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
