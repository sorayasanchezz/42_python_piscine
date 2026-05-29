def read_file(file: str) -> None:

    # Show system header
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"\nAccessing Storage Vault: {file}")

    # Shows what's in the file
    try:
        with open(file, "r") as f:
            data = f.read()

        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(data)
        print("\nData recovery complete. Storage unit disconnected.")

    # If the file does not exist, this prevents potential errors
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    read_file("ancient_fragment.txt")
