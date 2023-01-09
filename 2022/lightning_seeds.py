import random
enc = "4fcbac835550403f13c4cc337d8d8da48351921dfb7cd47d33857432c2ee665d821227"
enc_bytes = bytes.fromhex(enc)

for i in range (0, 999):
    seed = i
    random.seed(seed)
    decrypted = ''.join(f'{chr(c ^ random.randint(0,255))}' for c in enc_bytes)
    if "DOCTF" in decrypted:
        print (decrypted)

