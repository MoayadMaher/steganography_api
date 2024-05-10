from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from getpass import getpass


def generate_public_private_keys(): 
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )

    password = getpass("RSA Private Key Passphrase(Leave it empty to ignore password): ").encode('utf-8')
    if password:
        encryption_algorithm = serialization.BestAvailableEncryption(password)

    pem_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm if password else serialization.NoEncryption()
    )

    public_key = private_key.public_key()
    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open("private.pem", "wb") as f:
        f.write(pem_private)

    with open("public.pub", "wb") as f:
        f.write(pem_public)


if __name__ == "__main__":
    generate_public_private_keys()

print("Keys generated successfully")