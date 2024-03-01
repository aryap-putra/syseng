# Caesar Cipher Encryption and Decryption

![Python Badge](https://img.shields.io/badge/Made%20with-Python-blue)

This Python project implements a basic Caesar cipher algorithm, allowing you to encrypt and decrypt messages using a simple shift-based substitution method. The Caesar cipher is one of the oldest and simplest encryption techniques, dating back to ancient Rome.

## How It Works

The Caesar cipher works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. For example, with a shift of 3, 'A' becomes 'D,' 'B' becomes 'E,' and so on. The same shift value is used for both encryption and decryption.

### Features

- **Encryption**: You can input a message and a shift value to encrypt it. The encrypted message will be displayed.
- **Decryption**: If you have an encrypted message and know the shift value, you can decrypt it to reveal the original plaintext.
- **Customizable Shift**: Choose any integer as your shift value, allowing you to create different cipher variations.

## Getting Started

1. Clone this repository to your local machine.
2. Run the `caesar_cipher.py` script.
3. Follow the prompts to either encrypt or decrypt a message.

```bash
python caesar_cipher.py
```

# Example

Here's an example of encrypting the message "HELLO, WORLD!" with a shift of 3:

- Original Message: HELLO, WORLD!
- Encrypted Message: KHOOR, ZRUOG!

# Acknowledgments

- Inspired by the historical Caesar cipher.
- Created with ❤️ by Arya.
