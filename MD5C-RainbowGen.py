import crypt

# Salt and output file configuration
salt = "$1$00000000"  # Salt
password_file = "wordlist.txt"  # Password file
output_file = "hashed_passwords_with_salt.txt"  # File to store generated hashes

def display_banner():
    """Displays a banner with program information."""
    print("  ___      _      _                __  __ ___  ___  ___ ")
    print(" | _ \\__ _(_)_ _ | |__  _____ __ _|  \\/  |   \\| __|/ __|")
    print(" |   / _` | | ' \\| '_ \\/ _ \\ V  V / |\\/| | |) |__ \\ (__ ")
    print(" |_|_\\__,_|_|_||_|_.__/\\___/\\_/\\_/|_|  |_|___/|___/\\___|\n")
    print("Developed By FilliusMahiae\n")


def main():
    """Main function to generate MD5-Crypt hashes from a wordlist."""
    display_banner()
    
    # Initialize the counter for generated hashes
    generatedSum = 0

    try:
        # Open the password file
        with open(password_file, "r", encoding="latin-1") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The password file '{password_file}' was not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading the password file: {e}")
        return

    try:
        # Open the output file for writing hashes
        with open(output_file, "w") as f_out:
            for password in passwords:
                # Increment the counter
                generatedSum += 1

                # Show progress every million hashes
                if generatedSum % 1000000 == 0:
                    print(f"Generated: {generatedSum}")
                
                # Generate the MD5 Crypt hash from the salt+password combination
                md5_hash = crypt.crypt(password, salt)
                
                # Save the hash and original password to the output file
                f_out.write(f"{md5_hash}:{password}\n")
    except Exception as e:
        print(f"An error occurred while writing to the output file: {e}")
        return

    print(f"Hashes successfully generated and saved to '{output_file}'.")

if __name__ == "__main__":
    main()
