from Crypto.Cipher import AES
from binascii import unhexlify
from Crypto.Util.number import long_to_bytes
from pwn import xor

key = long_to_bytes(0x13371337133713371337133713371337)
header = "53514c69746520666f726d6174203300"

with open('challenge_enc.sqlite3', 'rb') as f:
  ciphertext = f.read()

enc_iv = xor (ciphertext[:16], unhexlify(header))
cipher = AES.new(key, AES.MODE_ECB)
iv = cipher.decrypt (enc_iv)

cipher = AES.new(key, AES.MODE_OFB, iv)
pt = (cipher.decrypt(ciphertext))

with open('plaintext.sqlite3', 'wb') as f:
  f.write(pt)
  
 # irisctf{g0tt4_l0v3_s7re4mciph3rs}
