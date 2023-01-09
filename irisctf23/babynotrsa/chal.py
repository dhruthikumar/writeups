from Crypto.Util.number import getStrongPrime

p = getStrongPrime(1024)
q = getStrongPrime(1024)

n = p*q

import secrets
e = secrets.randbelow(n)

flag = b"irisctf{REDACTED_REDACTED_REDACTED}"
assert len(flag) == 35
flag = int.from_bytes(flag, byteorder='big')

encrypted = (flag * e) % n

print(f"n: {n}")
print(f"e: {e}")
print(f"flag: {encrypted}")
flag = int.to_bytes(flag, byteorder='big')
