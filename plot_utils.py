#TIME COMPLEXITY PLOT
#Creates time-vs-key size plot.
import matplotlib.pyplot as plt
import time
from rsa_utils import generate_rsa_keys
from brute_force import factorize_brute_force

def plot_time_vs_keysize(start_bits=8, end_bits=18):
    sizes = []
    times = []

    for bits in range(start_bits, end_bits + 1, 2):
        keys = generate_rsa_keys(bits)
        _, _, t = factorize_brute_force(keys['public'][1])
        sizes.append(bits * 2)  # n is roughly 2 * bits
        times.append(t)

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, times, marker='o')
    plt.xlabel('RSA Modulus Size (bits)')
    plt.ylabel('Time to Factor (seconds)')
    plt.title('Brute Force Factorization Time vs Key Size')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("time_vs_keysize.png")
