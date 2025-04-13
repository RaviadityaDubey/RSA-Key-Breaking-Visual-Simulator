#BRUTE FORCE FACTORIZATION
import time

def factorize_brute_force(n):
    start = time.time()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            p, q = i, n // i
            end = time.time()
            return p, q, end - start
    end = time.time()
    return None, None, end - start
