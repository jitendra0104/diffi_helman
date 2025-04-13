from py_ecc.bls.ciphersuites import G2ProofOfPossession as bls
import hashlib

# Function to generate private and public key for a client
def generate_keys(client_id):
    private_key = bls.KeyGen(int.to_bytes(client_id, length=32, byteorder='big'))
    public_key = bls.SkToPk(private_key)
    return private_key, public_key

# Function to sign a message using the private key
def sign_message(private_key, message):
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = bls.Sign(private_key, message_hash)
    return signature, message_hash

# Function to verify the signature using public key and message hash
def verify_signature(public_key, message_hash, signature):
    return bls.Verify(public_key, message_hash, signature)

# Simulate the digital signature process for multiple clients
def simulate():
    for client_id in range(1, 4):  # Simulating 3 clients
        # Generate key pair
        private_key, public_key = generate_keys(client_id)

        # Prepare and sign message
        message = f"Hello from client {client_id}"
        signature, message_hash = sign_message(private_key, message)

        print(f"[Client {client_id}] Message: '{message}'")

        # Server verifies the signature
        is_valid = verify_signature(public_key, message_hash, signature)
        print(f"-> Signature valid: {is_valid}\n")

simulate()