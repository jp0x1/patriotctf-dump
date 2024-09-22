#include <openssl/evp.h>
#include <openssl/err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void handleErrors(void) {
    ERR_print_errors_fp(stderr);
    abort();
}

int decrypt(unsigned char *ciphertext, int ciphertext_len, unsigned char *key,
            unsigned char *iv, unsigned char *plaintext) {
    EVP_CIPHER_CTX *ctx;
    int len;
    int plaintext_len;

    // Create and initialize the context
    if (!(ctx = EVP_CIPHER_CTX_new())) handleErrors();

    // Initialize the decryption operation.
    if (1 != EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv)) handleErrors();

    // Provide the message to be decrypted and obtain the plaintext output.
    if (1 != EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, ciphertext_len)) handleErrors();
    plaintext_len = len;

    // Finalize the decryption. Further plaintext bytes may be written at this stage.
    if (1 != EVP_DecryptFinal_ex(ctx, plaintext + len, &len)) handleErrors();
    plaintext_len += len;

    // Clean up
    EVP_CIPHER_CTX_free(ctx);

    return plaintext_len;
}

int main() {
    // Hardcoded 32-byte key (256 bits for AES-256)
    unsigned char key[32] = {
        0x60, 0x3d, 0xeb, 0x10, 0x15, 0xca, 0x71, 0xbe,
        0x2b, 0x73, 0xae, 0xf0, 0x85, 0x7d, 0x77, 0x81,
        0x1f, 0x35, 0x2c, 0x07, 0x3b, 0x61, 0x08, 0xd7,
        0x2d, 0x98, 0x10, 0xa3, 0x09, 0x14, 0xdf, 0xf4
    };

    // Hardcoded 16-byte IV (128 bits for AES)
    unsigned char iv[16] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f
    };

    // File name for the ciphertext
    const char *ciphertext_file = "flag.txt.enc";

    // Open and read the ciphertext from file
    FILE *ciphertext_fp = fopen(ciphertext_file, "rb");
    if (!ciphertext_fp) {
        perror("Unable to open ciphertext file");
        return 1;
    }
    // Determine the size of the ciphertext
    fseek(ciphertext_fp, 0, SEEK_END);
    long ciphertext_len = ftell(ciphertext_fp);
    fseek(ciphertext_fp, 0, SEEK_SET);

    // Allocate memory for the ciphertext and read it from the file
    unsigned char *ciphertext = (unsigned char *)malloc(ciphertext_len);
    if (!ciphertext) {
        perror("Memory allocation failed");
        fclose(ciphertext_fp);
        return 1;
    }
    if (fread(ciphertext, 1, ciphertext_len, ciphertext_fp) != ciphertext_len) {
        perror("Failed to read ciphertext");
        free(ciphertext);
        fclose(ciphertext_fp);
        return 1;
    }
    fclose(ciphertext_fp);

    // Buffer to hold the decrypted plaintext
    unsigned char *plaintext = (unsigned char *)malloc(ciphertext_len);
    if (!plaintext) {
        perror("Memory allocation failed");
        free(ciphertext);
        return 1;
    }

    // Perform the decryption
    int decrypted_len = decrypt(ciphertext, ciphertext_len, key, iv, plaintext);

    // Null-terminate the plaintext if it's a string
    plaintext[decrypted_len] = '\0';

    // Print the decrypted plaintext
    printf("Decrypted text: %s\n", plaintext);

    // Clean up
    free(ciphertext);
    free(plaintext);

    return 0;
}