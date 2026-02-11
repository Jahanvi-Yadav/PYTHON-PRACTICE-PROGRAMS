# Hill Cipher Encryption using given formula

K = [
    [17, 17, 5],
    [21, 18, 21],
    [2, 2, 19],  
    
]

plaintext = "pay"

# convert plaintext to numbers
P = []
for ch in plaintext:
    P.append(ord(ch) - 97)

print("Plaintext numeric values:", P)

# encryption using formula [x y z] = [p1 p2 p3] × K
C = [0, 0, 0]

C[0] = (P[0]*K[0][0] + P[1]*K[1][0] + P[2]*K[2][0]) % 26
C[1] = (P[0]*K[0][1] + P[1]*K[1][1] + P[2]*K[2][1]) % 26
C[2] = (P[0]*K[0][2] + P[1]*K[1][2] + P[2]*K[2][2]) % 26

print("After matrix multiplication (mod 26):", C)

ciphertext = ""
for val in C:
    ciphertext += chr(val + 65)

print("Ciphertext:", ciphertext)

