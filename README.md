# encrypt_payload

Bu proje, kullanıcıların dosya şifreleme işlemleri ve MSFvenom ile payload üretme işlemleri yapmalarını sağlar. İki ana dosya içerir:

- **function.py**: Dosya şifreleme ve MSFvenom payload oluşturma işlemleri için fonksiyonlar içerir.
- **start.py**: Projenin çalıştırılabilir dosyasıdır.

## Kullanılan Kütüphaneler

Bu projede aşağıdaki Python kütüphaneleri kullanılmaktadır:

- `cryptography`: Dosya şifreleme işlemleri için AES şifreleme algoritması kullanılır.
- `subprocess`: MSFvenom komutlarını çalıştırmak için kullanılır.
- `os`: Sistem işlemleri için kullanılır.


---

## Kurulum

Projeyi kullanmadan önce gerekli kütüphaneleri yüklemek için şu komutu çalıştırabilirsiniz:

```bash
pip install -r requirements.txt
```
```bash

python3 start.py

```
# Dosya Şifreleme

function.py dosyasındaki encrypt_file fonksiyonu, verilen dosyayı AES algoritması ile şifreler. Şifreli dosya .enc uzantısı ile kaydedilir.

Fonksiyonlar
- genel_cont(file_name): MSFvenom ile Windows Meterpreter reverse TCP payload oluşturur.
- generate_key(password): Parola ile şifreleme anahtarı üretir.
- encrypt_file(filename, password): Dosyayı şifreler.

--- 

## Etik Uyarı

Bu araç yalnızca **eğitim amaçlı** kullanılmalıdır.
Başkalarına ait sistemlere yönelik herhangi bir izinsiz erişim girişimi yasadışıdır ve etik dışıdır.
Lütfen bu aracı yalnızca **test ortamlarında** kullanın. Aksi takdirde yasal sorumluluk doğurabilir.



## Lisans

Bu proje, [MIT Lisansı](LICENSE) altında lisanslanmıştır.

---

### `requirements.txt`

```txt
cryptography
os
subprocces
```
