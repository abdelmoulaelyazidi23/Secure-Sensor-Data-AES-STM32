from Crypto.Cipher import AES
import serial, binascii

# --- Clé AES identique à celle utilisée dans ton code STM32 ---
key = bytes([
    0x00, 0x7E, 0x15, 0x16,
    0x28, 0xAE, 0xD2, 0xA6,
    0xAB, 0xF7, 0x15, 0x88,
    0x09, 0xCF, 0x4F, 0x3C
])

# --- Mode AES (ECB, identique à ton STM32) ---
cipher = AES.new(key, AES.MODE_ECB)

# --- Adapter le port selon ton PC (ex: COM5, COM7...) ---
ser = serial.Serial('COM3', 115200, timeout=1)

print("📡 Lecture du flux chiffré depuis la STM32...\n")

while True:
    data = ser.readline().strip()
    if not data:
        continue

    try:
        # Conversion du texte hexadécimal en bytes
        ciphertext = binascii.unhexlify(data)
        # Déchiffrement avec la clé AES
        plaintext = cipher.decrypt(ciphertext).decode(errors='ignore')

        print(f"🔒 Chiffré : {data.decode()}")
        print(f"🔓 Déchiffré : {plaintext}\n")

    except Exception as e:
        print(f"⚠️ Erreur : {e}")