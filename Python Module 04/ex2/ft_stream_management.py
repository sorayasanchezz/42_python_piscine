import sys

if __name__ == "__main__":
    # Display the system header
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    # Collect user input
    archivist_ID = input("Input Stream active. Enter archivist ID: ")
    status_report = input("Input Stream active. Enter status report: ")
    print()

    # Send each piece of data through its corresponding channel
    sys.stdout.write(
        f"[STANDARD] Archive status from {archivist_ID}: {status_report}\n")
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write(
        "[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")
