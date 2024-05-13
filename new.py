import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plaintext, key):
    a, b = key
    ciphertext = ''
    for char in plaintext:
        if char != ' ':
            ciphertext += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            ciphertext += ' '
    return ciphertext

def affine_decrypt(ciphertext, key):
    a, b = key
    plaintext = ''
    inverse_a = mod_inverse(a, 26)
    if inverse_a is None:
        messagebox.showerror("Error", "The provided key is not valid for decryption.")
        return plaintext
    for char in ciphertext:
        if char != ' ':
            plaintext += chr(((inverse_a * (ord(char) - 65 - b)) % 26) + 65)
        else:
            plaintext += ' '
    return plaintext

def encrypt():
    plaintext = plaintext_entry.get().upper()
    key = (int(a_entry.get()), int(b_entry.get()))
    ciphertext = affine_encrypt(plaintext, key)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

def decrypt():
    ciphertext = ciphertext_entry.get().upper()
    key = (int(a_entry.get()), int(b_entry.get()))
    plaintext = affine_decrypt(ciphertext, key)
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

# Create main window
root = tk.Tk()
root.title("Affine Cipher Encryption/Decryption")

# Create style for labels
style = ttk.Style()
style.configure("TLabel", foreground="black", background="white")

# Create labels
plaintext_label = ttk.Label(root, text="Plaintext:")
ciphertext_label = ttk.Label(root, text="Ciphertext:")
a_label = ttk.Label(root, text="Key (a):")
b_label = ttk.Label(root, text="Key (b):")
plaintext_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
ciphertext_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
a_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
b_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

# Create entry widgets
plaintext_entry = ttk.Entry(root)
ciphertext_entry = ttk.Entry(root)
a_entry = ttk.Entry(root)
b_entry = ttk.Entry(root)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)
ciphertext_entry.grid(row=1, column=1, padx=5, pady=5)
a_entry.grid(row=2, column=1, padx=5, pady=5)
b_entry.grid(row=3, column=1, padx=5, pady=5)

# Create buttons
encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt)
decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt)
encrypt_button.grid(row=4, column=0, padx=(5, 2), pady=5)  # Increase padx for left side of Encrypt button
decrypt_button.grid(row=4, column=1, padx=(2, 5), pady=5)  # Increase padx for right side of Decrypt button

# Run the application
root.mainloop()