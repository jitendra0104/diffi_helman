def encryption_ceaser_cipher(plain_text, num):
    cipher_text = ""
    for i in plain_text:
        if i.isalpha():
            if i.islower():
                new_char = chr(((ord(i) - ord('a') + num) % 26) + ord('a'))
            else:
                new_char = chr(((ord(i) - ord('A') + num) % 26) + ord('A'))
            cipher_text += new_char
        else:
            cipher_text += i
    return cipher_text

def decryption_ceaser_cipher(cipher_text, num):
    plain_text = ""
    for i in cipher_text:
        if i.isalpha():
            if i.islower():
                new_char = chr(((ord(i) - ord('a') - num) % 26) + ord('a'))
            else:
                new_char = chr(((ord(i) - ord('A') - num) % 26) + ord('A'))
            plain_text += new_char
        else:
            plain_text += i
    return plain_text
