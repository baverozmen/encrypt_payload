# **encrypt_payload**
This project allows users to perform file encryption operations and generate payloads with MSFvenom. It includes two main files:

- *function.py*: Contains functions for file encryption and MSFvenom payload generation.
- *start.py*: The executable file of the project.

## **Libraries Used**
The following Python libraries are used in this project:

- `cryptography`: Used for AES encryption algorithm for file encryption.
- `subprocess`: Used to run MSFvenom commands.
- `os`: Used for system operations.

---
## **Installation**
Before using the project, you can run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```
```bash

python3 start.py

```
## **File Encryption**
The `encrypt_file` function in the `function.py` file encrypts the given file using the AES algorithm. The encrypted file is saved with a .enc extension.

Functions
- genel_cont(file_name): Creates a Windows Meterpreter reverse TCP payload with MSFvenom.
- generate_key(password): Generates an encryption key using a password.
- encrypt_file(filename, password): Encrypts the file.

---
## **Ethical Warning**
This tool should only be used for *educational purposes*.
Any unauthorized access attempt to systems belonging to others is illegal and unethical.
Please use this tool only in *test environments*. Otherwise, it may result in legal liability.

## **License**
This project is licensed under the [MIT License](LICENSE).

---
*`requirements.txt`*
```txt
cryptography
os
subprocess
```
