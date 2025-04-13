#RSA KEY GENERATION
import random
from sympy import isprime

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
    g, x, _ = egcd(e, phi)
    return x % phi if g == 1 else None

def generate_rsa_keys(bits=16):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while q == p:
        q = generate_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = modinv(e, phi)
    return {'public': (e, n), 'private': (d, n), 'primes': (p, q)}


def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(c), e, n) for c in message]

def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(c, d, n)) for c in ciphertext])