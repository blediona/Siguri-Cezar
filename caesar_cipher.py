def shift_char(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char


def encrypt_caesar(text, shift):
    encrypted = ""
    for char in text:
        encrypted += shift_char(char, shift)
    return encrypted


def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)
