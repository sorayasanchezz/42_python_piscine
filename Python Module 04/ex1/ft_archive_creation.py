def create_file(filenaname: str, entries: list[str]) -> None:
    print("Initializing new storage unit:", filenaname)

    with open(filenaname, "w") as f:
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")

        for entry in entries:
            f.write(entry + "\n")
            print(entry)

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filenaname}' ready for long-term preservation.")


if __name__ == "__main__":
    filename = "new_discovery.txt"

    entry1 = "[ENTRY 001] New quantum algorithm discovered"
    entry2 = "[ENTRY 002] Efficiency increased by 347%"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee"
    entries = [entry1, entry2, entry3]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    create_file(filename, entries)
