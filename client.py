import socket
import ceaser_cipher
import diffi_helman

def client_program():
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))

    diffi_helman.diffe_helman()
    shared_key = diffi_helman.power(9, 3, 23) 

    print(f"Shared Key: {shared_key}")

    message = input("Enter the message: ")

    while message.lower().strip() != 'bye':
        encrypted_text = ceaser_cipher.encryption_ceaser_cipher(message, shared_key)
        client_socket.send(encrypted_text.encode())

        data = client_socket.recv(1024).decode()
        decrypted_data = ceaser_cipher.decryption_ceaser_cipher(data, shared_key)
        print("Server:", decrypted_data)

        message = input("Enter the message: ")

    client_socket.close()

client_program()
