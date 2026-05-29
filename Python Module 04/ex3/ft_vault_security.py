def read_file(filename: str) -> bool:
    try:
        print(
            "Initiating secure vault access...\n"
            "Vault connection established with failsafe protocols\n\n"
            "SECURE EXTRACTION:"
            )
        with open(filename, "r") as f:
            print(f.read())

    except FileNotFoundError as e:
        print(e)
        return False
    return True


def create_file(filename: str, entries: list[str]) -> None:
    print("\nSECURE PRESERVATION:")
    with open(filename, "w") as f:
        for entry in entries:
            f.write(entry)
            print(entry)
    print("Vault automatically sealed upon completion")


if __name__ == "__main__":
    filename_read = "classified_data.txt"
    filename_write = "security_protocols.txt"
    entries = ["[CLASSIFIED] New security protocols archived"]

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    if (read_file(filename_read)):
        create_file(filename_write, entries)
        print("\nAll vault operations completed with maximum security.")
