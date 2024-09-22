from Crypto.Cipher import AES
import binascii

def aes_cfb_decrypt(input_file, output_file):
    # Define the key and IV parts as in the C code
    
    # Initialize AES cipher in CFB mode for decryption
    cipher = AES.new(key_bytes, AES.MODE_CFB, iv=iv_bytes, segment_size=128)

    # Open the input file (encrypted) and the output file (decrypted plaintext)
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            # Read up to 1024 bytes from the input file
            encrypted_data = infile.read(0x400)
            if not encrypted_data:
                break

            # Decrypt the data
            decrypted_data = cipher.decrypt(encrypted_data)

            # Write the decrypted data to the output file
            outfile.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    aes_cfb_decrypt('flag.txt.enc', 'decrypted_flag.txt')