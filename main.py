#STREAMLIT UI
import streamlit as st
from rsa_utils import generate_rsa_keys, encrypt, decrypt
from brute_force import factorize_brute_force
from plot_utils import plot_time_vs_keysize

st.title("🔐 RSA Key Breaking Visual Simulator")

key_size = st.slider("Select RSA Key Size (bits for each prime)", 8, 18, 12)
message = st.text_input("Enter a message to encrypt", "hi")

if st.button("Generate RSA & Simulate"):
    keys = generate_rsa_keys(key_size)
    e, n = keys['public']
    d, _ = keys['private']
    st.write(f"🔑 Public Key: (e={e}, n={n})")
    st.write(f"🔒 Private Key: (d={d})")

    encrypted = encrypt(message, keys['public'])
    st.write(f"🔐 Encrypted Message: {encrypted}")

    decrypted = decrypt(encrypted, keys['private'])
    st.write(f"📜 Decrypted Message: {decrypted}")

    st.write("🛠️ Brute-Force Factorization...")
    p, q, t = factorize_brute_force(n)
    if p and q:
        st.success(f"✔️ Factors found: p={p}, q={q} in {t:.4f} seconds")
    else:
        st.error("❌ Could not factor")

if st.button("📈 Plot Time vs Key Size"):
    plot_time_vs_keysize()
    st.image("time_vs_keysize.png", use_column_width=True)
