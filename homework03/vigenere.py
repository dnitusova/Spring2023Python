a = 97
z = 122
A = 65
Z = 90

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""

    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
            continue
        if char.islower():
            new_char = chr(a + ((ord(char) + shift - a) % (z - a + 1)))
        else:
            new_char = chr(A + ((ord(char) + shift - A) % (Z - A + 1)))
        ciphertext += new_char
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = encrypt_caesar(ciphertext, -shift)
    return plaintext

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
    ciphertext = ""
    keynumbers = keyword * (len(plaintext) // len(keyword) + 1)
    keynumbers = [ord(char) - a if char.islower() else ord(char) - A for char in keynumbers]

    for i in range(len(plaintext)):
        ciphertext += encrypt_caesar(plaintext[i], keynumbers[i])
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
    keynumbers = keyword * (len(ciphertext) // len(keyword) + 1)
    keynumbers = [ord(char) - a if char.islower() else ord(char) - A for char in keynumbers]

    for i in range(len(ciphertext)):
        plaintext += decrypt_caesar(ciphertext[i], keynumbers[i])
    return plaintext
