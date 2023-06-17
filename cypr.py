from cryptography import fernet

key = fernet.Fernet.generate_key()

f = fernet.Fernet(key)

token = f.encrypt(b"my deep dark secret ")
print(f'my key = {key.decode()} and token = {token.decode()}')

message = f.decrypt(token=token)
print(message.decode())