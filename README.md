# MD5C-RainbowGen

## Overview
**MD5C-RainbowGen** is a Python-based tool designed to generate MD5-Crypt rainbow tables for password security analysis and research. By hashing passwords from a wordlist with a customizable salt, it creates an efficient table of password-hash pairs, useful for testing password vulnerabilities and strengthening security.

## Features
- **MD5-Crypt Hashing**: Uses the Linux `crypt` module for secure and efficient hash generation.
- **Customizable Salt**: Modify the salt value to create unique and diverse rainbow tables.
- **Efficient for Large Wordlists**: Progress tracking ensures smooth execution even with extensive datasets.
- **Password-Hash Table Output**: Exports a ready-to-use file of password-hash pairs for reference.

## Requirements
- **Linux Operating System**: This script requires the `crypt` module, which is not supported on Windows or macOS.
- A properly formatted wordlist file (default: `wordlist.txt`).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MD5C-RainbowGen.git
   cd MD5C-RainbowGen
   ```
2. Ensure your wordlist file is available in the repository directory.

## Usage
1. Add your wordlist to the directory (default name: `wordlist.txt`).
2. Open the script and configure the salt (default: `$1$00000000`).
3. Run the script:
   ```bash
   python rainbowgen.py
   ```
4. The rainbow table will be saved as `hashed_passwords_with_salt.txt`.

## Notes
- **Linux-Only**: The `crypt` module is only available on Linux systems.
- Ensure your wordlist file is encoded in `latin-1` and has one password per line.
- For optimal performance, use a machine with sufficient memory when working with large wordlists.

## License
This project is licensed under the [MIT License](LICENSE).

<br>

Developed by Sergio Mahía
