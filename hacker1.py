import secrets
import os
import string

def generator(length):
    alphabet = string.ascii_lowercase + string.digits
    os.system("")
    return ''.join(secrets.choice(alphabet) for _ in range(length))


random_string = generator(26)
print(random_string)
