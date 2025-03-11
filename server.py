import socket
import ceaser_cipher
import diffi_helman

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    conn, address = server_socket.accept()
    
    diffi_helman.diffe_helman()
    shared_key = diffi_helman.power(9, 5, 23)

    print(f"Shared Key: {shared_key}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        decrypted_data = ceaser_cipher.decryption_ceaser_cipher(data, shared_key)
        print("Client:", decrypted_data)

        data = input('Enter the message: ')
        encrypted_data = ceaser_cipher.encryption_ceaser_cipher(data, shared_key)
        conn.send(encrypted_data.encode())

    conn.close()

server_program()
