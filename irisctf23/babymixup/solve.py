from Crypto.Cipher import AES
from pwn import xor
from binascii import unhexlify

IV1 = "4ee04f8303c0146d82e0bbe376f44e10"
CT1 = "de49b7bb8e3c5e9ed51905b6de326b39b102c7a6f0e09e92fe398c75d032b41189b11f873c6cd8cdb65a276f2e48761f6372df0a109fd29842a999f4cc4be164"
IV2 = "1fe31329e7c15feadbf0e43a0ee2f163"
CT2 = "f6816a603cefb0a0fd8a23a804b921bf489116fcc11d650c6ffb3fc0aae9393409c8f4f24c3d4b72ccea787e84de7dd0"

msg = b"Hello, this is a public message. This message contains no flags."

cipher = AES.new(unhexlify(IV1), AES.MODE_ECB)
decrypted = (cipher.decrypt(unhexlify(CT1)[:16]))
key = xor(decrypted, msg[:16])
cipher = AES.new(key, AES.MODE_CBC, unhexlify(IV2))
flag = (cipher.decrypt(unhexlify(CT2)))
print (flag)

#irisctf{the_iv_aint_secret_either_way_using_cbc}
