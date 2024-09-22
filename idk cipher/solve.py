import base64

# Cipher text (Base64 encoded)
ct = 'QRVWUFdWEUpdXEVGCF8DVEoYEEIBBlEAE0dQAURFD1I='

# Decode the Base64 ciphertext
ct = base64.b64decode(ct)

# Convert each byte to a hexadecimal representation
hex_array = [format(byte, '02x') for byte in ct]
print("Hex Array:", hex_array)

arr = []
reved_arr = []

# Separate hex bytes based on their index (even/odd)
for i in range(len(hex_array)):
    if i % 2 != 0:
        reved_arr.append(hex_array[i])
    else:
        arr.append(hex_array[i])

print("Even Indices (arr):", arr)
print("Odd Indices (reved_arr):", reved_arr)

# Reverse the reversed array and append it back to the array
reved_arr = reved_arr
arr = arr + reved_arr
print("Combined Array:", [chr(int(i, 16)) for i in arr])

# Mod the hex array values by 256
mod_arr = [int(byte, 16) % 255 for byte in arr]  # Mod by 256 for each value
print("Modded Array (by 256):", mod_arr)

# Convert modded values back to hexadecimal
modded_hex = [format(val, '02x') for val in mod_arr]
print("Modded Hex Array:", modded_hex)

# Define the secret key (as a string)
secret_key = "secretkey"  # Example key, adjust as needed

# Ensure secret key repeats by using modulo and XOR each byte in the hex array
xor_result = ''.join(
    chr(int(byte, 16) ^ ord(secret_key[i % len(secret_key)]))  # XOR with corresponding key byte
    for i, byte in enumerate(reved_arr)  # For each hex byte
)
print("XOR Result:", xor_result)
xor_result = ''.join(
    chr(int(byte, 16) ^ ord(secret_key[i % len(secret_key)]))  # XOR with corresponding key byte
    for i, byte in enumerate(arr)  # For each hex byte
)



print("XOR Result:", xor_result)

# Example of reversing a string
# 234c81cf3cd2a50d77j17d3ku
