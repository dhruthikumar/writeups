passw1 = "Cacturne-Grass-Dark"

encrypted1 = b'kz\xc6\xb9\xd9Du\xcb\x8a\x9e\xe0\x9d\xbeo\xee\x03\xcf\xddd'
key1 = b''.join((ord(x) ^ y).to_bytes(1,'big') for (x,y) in zip(passw1, encrypted1))

f = open('encrypted_passwords.txt', 'rb')
lines = [line.rstrip() for line in f]

cnt = 0
for j in range (0, len(lines)):
    word=''
    n = len(lines[j]) if len(lines[j]) < len(key1) else len(key1)
    for i in range (0, n):
        word+=chr((lines[j][i])^(key1[i]))
    if ("Dugtrio-Ground-Stee" in word):
        encrypted2 = lines[j]

passw2 = "Dugtrio-Ground-Steelix"
key2 = b''.join((ord(x) ^ y).to_bytes(1,'big') for (x,y) in zip(passw2, encrypted2))

for j in range (0, len(lines)):
    word=''
    n = len(lines[j]) if len(lines[j]) < len(key2) else len(key2)
    for i in range (0, n):
        word+=chr((lines[j][i])^(key2[i]))
    print (word)
f.close()

    
