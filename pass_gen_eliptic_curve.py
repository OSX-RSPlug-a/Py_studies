import hashlib
import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
#pip install cryptography


private_key = ec.generate_private_key(ec.SECP256R1())

k = private_key.private_numbers().private_value.to_bytes(32, 'big')

K = private_key.public_key()

K_bytes = K.public_bytes(Encoding.X962, PublicFormat.CompressedPoint)

password = base64.urlsafe_b64encode(hashlib.sha256(k).digest()).decode()[:20]


print(f"Private key (hex): {k.hex()[:32]} ")
print(f"Public key (hex):  {K_bytes.hex()[:32]} ")
print(f"Password:         {password}")