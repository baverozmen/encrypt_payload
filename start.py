from function import encrypt_file, generate_key, genel_cont
import os

os.system("clear")
file_name = input("dosya adını giriniz: ")
password = input("Şifreleme için bir parola girin: ")
genel_cont(file_name)
generate_key(password)
encrypt_file(f"{file_name}.exe", password)