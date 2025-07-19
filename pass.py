import secrets
import string

def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Example usage
print("Secure password:", generate_secure_password(16))
print("Here's your uncrackable password just copy it!!! :")
